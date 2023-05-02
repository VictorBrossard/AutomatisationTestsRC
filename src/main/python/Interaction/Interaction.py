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

from Interaction.Screenshot import Screenshot
from Interaction.InputRecorder import InputRecorder
from Interaction.ExecuteTest import ExecuteTest

from FilesManagement.ManipulationSettingsFile import ManipulationSettingsFile
from FilesManagement.InitSoftFolders import CONSTANT_TESTS_FOLDER_PATH

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


    def write_test(self):
        """ `+`
        `Type:` Procedure
        `Description:` initiates the action of recording user actions
        """

        # pop-up asking for the name of the file we are going to create to save the test
        pop_up = UserEntryPopUp("Record Tests", "Entrez le nom du test : ")
        pop_up.mainloop()

        recorder = InputRecorder(pop_up.get_user_entry())

        if recorder.get_was_file_created():
            recorder.start_recording()


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
        
        rc_window_foreground(self.rc_window_name)

        for file in file_paths_list:
            # We separate the name of the file and its path to be able to handle it better later
            file_path_without_name = os.path.dirname(file)
            file_name = os.path.basename(file)

            # checking if the file is in the right folder otherwise it is not a test
            if os.path.abspath(file_path_without_name) == os.path.abspath(CONSTANT_TESTS_FOLDER_PATH):
                ExecuteTest().read_test_file(file_name)
                time.sleep(2)

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
        