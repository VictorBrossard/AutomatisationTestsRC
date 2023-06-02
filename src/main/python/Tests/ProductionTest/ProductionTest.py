# Author        : Victor BROSSARD
# Description   : class that manages the production test run

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import time
import datetime

from Useful.AllConstant import CONSTANT_TEST_PIECES_FOLDER_PATH
from Useful.AllConstant import CONSTANT_START_PROD_FILE
from Useful.AllConstant import CONSTANT_TEST_SETTINGS_FILE_NAME

from Interaction.ExecuteTestFile import ExecuteTestFile

from Database.Database import Database

from RCTest.Test import Test

#-----------------------------------------------------------------------------------------------------

class ProductionTest(Test):
    """ `+`
    :class:`ProductionTest` manages the production test run
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

        super().__init__(test_folder_path, database, folder_name)

        self.has_prg_changed = (loaded_prg != wanted_prg)
        self.start_time = None


    def launch_test(self) -> (datetime.datetime | None):
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
            name_file = self.trace_file.find_trace()

            if name_file == "":
                break

            time.sleep(1)

            self.launch_test_file(name_file)

        return self.start_time
    

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

            self.execute_file_list(file_list)

        elif name_file == "program_name.txt":
            # executes pattern to change program
            file_list = [
                f"{self.test_folder_path}\\program_name.txt",
                f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\enter.txt",
                f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\placement_button.txt",
                f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\partial_prod_prg_change.txt",
                f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\program_change.txt"
            ]

            self.execute_file_list(file_list)

        elif name_file == "placement_button.txt":
            # execution of the pattern that partially starts the machine without changing the program
            file_list = [
                f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\placement_button.txt",
                f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\partial_prod_no_prg_change.txt",
                f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\prod_parameter.txt"
            ]

            self.execute_file_list(file_list)

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
        
        fil = open(f"{self.test_folder_path}\\{CONSTANT_TEST_SETTINGS_FILE_NAME}")
        settings_lines = fil.readlines()
        fil.close()

        # decomposition of the tuple to calculate the max production time
        try:
            unit_time = float(max_time_tuple[0][0])
            nb_cards_to_made = int(settings_lines[1]) - int(settings_lines[2])
            time_for_a_card = unit_time/1000
            time_for_cards = time_for_a_card * nb_cards_to_made - 3 # the 3 corresponds to the waiting time for the start of the function
        except Exception as e:
            print(f"[ERREUR] {e}")
            return
        
        if nb_cards_to_made <= 0:
            return

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