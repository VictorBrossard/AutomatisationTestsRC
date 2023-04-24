# Author        : Victor BROSSARD
# Description   : File that allows the creation or reading of the file that stores the software paths
#                 Useful to avoid giving all the time the paths

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
import subprocess
import os

from PathsInit.PathsInitWithoutPaths import PathsInitWithoutPaths
from PathsInit.PathsInitWithPaths import  PathsInitWithPaths
from FilesManagement.InitFolders import CONSTANT_SETTINGS_FOLDER_PATH  # path where we store the settings file
from FilesManagement.InitFolders import CONSTANT_NAME_SETTINGS_FILE
from FilesManagement.InitFolders import CONSTANT_INIT_PATH

#-----------------------------------------------------------------------------------------------------
# Initialization of constants

#-----------------------------------------------------------------------------------------------------

class InitSettingsFile(object):
    """ `+`
    :class:`PathsFile` manages the file that stores the software paths
    """
    
    def __init__(self):
        """ `-`
        `Type:` Constructor
        """

        # Check if the file exists
        if os.path.exists(CONSTANT_SETTINGS_FOLDER_PATH + '\\' + CONSTANT_NAME_SETTINGS_FILE):
            self.__open_file()
        else:
            self.__create_file()

    
    def __create_file(self):
        """ `-`
        `Type:` Procedure
        `Description:` create the file that stores the paths in case it does not exist and opens the programs thanks to these paths
        """

        # Creation of the file 
        os.chdir(CONSTANT_SETTINGS_FOLDER_PATH) # Change the current working directory by giving the path
        subprocess.run(['type', 'nul', '>', CONSTANT_NAME_SETTINGS_FILE], shell=True)

        # Opening software without knowing the paths (will ask the user for the paths)
        paths_to_store = PathsInitWithoutPaths()

        # Save the paths in the file we have created
        os.chdir(CONSTANT_SETTINGS_FOLDER_PATH)
        file_path = open(CONSTANT_NAME_SETTINGS_FILE, 'w')      # Opening the file in write mode ('w')
        file_path.write("simulat.exe \n")                       # Simulator software name
        file_path.write("rc5.exe \n")                           # RC software name
        file_path.write(paths_to_store.get_simu_path() + "\n")  # Simulator Path
        file_path.write(paths_to_store.get_rc_path() + "\n")    # RC Path
        file_path.write(CONSTANT_INIT_PATH + "\n")              # Init Folder Path
        file_path.write("Menu général \n")                      # RC window name
        file_path.write("tab \n")                               # Key to end test recording
        file_path.close()

    
    def __open_file(self):
        """ `-`
        `Type:` Procedure
        `Description:` allow, if the file exists, to open the programs thanks to the paths in the file
        """

        # Get the path for the simulator which is in the first line of the file
        os.chdir(CONSTANT_SETTINGS_FOLDER_PATH)
        file_path = open(CONSTANT_NAME_SETTINGS_FILE, 'r')  # Opening the file in read mode ('r')
        simu_path = file_path.readlines()[2].rstrip()       # Get the first line of the file
        file_path.close()

        # Get the path for RC which is in the second line of the file
        os.chdir(CONSTANT_SETTINGS_FOLDER_PATH)
        file_path = open(CONSTANT_NAME_SETTINGS_FILE, 'r')
        rc_path = file_path.readlines()[3].rstrip() # rstrip removes the line break which is automatically taken into account with the readlines function
        file_path.close()
    
        # Opening software knowing the paths (no need to ask the user)
        PathsInitWithPaths(simu_path, rc_path)
