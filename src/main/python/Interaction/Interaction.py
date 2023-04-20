# Author        : Victor BROSSARD
# Description   : 

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import pyautogui
import win32gui

from GraphicInterface.UserEntryPopUp import UserEntryPopUp
from Interaction.Screenshot import Screenshot
from Interaction.InputRecorder import InputRecorder
from Interaction.ExecuteTest import ExecuteTest

#-----------------------------------------------------------------------------------------------------
#
class Interaction:

    # Constructor
    def __init__(self):
        pass

    #
    def close_rc(self):
        #
        rc_window_foreground()

        #
        ExecuteTest().read_test_file("close_rc.txt")

    #
    def screenshot(self):
        rc_window_foreground()
        Screenshot()

    def write_test(self):
        #
        pop_up = UserEntryPopUp("Record Tests", "Entrez le nom du test : ")
        pop_up.mainloop()

        InputRecorder(pop_up.get_user_entry()).start_record()

    def execute_test(self, file_name):
        """
        """
        rc_window_foreground()
        ExecuteTest().read_test_file(file_name)

#-----------------------------------------------------------------------------------------------------
#
def rc_window_foreground():
    ###### NOM DE LE FENETRE
    hwnd = win32gui.FindWindow(None, 'Menu Général')

    #### SI LE NOM EST PAS TROUVE ON REDEMANDE LE NOM OR VU QU ON LE STOCK PAS CA FAIT UNE BOUCLE
    try :
        win32gui.SetForegroundWindow(hwnd)
    except Exception:
        uepu = UserEntryPopUp("ERROR WINDOW NAME", "Donnez le nom de la fenêtre de RC : ")
        uepu.mainloop()
        hwnd = uepu.get_user_entry()
        win32gui.SetForegroundWindow(hwnd)