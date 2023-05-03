# Author        : Victor BROSSARD
# Description   : Class that allows you to create any type of file

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
CONSTANT_TEST_PIECES_FOLDER_PATH = CONSTANT_TESTS_FOLDER_PATH + "\\test pieces"
CONSTANT_TEST_AVAILABLE_FOLDER_PATH = CONSTANT_TESTS_FOLDER_PATH + "\\test available"

#-----------------------------------------------------------------------------------------------------

class InitFolder(object):
    """ `+`
    :class:`InitFolder` allows you to create any type of file
    """

    def __init__(self):
        """ `-`
        `Type:` Constructor
        """

        pass


    def _create_folder(self, name_folder: str, path: str) -> str:
        """ `#`
        `Type:` Function
        `Description:` create a folder with its name and path
        :param:`name_folder:` name of the folder to be created
        :param:`path:` path where we create the folder
        `Return:` the path of the folder if it has been created
        """
        
        full_path = f"{path}\\{name_folder}"

        # Check that the file doesn't exist
        if not os.path.exists(full_path):
            os.chdir(path)              # Change the current working directory by giving the path
            os.makedirs(name_folder)    # Create the folder
            return full_path
        else:
            return ""


    def create_test_folder(self, name: str) -> str:
        """ `+`
        `Type:` Function
        `Description:` creates a folder to store all test information
        :param:`name:` test name
        `Return:` test folder path
        """

        return self._create_folder(name, CONSTANT_EXCUTABLE_TESTS_FOLDER_PATH)

