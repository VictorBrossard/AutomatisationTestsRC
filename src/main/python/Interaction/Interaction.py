# Author        : Victor BROSSARD
# Description   : Object that does the interactions instead of the user

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import os
import time

from GraphicInterface.MessageBox import MessageBox
from GraphicInterface.UserEntryPopUp import UserEntryPopUp
from GraphicInterface.SettingsInterface import SettingsInterface
from GraphicInterface.SimpleQuestionInterface import SimpleQuestionInterface

from Interaction.Screenshot import Screenshot
from Interaction.ExecuteTest import ExecuteTest
from Interaction.InputRecorder import InputRecorder
from Interaction.ManageSoftwares import ManageSoftwares

from FilesManagement.Folders.ManageFolders import CONSTANT_TEST_PIECES_FOLDER_PATH
from FilesManagement.Folders.ManageFolders import CONSTANT_TEST_AVAILABLE_FOLDER_PATH
from FilesManagement.Folders.TestReportFolder import TestReportFolder
from FilesManagement.Folders.ManageFolders import ManageFolders

from FilesManagement.Files.ManipulationSettingsFile import ManipulationSettingsFile
from FilesManagement.Files.ManageSpecificFiles import ManageSpecificFiles
from FilesManagement.Files.ManageReportFile import ManageReportFile

from RCTest.Precondition import Precondition
from RCTest.PostCondition import PostCondition

from Database.Database import Database

#-----------------------------------------------------------------------------------------------------

