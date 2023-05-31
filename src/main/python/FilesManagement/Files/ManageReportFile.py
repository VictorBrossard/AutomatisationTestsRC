# Author        : Victor BROSSARD
# Description   : Class that manages the creation of the test report

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
import os

from FilesManagement.Files.ManageAnyFile import ManageAnyFile

from Database.Database import Database

from abc import ABC
from abc import abstractmethod

#-----------------------------------------------------------------------------------------------------

class ManageReportFile(ManageAnyFile, ABC):
    """ `+`
    :class:`ManageReportFile` manages the creation of the test report
    """
    
    def __init__(self, database: Database, report_folder_path: str, test_folder_path: str):
        """ `-`
        `Type:` Constructor
        :param:`database:` object that manages the interaction with the database
        :param:`report_folder_path:` path where you save the file
        :param:`test_folder_path:` path of the test file to be analyzed
        """

        self.data = database
        self.report_folder_path = report_folder_path
        self.test_folder_path = test_folder_path
        
        self.test_name = os.path.basename(report_folder_path) # name of the file which is also the name of the test
        self.content_list = [] # future file content
        self.temp_content_list = []


    @abstractmethod
    def create_report_file_test(self):
        """ `+`
        `Type:` Procedure
        `Description:` creates a txt report file for the test
        """

        pass