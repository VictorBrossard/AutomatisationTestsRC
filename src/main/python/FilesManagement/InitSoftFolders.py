# Author        : Victor BROSSARD
# Description   : Class that creates all the folders where we will store our files

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
from FilesManagement.InitFolder import InitFolder
from FilesManagement.InitFolder import CONSTANT_INIT_PATH
from FilesManagement.InitFolder import CONSTANT_MAIN_FOLDER_PATH
from FilesManagement.InitFolder import CONSTANT_FILES_FOLDER_PATH
from FilesManagement.InitFolder import CONSTANT_TESTS_FOLDER_PATH

#-----------------------------------------------------------------------------------------------------

class InitSoftFolders(InitFolder):
    """ `+`
    :class:`InitFolders` creates all the folders where we will store our files
    """

    def __init__(self):
        """ `-`
        `Type:` Constructor
        """

        self.main = self._create_folder("AutomatisationRC", CONSTANT_INIT_PATH)

        self.files = self._create_folder("Files", CONSTANT_MAIN_FOLDER_PATH)

        self.screenshot = self._create_folder("screenshots", CONSTANT_FILES_FOLDER_PATH)
        self.tests = self._create_folder("tests", CONSTANT_FILES_FOLDER_PATH)
        self.settings = self._create_folder("settings", CONSTANT_FILES_FOLDER_PATH)

        self.reports = self._create_folder("reports", CONSTANT_TESTS_FOLDER_PATH)
        self.ex_tests = self._create_folder("executable tests", CONSTANT_TESTS_FOLDER_PATH)

    
    def get_main_folder_path(self):
        """ `+`
        `Type:` Function
        `Description:` getter that returns the variable main
        `Return:` main
        """

        return self.main
    

    def get_files_folder_path(self):
        """ `+`
        `Type:` Function
        `Description:` getter that returns the variable files
        `Return:` files
        """

        return self.files
    

    def get_screenshot_folder_path(self):
        """ `+`
        `Type:` Function
        `Description:` getter that returns the variable screenshot
        `Return:` screenshot
        """

        return self.screenshot
    

    def get_tests_folder_path(self):
        """ `+`
        `Type:` Function
        `Description:` getter that returns the variable tests
        `Return:` tests
        """

        return self.tests
    

    def get_settings_folder_path(self):
        """ `+`
        `Type:` Function
        `Description:` getter that returns the variable settings
        `Return:` settings
        """

        return self.settings
    

    def get_reports_folder_path(self):
        """ `+`
        `Type:` Function
        `Description:` getter that returns the variable reports
        `Return:` reports
        """

        return self.reports
    

    def get_ex_tests_folder_path(self):
        """ `+`
        `Type:` Function
        `Description:` getter that returns the variable ex_tests
        `Return:` ex_tests
        """

        return self.ex_tests