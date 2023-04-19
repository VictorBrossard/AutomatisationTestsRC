# Author        : Victor BROSSARD
# Description   : Object that opens simulator and RC

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
import subprocess
import os
import tkinter.messagebox
import sys

from GraphicInterface.UserEntryPopUp import UserEntryPopUp

#-----------------------------------------------------------------------------------------------------
# Class that uses software paths to open them
class PathsInit(object):

    # Constructor
    def __init__(self):
        # Initializes object variables
        self.simu_path = ""
        self.rc_path = ""
        
    # Function that asks the user for the path to access the simulator
    def simu_init(self):
        # Opening the pop-up that asks the user for the path
        simu_pop_up = UserEntryPopUp("Chemin Simulateur", "Entrez le chemin pour accéder au simulateur : ")
        simu_pop_up.mainloop()

        # Returns the path given by the user
        return simu_pop_up.get_user_entry()
    
    # Function that asks the user for the path to access RC
    def rc_init(self):
        # Opening the pop-up that asks the user for the path
        rc_pop_up = UserEntryPopUp("Chemin RC", "Entrez le chemin pour accéder à RC : ")
        rc_pop_up.mainloop()

        # Returns the path given by the user
        return rc_pop_up.get_user_entry()
    
    # Function that opens the simulator
    def start_simu(self):
        try:
            # Opening the software 
            os.chdir(self.simu_path)                                    # Change the current working directory by giving the path
            subprocess.run(['start', 'simulat.exe'], shell=True)        # Open the software using the start command
        except Exception as e:
            tkinter.messagebox.showinfo('ERROR chemin Simulateur',e)    # Displaying the error message for the user
            os.chdir(os.getcwd())
            os.remove('pathFile.txt')                                   # Delete the file that stores the paths because the path is wrong so we don't need to store it

            # End the program
            sys.exit()
            

    # Function that opens RC
    def start_rc(self):
        try:
            # Opening the software
            os.chdir(self.rc_path)                              # Change the current working directory by giving the path
            subprocess.run(['start', 'rc5.exe'], shell=True)    # Open the software using the start command
        except Exception as e:
            tkinter.messagebox.showinfo('ERROR chemin RC',e)    # Displaying the error message for the user
            os.chdir(os.getcwd())
            os.remove('pathFile.txt')                           # Delete the file that stores the paths because the path is wrong so we don't need to store it
            
            # End the program
            sys.exit()

    # Function that returns the variable simu_path
    def get_simu_path(self):
        return self.simu_path
    
    # Function that returns the variable rc_path
    def get_rc_path(self):
        return self.rc_path