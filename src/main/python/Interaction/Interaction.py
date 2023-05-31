# Author        : Victor BROSSARD
# Description   : Object that does the interactions instead of the user

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import os
import time
import win32gui

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
from Useful.AllConstant import CONSTANT_SHORT_FORMAT_DATES_DATABASE
from Useful.AllConstant import CONSTANT_RC_WINDOW_NAME
from Useful.AllConstant import CONSTANT_TEST_NAME

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


    def execute_test(self, test_type: str, database: Database, file_paths_list: list[str]):
        """ `+`
        `Type:` Procedure
        `Description:` execute production test
        :param:`test_type:` type of the test
        :param:`database:` object that manages the interaction with the database
        :param:`file_paths_list:` list of file paths that store the paths to the test folders
        """

        if test_type == CONSTANT_TEST_NAME[0]:
            self.__execute_prod_test(database, file_paths_list)


    def __execute_prod_test(self, database: Database, file_paths_list: list[str]):
        """ `-`
        `Type:` Procedure
        `Description:` execute all the production test files in the parameter list
        :param:`test_type:` type of the test
        :param:`database:` object that manages the interaction with the database
        :param:`file_paths_list:` list of file paths that store the paths to the test folders
        """

        if file_paths_list == []:
            return

        # execution of each file in the list
        for i, fil in enumerate(file_paths_list):
            # creation of a folder for the test report
            file_name = os.path.basename(fil)
            folder = TestReportFolder(file_name)

            # creation of test items depending on each test
            manage_files = ManageSpecificFiles()
            wanted_prg = manage_files.create_temp_test_pieces_file(fil, i, folder.get_now())

            # launches the general precondition for launching a test
            loaded_prg = Precondition(database).start_precondition_prod_test()
            time.sleep(6)
            self.__rc_window_foreground(CONSTANT_RC_WINDOW_NAME)
            time.sleep(1)

            # test execution
            trace_file = ReadTraceFile(fil, database, folder.get_folder_name(), loaded_prg, wanted_prg)
            start_time = trace_file.launch_prod_test()

            if start_time is not None:
                # take a screenshot
                Screenshot().take_screenshot(folder.get_screenshot_folder_path(), "screenshot_report")

                # create report
                ManageReportFile(
                    database, 
                    folder.get_folder_path(), 
                    fil
                ).create_report_file_prod_test(folder.get_now(), start_time.strftime(CONSTANT_SHORT_FORMAT_DATES_DATABASE))

            # launches the general postcondition to stop a test
            PostCondition(database).start_postcondition_prod_test(folder.get_folder_path(), trace_file)


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

        if user_entry_list == []:
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
        self.__rc_window_foreground(CONSTANT_RC_WINDOW_NAME)
        MessageBox("Enregistrement", "[INFO] L'enregistrement commence.").mainloop()
        
        # recording of user's actions
        test_piece = InputRecorder(user_entry_list[0], CONSTANT_TEST_PIECES_FOLDER_PATH)

        if test_piece.get_was_file_created():
            test_piece.start_recording()
        else:
            return

        # software closure
        soft.close_soft()


    def __rc_window_foreground(self, window_name: str):
        """ `+`
        `Type:` Procedure
        `Description:` puts the RC window in the foreground to be sure that we are handling the right software
        :param:`window_name:` RC window name
        """

        # window to search
        hwnd = win32gui.FindWindow(None, window_name)

        try :
            win32gui.SetForegroundWindow(hwnd)  # Bringing RC to the fore
        except Exception as e:
            print(f"[ERREUR] {e}")              # Displaying the error message for the user