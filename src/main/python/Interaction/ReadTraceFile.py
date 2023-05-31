# Author        : Victor BROSSARD
# Description   : Class that reads the trace file

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import os
import shutil
import chardet

from FilesManagement.Files.ManipulationSettingsFile import ManipulationSettingsFile

from Useful.AllConstant import CONSTANT_TESTS_FOLDER_PATH
from Useful.AllConstant import CONSTANT_TRACE_FILE_NAME
from Useful.AllConstant import CONSTANT_TRACE_DICTIONNARY

from Useful.UsefulFunction import starts_with

#-----------------------------------------------------------------------------------------------------

class ReadTraceFile(object):
    """ `+`
    :class:`ReadTraceFile` reads the trace file
    """

    def __init__(self):
        """ `-`
        `Type:` Constructor
        """

        self.trace_file_path = ManipulationSettingsFile().get_line(7)


    def find_trace(self) -> str:
        """ `-`
        `Type:` Function
        `Description:` digs into the traces to find out which file is to be executed
        `Return:` the file name to be executed
        """

        path_trace_file = self.__find_last_modif_trace_file()

        # verifies that a trace file has been found
        if path_trace_file is None:
            return ""
        
        path_copy_trace_file = f"{CONSTANT_TESTS_FOLDER_PATH}\\{os.path.basename(path_trace_file)}"
        file_to_run = ""

        shutil.copy(path_trace_file, CONSTANT_TESTS_FOLDER_PATH) # copy the file to be able to manipulate it

        # seeks file encoding
        trace_file = open(path_copy_trace_file, "rb")
        result = chardet.detect(trace_file.read())
        trace_file.close()

        # open the file starting from the end
        trace_file = open(path_copy_trace_file, 'r', encoding=result['encoding'])
        trace_file.seek(0, 2) 
        pos = trace_file.tell()

        # browse the file line by line upwards
        while pos >= 0:
            trace_file.seek(pos) # move to the current position
            try:
                next_char = trace_file.read(1) # read the following character

                if next_char == "\n":
                    line = trace_file.readline().rstrip()
                    boolean, file_to_run = self.__find_file_to_execute(line) # search for the next file to run

                    if boolean:
                        break
                    else:
                        pos -= len(line) + 1 # update the position to point to the previous line
                else:
                    pos -= 1 # move the cursor forward by one character if you have not reached a new line
            except Exception:
                pos -= 1

        trace_file.close()              # close the file
        os.remove(path_copy_trace_file) # deleting the file that has been copied

        return file_to_run


    def __find_word(self, word: str, string: str) -> bool:
        """ `-`
        `Type:` Function
        `Description:` check if the word is in the character string
        :param:`word:` word to check
        :param:`string:` string with which we check the word
        `Return:` bool
        """

        if word in string:
            return True
        else:
            return False
        

    def __find_file_to_execute(self, line: str) -> tuple[bool, str]:
        """ `-`
        `Type:` Function
        `Description:` finds the right file to run based on the line in the trace file
        :param:`line:` line in the trace file
        `Return:` a bool and the name of the file to be executed
        """

        for key in CONSTANT_TRACE_DICTIONNARY:
            if self.__find_word(key, line):
                file_to_execute = CONSTANT_TRACE_DICTIONNARY[key]
                return True, file_to_execute

        return False, ""


    def __find_last_modif_trace_file(self) -> (str | None):
        """ `-`
        `Type:` Function
        `Description:` find the last modified trace file to make sure you're on the right one
        `Return:` name of the trace file with its path or None if there is none
        """

        last_modified_file = None
        last_modification_date = None

        # browse all folder file names
        for file_name in os.listdir(self.trace_file_path):
            # verifies that the file is an CONSTANT_TRACE_FILE_NAME file
            if starts_with(file_name, CONSTANT_TRACE_FILE_NAME):
                file_path = os.path.join(self.trace_file_path, file_name)
                modification_date = os.path.getmtime(file_path)

                # verifies that the file is the last one modified
                if last_modification_date is None or modification_date > last_modification_date:
                    last_modified_file = file_path
                    last_modification_date = modification_date


        if last_modified_file is not None:
            return last_modified_file
        else:
            print(f"[ERREUR] Aucun fichier trace n'existe dans le dossier : {self.trace_file_path}")
            return None