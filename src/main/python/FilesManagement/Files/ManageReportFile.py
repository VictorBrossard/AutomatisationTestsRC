# Author        : Victor BROSSARD
# Description   : Class that manages report file

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
import subprocess
import os

from FilesManagement.Files.ManageAnyFile import ManageAnyFile

#-----------------------------------------------------------------------------------------------------

class ManageReportFile(ManageAnyFile):
    """ `+`
    :class:`ManageReportFile` manages report file
    """
    
    def __init__(self):
        """ `-`
        `Type:` Constructor
        """

        pass


    def create_report_file(self, path: str, line_list: list):
        """ `+`
        `Type:` Procedure
        `Description:` creates a txt file
        :param:`path:` path where you save the file
        :param:`line_list:` line to write in the file
        """

        self.create_file(path, "report.txt", line_list)