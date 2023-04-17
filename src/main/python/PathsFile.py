# Author        : Victor BROSSARD
# Description   : File that allows the creation or reading of the file that stores the software paths
#                 Useful to avoid giving all the time the paths

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
import subprocess
import os

from Init import InitWhithPaths, InitWithoutPaths
from MainInterface import MainInterface

#-----------------------------------------------------------------------------------------------------
# Initialization of constants
CONSTANT_NAME_FILE = 'pathFile.txt'
CONSTANT_PATH_FILE_STORE_PATHS = os.getcwd() # File directory

#-----------------------------------------------------------------------------------------------------
# Class that manages the file that stores the software paths
class PathsFile(object):

    # Constructor
    def __init__(self):
        # Check if the file exists
        if os.path.exists(CONSTANT_PATH_FILE_STORE_PATHS + '/' + CONSTANT_NAME_FILE):
            self.open_paths_file()
        else:
            self.create_paths_file()

    # Function that creates the file that stores the paths in case it does not exist and opens the programs thanks to these paths
    def create_paths_file(self):
        # Creation of the file in the current directory 
        os.chdir(CONSTANT_PATH_FILE_STORE_PATHS) # Change the current working directory by giving the path
        subprocess.run(['type', 'nul', '>', CONSTANT_NAME_FILE], shell=True)

        # Opening software without knowing the paths (will ask the user for the paths)
        paths_to_store = InitWithoutPaths()

        # Save the paths in the file we have created
        os.chdir(CONSTANT_PATH_FILE_STORE_PATHS)
        path_file = open(CONSTANT_NAME_FILE, 'w') # Opening the file in write mode ('w')
        path_file.write(paths_to_store.get_simu_path() + "\n" + paths_to_store.get_rc_path())
        path_file.close()

    # Function that allows, if the file exists, to open the programs thanks to the paths in the file 
    def open_paths_file(self):
        # Get the path for the simulator which is in the first line of the file
        os.chdir(CONSTANT_PATH_FILE_STORE_PATHS)
        path_file = open(CONSTANT_NAME_FILE, 'r')       # Opening the file in read mode ('r')
        simu_path = path_file.readlines()[0].rstrip()   # Get the first line of the file
        path_file.close()

        # Get the path for RC which is in the second line of the file
        os.chdir(CONSTANT_PATH_FILE_STORE_PATHS)
        path_file = open(CONSTANT_NAME_FILE, 'r')
        rc_path = path_file.readlines()[1].rstrip() # rstrip removes the line break which is automatically taken into account with the readlines function
        path_file.close()
    
        # Opening software knowing the paths (no need to ask the user)
        InitWhithPaths(simu_path, rc_path)
