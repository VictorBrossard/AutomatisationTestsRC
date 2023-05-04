# Author        : Victor BROSSARD
# Description   : Object that does the interactions instead of the user

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import win32gui
import tkinter.messagebox
import os
import time

from GraphicInterface.UserEntryPopUp import UserEntryPopUp
from GraphicInterface.SettingsInterface import SettingsInterface
from GraphicInterface.SimpleQuestionInterface import SimpleQuestionInterface

from Interaction.Screenshot import Screenshot
from Interaction.ExecuteTest import ExecuteTest
from Interaction.InputRecorder import InputRecorder

from FilesManagement.ManipulationSettingsFile import ManipulationSettingsFile
from FilesManagement.InitFolder import CONSTANT_TEST_PIECES_FOLDER_PATH
from FilesManagement.InitFolder import CONSTANT_TEST_AVAILABLE_FOLDER_PATH
from FilesManagement.InitTestReportFolder import InitTestReportFolder
from FilesManagement.InitFolder import InitFolder
from FilesManagement.InitFile import InitFile

from RCTest.Precondition import Precondition
from RCTest.PostCondition import PostCondition
from RCTest.ManageSoftwares import ManageSoftwares

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

    
    def close_rc(self):
        """ `+`
        `Type:` Procedure
        `Description:` performs the action of closing RC
        """

        rc_window_foreground(self.rc_window_name)
        ExecuteTest().read_test_file("close_rc.txt")

    
    def screenshot(self):
        """ `+`
        `Type:` Procedure
        `Description:` take a screenshot
        """

        rc_window_foreground(self.rc_window_name)
        Screenshot()


    def create_test(self):
        """ `+`
        `Type:` Procedure
        `Description:` creates an entire test
        """

        # pop-up asking for the name of the file we are going to create to save the test
        pop_up = UserEntryPopUp("Create Tests", ["Entrez le nom du test :", "Nombre de cartes à produire :"], [0, 1])
        pop_up.mainloop()

        user_entry_list = pop_up.get_user_entries()

        for entries in user_entry_list:
            if entries == "":
                tkinter.messagebox.showinfo('Missing Information ERROR', "Vous n'avez pas remplis toutes les cases.")
                return
            
        test_folder_path = InitFolder().create_test_folder(user_entry_list[0])

        if test_folder_path == "":
            tkinter.messagebox.showinfo('Test Name ERROR', 'Ce nom de test existe déjà.')
            return
        
        soft = ManageSoftwares()
        soft.open_soft()

        new_file = InitFile()
        new_file.create_file(test_folder_path, f"{user_entry_list[0]}_settings.txt", user_entry_list)
        time.sleep(6)

        before_production = SimpleQuestionInterface("Avant production", "Avez-vous des choses à faire avant la production ?")
        before_production.mainloop()

        if before_production.get_is_yes():
            precondition = InputRecorder("precondition", test_folder_path)

            if precondition.get_was_file_created():
                precondition.start_recording()
            else:
                return
            
        new_file.create_file(CONSTANT_TEST_AVAILABLE_FOLDER_PATH, f"{user_entry_list[0]}.txt", [test_folder_path])
            
        soft.close_soft()


    def settings(self):
        """ `+`
        `Type:` Procedure
        `Description:` launch the settings interface
        """

        SettingsInterface().mainloop()


    def execute_test(self, file_paths_list: list):
        """ `+`
        `Type:` Procedure
        `Description:` execute all the test files in the parameter list
        :param:`file_paths_list:` list of file paths to run
        """

        for file in file_paths_list:
            """# We separate the name of the file and its path to be able to handle it better later
            file_path_without_name = os.path.dirname(file)
            file_name = os.path.basename(file)

            # checking if the file is in the right folder otherwise it is not a test
            if os.path.abspath(file_path_without_name) == os.path.abspath(CONSTANT_TESTS_FOLDER_PATH):
                ExecuteTest().read_test_file(file_name)
                time.sleep(2)"""
            
            all_test_file = self.__get_all_test_file(file)

            if all_test_file == []:
                return

            Precondition().start_precondition()
            folder = InitTestReportFolder("test")
            time.sleep(6)

            for small_test in all_test_file:
                print(small_test)
                ExecuteTest().read_test_file(small_test)
                time.sleep(1)

            PostCondition().start_postcondition(folder.get_folder_path())
            time.sleep(1)


    def test_pieces(self):
        """ `+`
        `Type:` Procedure
        `Description:`
        """

        soft = ManageSoftwares()
        soft.open_soft()

        time.sleep(5)
        pop_up = UserEntryPopUp("Create Test Pieces", ["Entrez le nom du test :"], [0])
        pop_up.mainloop()

        user_entry_list = pop_up.get_user_entries()

        for entries in user_entry_list:
            if entries == "":
                tkinter.messagebox.showinfo('Missing Information ERROR', "Vous n'avez pas remplis toutes les cases.")
                soft.close_soft()
                return
        
        precondition = InputRecorder(user_entry_list[0], CONSTANT_TEST_PIECES_FOLDER_PATH)

        if precondition.get_was_file_created():
            precondition.start_recording()
        else:
            return

        soft.close_soft()


    def __get_all_test_file(self, file_with_path: str) -> list:
        """
        """

        file_list = []

        try:
            fil = open(file_with_path, 'r')
            path_line = fil.readlines()[0].rstrip()
            fil.close()
        except Exception:
            tkinter.messagebox.showinfo("File ERROR", "L'un des fichiers sélectionnés est corrompus.")
            return []

        precond_path = f"{path_line}\\precondition.txt"
        if os.path.exists(precond_path):
            file_list.append(precond_path)

        file_list.append(f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\partial_prod.txt") ######################## A CHANGER

        postcond_path = f"{path_line}\\postcondition.txt"
        if os.path.exists(postcond_path):
            file_list.append(postcond_path)

        return file_list

#-----------------------------------------------------------------------------------------------------

def rc_window_foreground(window_name: str):
    """ `+`
    `Type:` Procedure
    `Description:` puts the RC window in the foreground to be sure that we are handling the right software
    :param:`window_name:` RC window name
    """

    # window to search
    hwnd = win32gui.FindWindow(None, window_name)

    try :
        win32gui.SetForegroundWindow(hwnd) # Bringing RC to the fore
    except Exception as e:
        tkinter.messagebox.showinfo('RC Window Name ERROR', e)  # Displaying the error message for the user
        settings = SettingsInterface()
        settings.mainloop()
        rc_window_foreground(ManipulationSettingsFile().get_line(4))
        