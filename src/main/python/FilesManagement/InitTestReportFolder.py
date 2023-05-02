# Author        : Victor BROSSARD
# Description   : class that creates a folder to store the information of the test we just performed

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import os
import datetime

from FilesManagement.InitSoftFolders import CONSTANT_REPORTS_FOLDER_PATH

#-----------------------------------------------------------------------------------------------------

class InitTestReportFolder(object):
    """ `+`
    :class:`InitTestFolder` creates a folder to store the information of the test we just performed
    """

    def __init__(self, name: str):
        """ `-`
        `Type:` Constructor
        """

        self.name = self.__find_folder_name(name)
        self.folder_path = f"{CONSTANT_REPORTS_FOLDER_PATH}\\{self.name}"

        self.__create_folder(self.name, CONSTANT_REPORTS_FOLDER_PATH)
        self.__create_folder("screenshot", self.folder_path)
        self.__create_folder("traces", self.folder_path)
        self.__create_folder("database", self.folder_path)


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


    def __find_folder_name(self, test_name: str) -> str:
        """ `-`
        `Type:` Function
        `Description:` creates a folder to store the information from the test we just performed 
        :param:`test_name:` name of the test we have just performed
        `Return:` a new name
        """

        now = datetime.datetime.now().strftime("%Hh%Mm%Ss")
        new_name = f"{test_name}_{now}"
        return new_name
    

    def get_folder_name(self):
        """ `+`
        `Type:` Function
        `Description:` getter that returns the variable name
        `Return:` name
        """

        return self.name
    

    def get_folder_path(self):
        """ `+`
        `Type:` Function
        `Description:` getter that returns the variable folder_path
        `Return:` folder_path
        """

        return self.folder_path
