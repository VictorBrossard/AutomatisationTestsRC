# Author        : Victor BROSSARD
# Description   : Object that does the interactions instead of the user

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import os
import time

from GraphicInterface.MessageBox import MessageBox
from GraphicInterface.UserEntryPopUp import UserEntryPopUp

from Interaction.Screenshot import Screenshot
from Interaction.InputRecorder import InputRecorder
from Interaction.ManageSoftwares import ManageSoftwares

from FilesManagement.Folders.TestReportFolder import TestReportFolder
from FilesManagement.Folders.ManageFolders import ManageFolders

from FilesManagement.Files.ManipulationSettingsFile import ManipulationSettingsFile
from FilesManagement.Files.ManageSpecificFiles import ManageSpecificFiles
from FilesManagement.Files.ManageReportFile import ManageReportFile

from RCTest.Precondition import Precondition
from RCTest.PostCondition import PostCondition
from RCTest.ReadTraceFile import ReadTraceFile

from Database.Database import Database

from Useful.AllConstant import CONSTANT_TEST_PIECES_FOLDER_PATH
from Useful.AllConstant import CONSTANT_TEST_AVAILABLE_FOLDER_PATH
from Useful.AllConstant import CONSTANT_SHORT_FORMAT_DATES_DATABASE

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


    def create_test(self, is_command: bool, user_entry_list: list[str]):
        """ `+`
        `Type:` Procedure
        `Description:` creates an entire test
        :param:`is_command:` boolean to know if we use a command to execute this function
        :param:`user_entry_list:` information input by the user
        """
            
        # creation of the file that stores the test pieces
        test_folder_path = ManageFolders().create_test_folder(user_entry_list[0])

        if test_folder_path == "":
            if is_command:
                print("[ERREUR] Ce nom existe déjà.")
                return
            else:
                MessageBox("ERREUR Nom de test", "[ERREUR] Ce nom de test existe déjà.").mainloop()
                return

        # creation of test piece files
        new_file = ManageSpecificFiles()
        new_file.create_file(test_folder_path, f"{user_entry_list[0]}_settings.txt", user_entry_list)
        new_file.create_execution_file(test_folder_path, "name.txt", user_entry_list[0])
            
        # creation of the only file that the user can select to run the tests
        new_file.create_file(CONSTANT_TEST_AVAILABLE_FOLDER_PATH, f"{user_entry_list[0]}.txt", [test_folder_path])


    def execute_test(self, database: Database, file_paths_list: list[str]):
        """ `+`
        `Type:` Procedure
        `Description:` execute all the test files in the parameter list
        :param:`database:` object that manages the interaction with the database
        :param:`file_paths_list:` list of file paths that store the paths to the test folders
        """

        # execution of each file in the list
        for i, fil in enumerate(file_paths_list):
            # retrieve the path of the test folder
            test_file = open(fil, 'r')
            test_folder_path = test_file.readlines()[0].rstrip()
            test_file.close()

            # creation of a folder for the test report
            file_name = os.path.basename(test_folder_path)
            folder = TestReportFolder(file_name)

            # creation of test items depending on each test
            manage_files = ManageSpecificFiles()
            test_type, wanted_prg= manage_files.create_temp_test_pieces_file(test_folder_path, i, folder.get_now())

            # launches the general precondition for launching a test
            loaded_prg = Precondition(database).start_precondition()
            time.sleep(6.5)

            # test execution
            start_time = ReadTraceFile(test_folder_path, database, folder.get_folder_name(), loaded_prg, wanted_prg).launch()

            # take a screenshot
            Screenshot().take_screenshot(folder.get_screenshot_folder_path(), "screenshot_report")

            # create report
            ManageReportFile(database, folder.get_folder_path(), test_folder_path, folder.get_now(), start_time.strftime(CONSTANT_SHORT_FORMAT_DATES_DATABASE), i).create_report_file()

            # launches the general postcondition to stop a test
            PostCondition().start_postcondition(database, folder.get_folder_path())

            # deletion of the test pieces
            manage_files.delete_temp_test_pieces_file(test_folder_path, i)


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
        soft.close_soft()
        soft.open_soft()

        time.sleep(6) # we wait until the software is well opened
        MessageBox("Enregistrement", "[INFO] L'enregistrement commence.").mainloop()
        
        # recording of user's actions
        test_piece = InputRecorder(user_entry_list[0], CONSTANT_TEST_PIECES_FOLDER_PATH)

        if test_piece.get_was_file_created():
            test_piece.start_recording()
        else:
            return

        # software closure
        soft.close_soft()