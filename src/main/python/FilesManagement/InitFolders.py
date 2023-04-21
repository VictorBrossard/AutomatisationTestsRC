# Author        : Victor BROSSARD
# Description   : 

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import os

#-----------------------------------------------------------------------------------------------------
# Initialization of constants
CONSTANT_INIT_PATH = "C:\Program Files"

CONSTANT_MAIN_FOLDER_PATH = "C:\Program Files\AutomatisationRC"

CONSTANT_FILES_FOLDER_PATH = "C:\Program Files\AutomatisationRC\Files"

CONSTANT_SCREENSHOTS_FOLDER_PATH = "C:\Program Files\AutomatisationRC\Files\screenshots"
CONSTANT_TESTS_FOLDER_PATH = "C:\Program Files\AutomatisationRC\Files\\tests"               # \\ because \ does not work on its own when there is a t or an n
CONSTANT_SETTINGS_FOLDER_PATH = "C:\Program Files\AutomatisationRC\Files\\settings"

CONSTANT_NAMES_FOLDER_PATH = "C:\Program Files\AutomatisationRC\Files\\settings\\names"
CONSTANT_PATHFILE_FOLDER_PATH = "C:\Program Files\AutomatisationRC\Files\settings\pathFile"

#-----------------------------------------------------------------------------------------------------

class InitFolders(object):
    """ `+`
    :class:`InitFolders` creates all the folders where we will store our files
    """

    def __init__(self):
        """ `-`
        `Type:` Constructor
        """

        self.__create_folder("AutomatisationRC", CONSTANT_INIT_PATH)

        self.__create_folder("Files", CONSTANT_MAIN_FOLDER_PATH)

        self.__create_folder("screenshots", CONSTANT_FILES_FOLDER_PATH)
        self.__create_folder("tests", CONSTANT_FILES_FOLDER_PATH)
        self.__create_folder("settings", CONSTANT_FILES_FOLDER_PATH)

        self.__create_folder("filesNames", CONSTANT_SETTINGS_FOLDER_PATH)
        self.__create_folder("pathFile", CONSTANT_SETTINGS_FOLDER_PATH)

     
    def __create_folder(self, name_folder: str, path: str):
        """ `-`
        `Type:` Procedure
        `Description:` create a folder with its name and path
        :param:`name_folder:` name of the folder to be created
        :param:`path:` path where we create the folder
        """
        
        # Check that the file doesn't exist
        if not os.path.exists(path + "\\" + name_folder):
            os.chdir(path)              # Change the current working directory by giving the path
            os.makedirs(name_folder)    # create the folder
