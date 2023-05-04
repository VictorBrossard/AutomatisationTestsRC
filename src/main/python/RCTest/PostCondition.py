# Author        : Victor BROSSARD
# Description   : Class that manages the postconditions of the tests

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import shutil

from RCTest.ManageSoftwares import ManageSoftwares

from FilesManagement.Files.ManipulationSettingsFile import ManipulationSettingsFile

#-----------------------------------------------------------------------------------------------------

class PostCondition(object):
    """ `+`
    :class:`PostCondition` manages the postconditions of the tests
    """

    def __init__(self):
        """ `-`
        `Type:` Constructor
        """

        self.settings = ManipulationSettingsFile()
        self.softwares = ManageSoftwares()


    def start_postcondition(self, copy_traces_path: str):
        """ `+`
        `Type:` Function
        `Description:` launches the selected postcondition
        :param:`copy_traces_path:` path where we copy the trace folder
        """

        self.softwares.close_soft()

        tmp_path = self.settings.get_line(8)

        shutil.copytree(tmp_path, f"{copy_traces_path}\\traces")