# Author        : Victor BROSSARD
# Description   : 

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import pyautogui
import win32gui
import time

from Interface.UserEntryPopUp import UserEntryPopUp

#-----------------------------------------------------------------------------------------------------
#
class Interaction:

    # Constructor
    def __init__(self):
        pass

    #
    def close_rc(self):
        try :
            hwnd = win32gui.FindWindow(None, 'Menu Général')
        except Exception:
            print('je suis là')
            uepu = UserEntryPopUp("ERROR WINDOW NAME", "Donnez le nom de la fenêtre de RC : ")
            uepu.mainloop()
            hwnd = uepu.get_user_entry()
        
        win32gui.SetForegroundWindow(hwnd)
        pyautogui.click(1804, 956)

    #
    def calibration(self):
        print('calibrage')