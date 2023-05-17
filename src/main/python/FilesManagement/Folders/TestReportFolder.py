# Author        : Victor BROSSARD
# Description   : class that creates a folder to store the information of the test we just performed

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import datetime

from FilesManagement.Folders.ManageFolders import ManageFolders

from Useful.AllConstant import CONSTANT_REPORTS_FOLDER_PATH

#-----------------------------------------------------------------------------------------------------

class TestReportFolder(ManageFolders):
    """ `+`
    :class:`InitTestFolder` creates a folder to store the information of the test we just performed
    """

    def __init__(self, name: str):
        """ `-`
        `Type:` Constructor
        """

        super().__init__()

        self.now = ""

        self.name = self.__find_folder_name(name)
        self.folder_path = f"{CONSTANT_REPORTS_FOLDER_PATH}\\{self.name}"

        self.main = self._create_folder(self.name, CONSTANT_REPORTS_FOLDER_PATH)
        self.screenshot = self._create_folder("screenshot", self.folder_path)
        self.database = self._create_folder("database", self.folder_path)


    def __find_folder_name(self, test_name: str) -> str:
        """ `-`
        `Type:` Function
        `Description:` creates a folder to store the information from the test we just performed 
        :param:`test_name:` name of the test we have just performed
        `Return:` a new name
        """

        self.now = datetime.datetime.now().strftime("%Y-%m-%d_%Hh%Mm%Ss")
        new_name = f"{test_name}_{self.now}"
        return new_name
    

    def get_folder_name(self) -> str:
        """ `+`
        `Type:` Function
        `Description:` getter that returns the variable name
        `Return:` name
        """

        return self.name
    

    def get_folder_path(self) -> str:
        """ `+`
        `Type:` Function
        `Description:` getter that returns the variable folder_path
        `Return:` folder_path
        """

        return self.folder_path
    

    def get_screenshot_folder_path(self) -> str:
        """ `+`
        `Type:` Function
        `Description:` getter that returns the variable screenshot
        `Return:` screenshot
        """

        return self.screenshot
    

    def get_database_folder_path(self) -> str:
        """ `+`
        `Type:` Function
        `Description:` getter that returns the variable database
        `Return:` database
        """

        return self.database
    

    def get_now(self) -> str:
        """ `+`
        `Type:` Function
        `Description:` getter that returns the variable now
        `Return:` now
        """

        return self.now
