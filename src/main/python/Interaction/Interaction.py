# Author        : Victor BROSSARD
# Description   : 

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import pyautogui
import win32gui

from GraphicInterface.UserEntryPopUp import UserEntryPopUp
from Interaction.Screenshot import Screenshot

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
        pyautogui.click(1804, 956)

    #
    def screenshot(self):
        rc_window_foreground()
        Screenshot()

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