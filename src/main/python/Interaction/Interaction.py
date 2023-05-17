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

from FilesManagement.Folders.ManageFolders import CONSTANT_TEST_PIECES_FOLDER_PATH
from FilesManagement.Folders.ManageFolders import CONSTANT_TEST_AVAILABLE_FOLDER_PATH
from FilesManagement.Folders.TestReportFolder import TestReportFolder
from FilesManagement.Folders.ManageFolders import ManageFolders

from FilesManagement.Files.ManipulationSettingsFile import ManipulationSettingsFile
from FilesManagement.Files.ManageSpecificFiles import ManageSpecificFiles
from FilesManagement.Files.ManageReportFile import ManageReportFile

from RCTest.Precondition import Precondition
from RCTest.PostCondition import PostCondition
from RCTest.ReadTraceFile import ReadTraceFile

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


    def create_test(self):
        """ `+`
        `Type:` Procedure
        `Description:` creates an entire test
        """

        prg_list = self.__get_program_list()

        # pop-up asking for the name of the file we are going to create to save the test
        pop_up = UserEntryPopUp(
            "Create Tests", 
            ["Entrez le nom du test :", "Nombre de cartes à produire :", "Initialisation de la machine :", "Programme :"], 
            [3, 1, 2, 2], 
            [["Complète", "Partielle"], prg_list]
        )
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
        new_file.create_execution_file(test_folder_path, "program_name.txt", user_entry_list[3])
            
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

            # launches the general precondition for launching a test
            prg = Precondition(database).start_precondition()
            time.sleep(6.5)

            start_time = ReadTraceFile(fil, database, folder.get_folder_name(), folder.get_now(), prg).launch()

            # take a screenshot
            Screenshot().take_screenshot(folder.get_screenshot_folder_path(), "screenshot_report")

            # create report
            ManageReportFile(database, folder.get_folder_path(), fil, folder.get_now(), start_time.strftime('%Y-%m-%d %H:%M:%S')).create_report_file()

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
    

    def __get_program_list(self):
        """ `-`
        `Type:` Function
        `Description:` will fetch the list of programs locally
        `Return:` list of programs
        """

        # path of the folder where the programs are
        folder_path = self.line_settings_file.get_line(8)
        files_with_dp_extension = []

        # recovery of the list of program names 
        for file_name_with_extension in os.listdir(folder_path):
            if file_name_with_extension.endswith(".dp"):
                file_name, extension = os.path.splitext(os.path.basename(file_name_with_extension))
                files_with_dp_extension.append(file_name)

        return files_with_dp_extension