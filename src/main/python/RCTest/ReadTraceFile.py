# Author        : Victor BROSSARD
# Description   : Class that reads the trace file and launches the right files for the test

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import os
import shutil
import chardet
import time
import datetime

from FilesManagement.Files.ManipulationSettingsFile import ManipulationSettingsFile
from FilesManagement.Files.ManageSpecificFiles import ManageSpecificFiles

from FilesManagement.Folders.ManageFolders import CONSTANT_TESTS_FOLDER_PATH
from FilesManagement.Folders.ManageFolders import CONSTANT_TEST_PIECES_FOLDER_PATH

from Interaction.ExecuteTestFile import ExecuteTestFile

from Database.Database import Database

#-----------------------------------------------------------------------------------------------------
# Initialization of constants
CONSTANT_START_PROD_FILE = "start_prod.txt"

#-----------------------------------------------------------------------------------------------------

class ReadTraceFile(object):
    """ `+`
    :class:`ReadTraceFile` reads the trace file and launches the right files for the test
    """

    def __init__(self, test_available: str, database: Database, folder_name: str, create_folder_time: str, loaded_prg: str):
        """ `-`
        `Type:` Constructor
        :param:`test_available:` test file name
        :param:`database:` object that manages the interaction with the database
        :param:`folder_name:` name of the folder which is equivalent to the name of the test in the database
        :param:`create_folder_time:` date of creation of the report folder
        :param:`loaded_prg:` name of the last program loaded in RC
        """

        self.trace_file_path = ManipulationSettingsFile().get_line(8)
        self.database = database
        self.folder_name = folder_name
        self.loaded_prg = loaded_prg

        try:
            fil = open(test_available, 'r')
            self.test_folder_path = fil.readlines()[0].rstrip()
            fil.close()
        except Exception:
            return
        
        self.has_prg_changed = self.__program_changed()
        
        # execution file to write the date after the test name
        ManageSpecificFiles().create_execution_file(self.test_folder_path, "last_execution.txt", f"_{create_folder_time}")
        
    
    def launch(self):
        """ `+`
        `Type:` Function
        `Definition:` starts the execution of the complete test
        `Return:` time at which the production is started
        """

        name_file = ""

        if self.has_prg_changed:
            self.__launch_test_file("prod_program.txt")
        else:
            self.__launch_test_file("partial_prod_no_prg_change.txt")

        # execution of all files
        while name_file != CONSTANT_START_PROD_FILE:
            name_file = self.__find_trace()
            self.__launch_test_file(name_file)
        
        """self.__launch_test_file("prod_program.txt")
        self.__launch_test_file("program_name.txt")
        self.__launch_test_file("validate_prog.txt")
        self.__launch_test_file("partial_prod.txt")
        self.__launch_test_file("program_change.txt")
        self.__launch_test_file("local_list_boxes.txt")
        self.__launch_test_file("name_prod.txt")
        self.__launch_test_file("card_recalibration.txt")
        self.__launch_test_file(CONSTANT_START_PROD_FILE)"""

        return self.start_time


    def __find_trace(self):
        """ `-`
        `Type:` Function
        `Description:` digs into the traces to find out which file is to be executed
        `Return:` the file name to be executed
        """

        path_trace_file = f"{self.trace_file_path}\\ieee001.TRC"
        path_copy_trace_file = f"{CONSTANT_TESTS_FOLDER_PATH}\\ieee001.TRC"
        name_file = ""

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
                    boolean, name_file = self.__find_file_to_execute(line) # search for the next file to run

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

        return name_file


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

        # line of the trace file that we want to find to be able to execute certain files
        file_name_dictionary = {
            "ClgMyDialog::OnInitDialog() : PRDBD_IDD_SUIVI_LOT" : "name_prod.txt",
            "CFX Trace : CTrSui::RecipeActivated" : CONSTANT_START_PROD_FILE,
            "ClgMyDialog::OnInitDialog() : PRG_IDD_SELECTION" : "program_name.txt",
            #"ClgMyDialog::OnDestroy() : PRG_IDD_SELECTION" : "partial_prod_prg_change.txt",
            "ClgMyDialog::OnInitDialog() : RC_IDD_LOCAL_LIST" : "local_list_boxes.txt"
        }

        for key in file_name_dictionary:
            if self.__find_word(key, line):
                file_to_execute = file_name_dictionary[key]
                return True, file_to_execute

        return False, ""
    

    def __launch_test_file(self, name_file: str):
        """ `-`
        `Type:` Procedure
        `Description:` execute the right files according to the name given in parameter
        :param:`name_file:` name of the file to be executed
        """

        if name_file == "":
            # case of error
            return
        
        elif name_file == CONSTANT_START_PROD_FILE:
            if self.has_prg_changed:
                time.sleep(3)
                ExecuteTestFile().read_test_file(f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\card_recalibration.txt")
                
            time.sleep(3)

            # execution of the file start_prod.txt
            self.start_time = datetime.datetime.now()
            ExecuteTestFile().read_test_file(f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\{name_file}")
            self.__prod_waiting_time()

        elif name_file == "name_prod.txt":
            # execution of the file name_prod.txt
            file_list = [
                f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\name_prod.txt",
                f"{self.test_folder_path}\\name.txt",
                f"{self.test_folder_path}\\last_execution.txt",
                f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\nb_card_to_make_prod.txt",
                f"{self.test_folder_path}\\card_to_make.txt",
                f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\nb_card_make_prod.txt",
                f"{self.test_folder_path}\\card_make.txt",
                f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\validate_prod.txt"
            ]

            for fil in file_list:
                ExecuteTestFile().read_test_file(fil)
                time.sleep(0.2)

        elif name_file == "program_name.txt":
            # execution of the file program_name.txt
            file_list = [
                f"{self.test_folder_path}\\program_name.txt",
                f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\validate_prog.txt",
                f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\partial_prod_prg_change.txt",
                f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\program_change.txt"
            ]

            for fil in file_list:
                ExecuteTestFile().read_test_file(fil)
                time.sleep(0.2)

        elif name_file == "partial_prod_no_prg_change.txt":
            # execution of the file partial_prod_no_prg_change.txt
            file_list = [
                f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\partial_prod_no_prg_change.txt",
                f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\prod_parameter.txt"
            ]

            for fil in file_list:
                ExecuteTestFile().read_test_file(fil)
                time.sleep(0.2)

        else:
            ExecuteTestFile().read_test_file(f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\{name_file}")
            time.sleep(0.5)


    def __prod_waiting_time(self):
        """ `-`
        `Type:` Procedure
        `Description:` makes the software wait for the production time
        """

        time.sleep(3) # pause to let the database refresh

        # get the production time of the card and the number of cards to make in the database
        max_time_tuple = self.database.get_tuples(
            "SELECT MAX(wrms.ExpectedCycleTime), (w.NbUnitsToDo div wrm.NbUnitsPerWork) AS cartes FROM workorders w JOIN workorderrecipemachines wrm ON w.IdWorkOrder = wrm.IdWorkOrder JOIN workorderrecipemachinestages wrms ON wrm.IdWorkOrderRecipeMachine = wrms.IdWorkOrderRecipeMachine WHERE w.Name = ?", 
            [self.folder_name]
        )

        # verification that there were no bugs in the execution of the command
        if len(max_time_tuple) != 1:
            return

        # decomposition of the tuple to calculate the max production time
        unit_time = float(max_time_tuple[0][0])
        nb_cards_to_made = int(max_time_tuple[0][1])
        time_for_a_card = unit_time/1000
        time_for_cards = time_for_a_card * nb_cards_to_made - 3 # the 3 corresponds to the waiting time for the start of the function

        card_made = 0

        # loop that allows the time to wait for the execution of the next file
        while time_for_cards > 0  and card_made != nb_cards_to_made:
            # sql command that fetches the number of cards in works
            card_made_tuple = self.database.get_tuples(
                "SELECT COUNT(*) FROM (workorders wo JOIN workorderrecipemachines worm ON wo.IdWorkOrder = worm.IdWorkOrder) JOIN works w ON worm.IdWorkOrderRecipeMachine = w.IdWorkOrderRecipeMachine WHERE wo.Name = ?", 
                [self.folder_name]
            )

            card_made = int(card_made_tuple[0][0])
            
            if card_made == nb_cards_to_made:
                # if there is the right number of cards in works we wait for the end of the production of the last card
                time.sleep(time_for_a_card)
            else:
                # in the other case, we wait a little while before asking the database again until we reach the maximum production time
                # if we are in this case then there was surely a problem
                time.sleep(2)
                time_for_cards = time_for_cards - 2


    def __program_changed(self):
        """ `-`
        `Type:` Function
        `Description:` check if the previously used program is the same as the one you want 
        `Return:` bool
        """

        test_name = os.path.basename(self.test_folder_path)
        setting_file_path = f"{self.test_folder_path}\\{test_name}_settings.txt"

        try:
            fil = open(setting_file_path, 'r')
            program_name = fil.readlines()[3].rstrip()
            fil.close()
        except Exception:
            return False
        
        if program_name == self.loaded_prg:
            return False
        else:
            return True
