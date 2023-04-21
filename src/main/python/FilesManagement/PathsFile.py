# Author        : Victor BROSSARD
# Description   : File that allows the creation or reading of the file that stores the software paths
#                 Useful to avoid giving all the time the paths

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
import subprocess
import os

from PathsInit.PathsInitWithoutPaths import PathsInitWithoutPaths
from PathsInit.PathsInitWithPaths import  PathsInitWithPaths
from FilesManagement.InitFolders import CONSTANT_PATHFILE_FOLDER_PATH  # path where we store the file pathfile

#-----------------------------------------------------------------------------------------------------
# Initialization of constants
CONSTANT_NAME_PATH_FILE = 'pathFile.txt'

#-----------------------------------------------------------------------------------------------------

class PathsFile(object):
    """ `+`
    :class:`PathsFile` manages the file that stores the software paths
    """
    
    def __init__(self):
        """ `-`
        `Type:` Constructor
        """

        # Check if the file exists
        if os.path.exists(CONSTANT_PATHFILE_FOLDER_PATH + '\\' + CONSTANT_NAME_PATH_FILE):
            self.__open_paths_file()
        else:
            self.__create_paths_file()

    
    def __create_paths_file(self):
        """ `-`
        `Type:` Procedure
        `Description:` create the file that stores the paths in case it does not exist and opens the programs thanks to these paths
        """

        # Creation of the file 
        os.chdir(CONSTANT_PATHFILE_FOLDER_PATH) # Change the current working directory by giving the path
        subprocess.run(['type', 'nul', '>', CONSTANT_NAME_PATH_FILE], shell=True)

        # Opening software without knowing the paths (will ask the user for the paths)
        paths_to_store = PathsInitWithoutPaths()

        # Save the paths in the file we have created
        os.chdir(CONSTANT_PATHFILE_FOLDER_PATH)
        file_path = open(CONSTANT_NAME_PATH_FILE, 'w') # Opening the file in write mode ('w')
        file_path.write(paths_to_store.get_simu_path() + "\n" + paths_to_store.get_rc_path())
        file_path.close()

    
    def __open_paths_file(self):
        """ `-`
        `Type:` Procedure
        `Description:` allow, if the file exists, to open the programs thanks to the paths in the file
        """

        # Get the path for the simulator which is in the first line of the file
        os.chdir(CONSTANT_PATHFILE_FOLDER_PATH)
        file_path = open(CONSTANT_NAME_PATH_FILE, 'r')  # Opening the file in read mode ('r')
        simu_path = file_path.readlines()[0].rstrip()   # Get the first line of the file
        file_path.close()

        # Get the path for RC which is in the second line of the file
        os.chdir(CONSTANT_PATHFILE_FOLDER_PATH)
        file_path = open(CONSTANT_NAME_PATH_FILE, 'r')
        rc_path = file_path.readlines()[1].rstrip() # rstrip removes the line break which is automatically taken into account with the readlines function
        file_path.close()
    
        # Opening software knowing the paths (no need to ask the user)
        PathsInitWithPaths(simu_path, rc_path)
