# Author        : Victor BROSSARD
# Description   : Object that opens simulator and RC

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
import subprocess
import os
import tkinter.messagebox
import sys

from GraphicInterface.UserEntryPopUp import UserEntryPopUp
from FilesManagement.InitFolders import CONSTANT_PATHFILE_FOLDER_PATH

#-----------------------------------------------------------------------------------------------------

class _PathsInit(object):
    """ `#`
    :class:`PathsInit` uses software paths to open them
    """

    def __init__(self):
        """ `-`
        `Type:` Constructor
        """

        # Initializes object variables
        self.simu_path = ""
        self.rc_path = ""
        

    def _simu_init(self) -> str:
        """ `#`
        `Type:` Fonction
        `Description:` asks the user for the path to access the simulator
        `Return:` Simulator path
        """

        # Opening the pop-up that asks the user for the path
        simu_pop_up = UserEntryPopUp("Simulator Path", "Enter the path to access the simulator : ")
        simu_pop_up.mainloop()

        # Returns the path given by the user
        return simu_pop_up.get_user_entry()
    
    
    def _rc_init(self) -> str:
        """ `#`
        `Type:` Function
        `Description:` asks the user for the path to access RC
        `Return:` RC path
        """

        # Opening the pop-up that asks the user for the path
        rc_pop_up = UserEntryPopUp("RC Path", "Enter the path to access RC : ")
        rc_pop_up.mainloop()

        # Returns the path given by the user
        return rc_pop_up.get_user_entry()
    

    def _start_simu(self):
        """ `#`
        `Type:` Procedure
        `Description:` open the simulator
        """

        try:
            # Opening the software 
            os.chdir(self.simu_path)                                    # Change the current working directory by giving the path
            subprocess.run(['start', 'simulat.exe'], shell=True)        # Open the software using the start command
        except Exception as e:
            tkinter.messagebox.showinfo('Simulator Path ERROR',e)    # Displaying the error message for the user
            os.chdir(CONSTANT_PATHFILE_FOLDER_PATH)
            os.remove('pathFile.txt')                                   # Delete the file that stores the paths because the path is wrong so we don't need to store it

            # End the program
            sys.exit()
            
    
    def _start_rc(self):
        """ `#`
        `Type:` Procedure
        `Description:` open RC
        """

        try:
            # Opening the software
            os.chdir(self.rc_path)                              # Change the current working directory by giving the path
            subprocess.run(['start', 'rc5.exe'], shell=True)    # Open the software using the start command
        except Exception as e:
            tkinter.messagebox.showinfo('RC Path ERROR',e)    # Displaying the error message for the user
            os.chdir(CONSTANT_PATHFILE_FOLDER_PATH)
            os.remove('pathFile.txt')                           # Delete the file that stores the paths because the path is wrong so we don't need to store it
            
            # End the program
            sys.exit()

    
    def get_simu_path(self) -> str:
        """ `+`
        `Type:` Function
        `Description:` getter that returns the variable simu_path
        `Return:` simu_path
        """

        return self.simu_path
    

    def get_rc_path(self) -> str:
        """ `+`
        `Type:` Function
        `Description:` getter that returns the variable rc_path
        `Return:` rc_path
        """

        return self.rc_path