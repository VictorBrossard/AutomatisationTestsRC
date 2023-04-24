# Author        : Victor BROSSARD
# Description   : Object that does the interactions instead of the user

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import win32gui

from GraphicInterface.UserEntryPopUp import UserEntryPopUp
from GraphicInterface.SettingsInterface import SettingsInterface
from Interaction.Screenshot import Screenshot
from Interaction.InputRecorder import InputRecorder
from Interaction.ExecuteTest import ExecuteTest

#-----------------------------------------------------------------------------------------------------
#
class Interaction(object):
    """ `+`
    :class:`Interaction` does the interactions instead of the user
    """

    def __init__(self):
        """ `-`
        `Type:` Constructor
        """

        pass

    
    def close_rc(self):
        """ `+`
        `Type:` Procedure
        `Description:` performs the action of closing RC
        """

        rc_window_foreground()
        ExecuteTest().read_test_file("close_rc.txt")

    
    def screenshot(self):
        """ `+`
        `Type:` Procedure
        `Description:` take a screenshot
        """

        rc_window_foreground()
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


    def execute_test(self, file_name: str):
        """ `+`
        `Type:` Procedure
        `Description:` run the test file file_name
        :param:`file_name:` name of file to execute
        """

        rc_window_foreground()
        ExecuteTest().read_test_file(file_name)


    def settings(self):
        """ `+`
        `Type:` Procedure
        `Description:` launches the settings interface
        """

        settings_interface = SettingsInterface()
        settings_interface.mainloop()

#-----------------------------------------------------------------------------------------------------

def rc_window_foreground():
    """ `+`
    `Type:` Procedure
    `Description:` puts the RC window in the foreground to be sure that we are handling the right software
    """

    # window to search
    hwnd = win32gui.FindWindow(None, 'Menu Général')

    #### PROBLEME
    #### SI LE NOM EST PAS TROUVE ON REDEMANDE LE NOM OR VU QU ON LE STOCK PAS CA FAIT UNE BOUCLE
    try :
        win32gui.SetForegroundWindow(hwnd)
    except Exception:
        uepu = UserEntryPopUp("ERROR WINDOW NAME", "Donnez le nom de la fenêtre de RC : ")
        uepu.mainloop()
        hwnd = uepu.get_user_entry()
        win32gui.SetForegroundWindow(hwnd)