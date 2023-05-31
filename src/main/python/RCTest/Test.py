# Author        : Victor BROSSARD
# Description   : class that manages the running of a test

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import time

from Interaction.ExecuteTestFile import ExecuteTestFile

from Database.Database import Database

from Interaction.ReadTraceFile import ReadTraceFile

from abc import ABC
from abc import abstractmethod

#-----------------------------------------------------------------------------------------------------

class Test(ABC):
    """ `+`
    :class:`Test` manages the running of a test
    """

    def __init__(self, test_folder_path: str, database: Database, folder_name: str):
        """ `-`
        `Type:` Constructor
        :param:`test_folder_path:` test folder path
        :param:`database:` object that manages the interaction with the database
        :param:`folder_name:` name of the folder which is equivalent to the name of the test in the database
        """

        self.database = database
        self.folder_name = folder_name
        self.test_folder_path = test_folder_path
        self.trace_file = ReadTraceFile()


    @abstractmethod
    def launch_test(self):
        """ `abstract`
        `Definition:` starts the execution of the complete test
        """

        pass
    

    @abstractmethod
    def launch_test_file(self, name_file: str):
        """ `abstract`
        `Type:` Procedure
        `Description:` execute the right files according to the name given in parameter
        """

        pass


    def execute_file_list(self, file_list: list[str]):
        """ `+`
        `Type:` Procedure
        `Description:` executes all files in the list
        :param:`file_list:` file to run
        """

        for fil in file_list:
            ExecuteTestFile().read_test_file(fil)
            time.sleep(0.2)