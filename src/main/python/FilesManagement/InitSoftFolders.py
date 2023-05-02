# Author        : Victor BROSSARD
# Description   : Class that creates all the folders where we will store our files

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import os

#-----------------------------------------------------------------------------------------------------
# Initialization of constants
CONSTANT_INIT_PATH = "C:\Program Files"

CONSTANT_MAIN_FOLDER_PATH = CONSTANT_INIT_PATH + "\AutomatisationRC"

CONSTANT_FILES_FOLDER_PATH = CONSTANT_MAIN_FOLDER_PATH + "\Files"

CONSTANT_SCREENSHOTS_FOLDER_PATH = CONSTANT_FILES_FOLDER_PATH + "\screenshots"
CONSTANT_TESTS_FOLDER_PATH = CONSTANT_FILES_FOLDER_PATH + "\\tests"  # \\ because \ does not work on its own when there is a t or an n
CONSTANT_SETTINGS_FOLDER_PATH = CONSTANT_FILES_FOLDER_PATH + "\\settings"

CONSTANT_REPORTS_FOLDER_PATH = CONSTANT_TESTS_FOLDER_PATH + "\\reports"
CONSTANT_EXCUTABLE_TESTS_FOLDER_PATH = CONSTANT_TESTS_FOLDER_PATH + "\\executable tests"

CONSTANT_NAME_SETTINGS_FILE = 'settings.txt'


#-----------------------------------------------------------------------------------------------------

class InitSoftFolders(object):
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

        self.__create_folder("reports", CONSTANT_TESTS_FOLDER_PATH)
        self.__create_folder("executable tests", CONSTANT_TESTS_FOLDER_PATH)

     
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