class Interaction(object):
    """ `+`
    :class:`Interaction` does the interactions instead of the user
    """

    def __init__(self):
        """ `-`
        `Type:` Constructor
        """

        self.line_settings_file = ManipulationSettingsFile() # read the file that contains the parameters
        self.rc_window_name = self.line_settings_file.get_line(5)


    def create_test(self):
        """ `+`
        `Type:` Procedure
        `Description:` creates an entire test
        """

        # pop-up asking for the name of the file we are going to create to save the test
        pop_up = UserEntryPopUp("Create Tests", ["Entrez le nom du test :", "Nombre de cartes à produire :"], [0, 1])
        pop_up.mainloop()

        # recovery of input values
        user_entry_list = pop_up.get_user_entries()

        # verification that the user has given us all the values
        for entries in user_entry_list:
            if entries == "":
                MessageBox("ERREUR Manque d'information", "[ERREUR] Vous n'avez pas remplis toutes les cases.").mainloop()
                return
            
        # creation of the file that stores the test pieces
        test_folder_path = ManageFolders().create_test_folder(user_entry_list[0])

        if test_folder_path == "":
            MessageBox("ERREUR Nom de test", "[ERREUR] Ce nom de test existe déjà.").mainloop()
            return

        # creation of test piece files
        new_file = ManageSpecificFiles()
        new_file.create_file(test_folder_path, f"{user_entry_list[0]}_settings.txt", user_entry_list)
        new_file.create_execution_file(test_folder_path, "name.txt", user_entry_list[0])
        new_file.create_execution_file(test_folder_path, "card_to_make.txt", user_entry_list[1])
        new_file.create_execution_file(test_folder_path, "card_make.txt", "0")

        # asks the user a question
        before_production = SimpleQuestionInterface("Avant production", "Avez-vous des choses à faire avant la production ?")
        before_production.mainloop()

        if before_production.get_is_yes():
            # software opening
            soft = ManageSoftwares()
            soft.open_soft()

            time.sleep(6) # waiting time for the opening of the software

            # start of the recording
            MessageBox("Enregistrement", "[INFO] L'enregistrement va commencer.").mainloop()
            precondition = InputRecorder("precondition", test_folder_path)

            # verification that the file did not have a problem at its creation
            if precondition.get_was_file_created():
                precondition.start_recording()
            else:
                return
            
            # software closure
            soft.close_soft()
            
        # creation of the only file that the user can select to run the tests
        new_file.create_file(CONSTANT_TEST_AVAILABLE_FOLDER_PATH, f"{user_entry_list[0]}.txt", [test_folder_path])


    def execute_test(self, database: Database, file_paths_list: list):
        """ `+`
        `Type:` Procedure
        `Description:` execute all the test files in the parameter list
        :param:`database:` object that manages the interaction with the database
        :param:`file_paths_list:` list of file paths that store the paths to the test folders
        """

        # execution of each file in the list
        for fil in file_paths_list:
            # creation of a file for the test report
            file_name, extension = os.path.splitext(os.path.basename(fil))
            folder = TestReportFolder(file_name)

            # will look for all the files that compose a test
            all_test_file = self.__get_all_test_file(fil, folder.get_now())
            if all_test_file == []:
                return

            # launches the general precondition for launching a test
            Precondition().start_precondition(database)
            time.sleep(6.5)

            # execution of each test piece
            for test_piece in all_test_file:
                if os.path.basename(test_piece) == "start_prod.txt":
                    ExecuteTest().read_test_file(test_piece)
                    self.__prod_waiting_time(database, folder.get_folder_name())
                else:
                    ExecuteTest().read_test_file(test_piece)
                    time.sleep(0.5)

            # take a screenshot
            Screenshot().take_screenshot(folder.get_screenshot_folder_path(), "screenshot_report")

            # create report
            ManageReportFile(database, folder.get_folder_path(), fil, folder.get_now()).create_report_file()

            # launches the general postcondition to stop a test
            PostCondition().start_postcondition(database, folder.get_folder_path())


    def test_pieces(self):
        """ `+`
        `Type:` Procedure
        `Description:` record a test piece
        """

        # request the name of the test piece to the user
        pop_up = UserEntryPopUp("Create Test Pieces", ["Entrez le nom du bout de test :"], [0])
        pop_up.mainloop()

        # recovery of input values
        user_entry_list = pop_up.get_user_entries()

        # verification that the user has given us a value
        if user_entry_list[0] == "":
            MessageBox("ERREUR Manque d'information", "[ERREUR] Vous n'avez pas remplis toutes les cases.").mainloop()
            return
            
        # check that the name is not already taken
        if os.path.exists(f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\{user_entry_list[0]}.txt"):
            MessageBox("ERREUR Nom de fichier", "[ERREUR] Ce fichier existe déjà.").mainloop()
            return
        
        # software opening
        soft = ManageSoftwares()
        soft.open_soft()

        time.sleep(6) # we wait until the software is well opened
        MessageBox("Enregistrement", "[INFO] L'enregistrement commence.").mainloop()
        
        # recording of user's actions
        precondition = InputRecorder(user_entry_list[0], CONSTANT_TEST_PIECES_FOLDER_PATH)

        if precondition.get_was_file_created():
            precondition.start_recording()
        else:
            return

        # software closure
        soft.close_soft()


    def __get_all_test_file(self, file_with_path: str, date_time: str) -> list:
        """ `-`
        `Type:` Function
        `Description:` put the test files in the right order of execution
        :param:`file_with_path:` full path of a file
        :param:`date_time:` date and time of the test
        `Return:` list of files to be executed
        """

        # get the path in the file
        try:
            fil = open(file_with_path, 'r')
            path_line = fil.readlines()[0].rstrip()
            fil.close()
        except Exception as e:
            MessageBox("ERREUR Fichier", f"[ERREUR] {e}").mainloop()
            return []
        
        # execution file to write the date after the test name
        ManageSpecificFiles().create_execution_file(path_line, "last_execution.txt", f"_{date_time}")

        # list of files to be executed in the right order
        file_list = [
            f"{path_line}\\precondition.txt",
            f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\partial_prod.txt",
            f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\name_prod.txt",
            f"{path_line}\\name.txt",
            f"{path_line}\\last_execution.txt",
            f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\nb_card_to_make_prod.txt",
            f"{path_line}\\card_to_make.txt",
            f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\nb_card_make_prod.txt",
            f"{path_line}\\card_make.txt",
            f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\start_prod.txt",
            #f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\stop_prod.txt",
            f"{path_line}\\postcondition.txt"
        ]

        for fil in file_list:
            if not os.path.exists(fil):
                file_list.remove(fil)

        return file_list
    

    def __prod_waiting_time(self, database: Database, folder_name: str):
        """ `-`
        `Type:` Procedure
        `Description:` makes the software wait for the production time
        :param:`database:` object that manages the interaction with the database
        :param:`folder_name:` name of the file which is equivalent to the name of the test in the database
        """

        time.sleep(2) # pause to let the database refresh

        # get the production time of the card and the number of cards to make in the database
        max_time_tuple = database.get_tuples(
            "SELECT MAX(wrms.ExpectedCycleTime), (w.NbUnitsToDo div wrm.NbUnitsPerWork) AS cartes FROM workorders w JOIN workorderrecipemachines wrm ON w.IdWorkOrder = wrm.IdWorkOrder JOIN workorderrecipemachinestages wrms ON wrm.IdWorkOrderRecipeMachine = wrms.IdWorkOrderRecipeMachine WHERE w.Name = ?", 
            [folder_name]
        )

        # verification that there were no bugs in the execution of the command
        if len(max_time_tuple) != 1:
            return

        # decomposition of the tuple to calculate the max production time
        unit_time = float(max_time_tuple[0][0])
        nb_cards_to_made = int(max_time_tuple[0][1])
        time_for_a_card = unit_time/1000
        time_for_cards = time_for_a_card * nb_cards_to_made

        card_made = 0

        # loop that allows the time to wait for the execution of the next file
        while time_for_cards > 0  and card_made != nb_cards_to_made:
            # sql command that fetches the number of cards in works
            card_made_tuple = database.get_tuples(
                "SELECT COUNT(*) FROM (workorders wo JOIN workorderrecipemachines worm ON wo.IdWorkOrder = worm.IdWorkOrder) JOIN works w ON worm.IdWorkOrderRecipeMachine = w.IdWorkOrderRecipeMachine WHERE wo.Name = ?", 
                [folder_name]
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