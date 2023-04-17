# Author        : Victor BROSSARD
# Description   : Ouvre simulateur et RC

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
import PathPopUp
import subprocess
import os
import tkinter.messagebox
import sys

from PathPopUp import PathPopUp

#-----------------------------------------------------------------------------------------------------
# Class that uses software paths to open them
class Init(object):

    # Constructor
    def __init__(self):
        # Initializes object variables
        self.simu_path = ""
        self.rc_path = ""
        
    # Function that asks the user for the path to access the simulator
    def simu_init(self):
        # Opening the pop-up that asks the user for the path
        simu_pop_up = PathPopUp("Simulateur")
        simu_pop_up.mainloop()

        # Returns the path given by the user
        return simu_pop_up.get_path()
    
    # Function that asks the user for the path to access RC
    def rc_init(self):
        # Opening the pop-up that asks the user for the path
        rc_pop_up = PathPopUp("RC")
        rc_pop_up.mainloop()

        # Returns the path given by the user
        return rc_pop_up.get_path()
    
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

#-----------------------------------------------------------------------------------------------------   
# Child class of Init which knows the paths of the software
class InitWhithPaths(Init):

    # Constructor
    def __init__(self, simu_way, rc_way):
        # Parent constuctor
        Init.__init__(self)

        # Initializes object variables
        self.simu_path = simu_way
        self.rc_path = rc_way
        
        # Open software
        self.start_simu()
        self.start_rc()

#-----------------------------------------------------------------------------------------------------
# Child class of Init which does not know the paths of the software so we will ask the user for them
class InitWithoutPaths(Init):

    # Constructor
    def __init__(self):
        # Parent constuctor
        Init.__init__(self)

        # Initializes object variables
        self.simu_path = self.simu_init()
        self.rc_path = self.rc_init()
        
        # Open software
        self.start_simu()
        self.start_rc()