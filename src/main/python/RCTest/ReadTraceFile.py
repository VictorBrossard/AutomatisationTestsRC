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

from Useful.AllConstant import CONSTANT_TESTS_FOLDER_PATH
from Useful.AllConstant import CONSTANT_TEST_PIECES_FOLDER_PATH
from Useful.AllConstant import CONSTANT_START_PROD_FILE
from Useful.AllConstant import CONSTANT_TRACE_FILE_NAME

from Useful.UsefulFunction import starts_with

from Interaction.ExecuteTestFile import ExecuteTestFile

from Database.Database import Database

#-----------------------------------------------------------------------------------------------------

class ReadTraceFile(object):
    """ `+`
    :class:`ReadTraceFile` reads the trace file and launches the right files for the test
    """

    def __init__(self, test_folder_path: str, database: Database, folder_name: str, loaded_prg: str, wanted_prg: str):
        """ `-`
        `Type:` Constructor
        :param:`test_folder_path:` test folder path
        :param:`database:` object that manages the interaction with the database
        :param:`folder_name:` name of the folder which is equivalent to the name of the test in the database
        :param:`loaded_prg:` name of the last program loaded in RC
        :param:`wanted_prg:` program desired by the user
        """

        self.trace_file_path = ManipulationSettingsFile().get_line(7)
        self.database = database
        self.folder_name = folder_name
        self.test_folder_path = test_folder_path
        self.has_prg_changed = (loaded_prg != wanted_prg)
        self.start_time = None
        
    
    def launch_prod_test(self) -> (datetime.datetime | None):
        """ `+`
        `Type:` Function
        `Definition:` starts the execution of the complete test
        `Return:` time at which the production is started
        """

        name_file = ""

        if self.has_prg_changed:
            self.launch_test_file("prod_program.txt")
        else:
            self.launch_test_file("placement_button.txt")

        # execution of all files
        while name_file != CONSTANT_START_PROD_FILE:
            name_file = self.find_trace()

            if name_file == "":
                break

            self.launch_test_file(name_file)

        return self.start_time


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

        # line of the trace file that we want to find to be able to execute certain files
        file_name_dictionary = {
            "ClgMyDialog::OnInitDialog() : PRDBD_IDD_SUIVI_LOT" : "name.txt",
            "CFX Trace : CTrSui::RecipeActivated" : CONSTANT_START_PROD_FILE,
            "ClgMyDialog::OnInitDialog() : PRG_IDD_SELECTION" : "program_name.txt",
            #"ClgMyDialog::OnDestroy() : PRG_IDD_SELECTION" : "partial_prod_prg_change.txt",
            "ClgMyDialog::OnInitDialog() : RC_IDD_LOCAL_LIST" : "local_list_boxes.txt",
            #"ClgMyDialog::OnDestroy() : IU_IDD_MAINMENU_PROD" : "destroy"
        }

        for key in file_name_dictionary:
            if self.__find_word(key, line):
                file_to_execute = file_name_dictionary[key]
                return True, file_to_execute

        return False, ""
    

    def launch_test_file(self, name_file: str):
        """ `+`
        `Type:` Procedure
        `Description:` execute the right files according to the name given in parameter
        :param:`name_file:` name of the file to be executed
        """

        if name_file == "":
            # case of error
            return
        
        elif name_file == CONSTANT_START_PROD_FILE:
            # pattern execution to start production
            if self.has_prg_changed:
                time.sleep(3)
                ExecuteTestFile().read_test_file(f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\card_recalibration.txt")
                
            time.sleep(3)
            self.start_time = datetime.datetime.now()
            ExecuteTestFile().read_test_file(f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\{CONSTANT_START_PROD_FILE}")
            self.__prod_waiting_time()
            ExecuteTestFile().read_test_file(f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\escape.txt")

        elif name_file == "name.txt":
            # pattern execution to fill the OF
            file_list = [
                f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\delete.txt",
                f"{self.test_folder_path}\\name.txt",
                f"{self.test_folder_path}\\last_execution.txt",
                f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\down.txt",
                f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\delete.txt",
                f"{self.test_folder_path}\\card_to_make.txt",
                f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\down.txt",
                f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\delete.txt",
                f"{self.test_folder_path}\\card_make.txt",
                f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\validate_prod.txt"
            ]

            self.__execute_file_list(file_list)

        elif name_file == "program_name.txt":
            # executes pattern to change program
            file_list = [
                f"{self.test_folder_path}\\program_name.txt",
                f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\enter.txt",
                f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\placement_button.txt",
                f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\partial_prod_prg_change.txt",
                f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\program_change.txt"
            ]

            self.__execute_file_list(file_list)

        elif name_file == "placement_button.txt":
            # execution of the pattern that partially starts the machine without changing the program
            file_list = [
                f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\placement_button.txt",
                f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\partial_prod_no_prg_change.txt",
                f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\prod_parameter.txt"
            ]

            self.__execute_file_list(file_list)

        elif name_file == "close_rc.txt":
            # execute pattern to close RC
            ExecuteTestFile().read_test_file(f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\close_rc.txt")
            time.sleep(1)

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


    def __execute_file_list(self, file_list: list[str]):
        """ `-`
        `Type:` Procedure
        `Description:` executes all files in the list
        :param:`file_list:` file to run
        """

        for fil in file_list:
            ExecuteTestFile().read_test_file(fil)
            time.sleep(0.2)


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