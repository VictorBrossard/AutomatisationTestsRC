# Author        : Victor BROSSARD
# Description   : Class that manages the postconditions of the tests

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import shutil

from Interaction.ManageSoftwares import ManageSoftwares

from FilesManagement.Files.ManipulationSettingsFile import ManipulationSettingsFile

from Database.Database import Database

from RCTest.ReadTraceFile import ReadTraceFile

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


    def start_postcondition(self, database: Database, folder_path: str, trace_file: ReadTraceFile):
        """ `+`
        `Type:` Procedure
        `Description:` launches the selected postcondition
        :param:`database:` object that manages the interaction with the database
        :param:`copy_traces_path:` path where we copy the trace folder
        :param:`trace_file:`
        """

        # Close Softwares
        trace_file.launch_test_file("close_rc.txt")
        self.softwares.close_soft()

        database.save_all_tuples(f"{folder_path}\\database")

        tmp_path = self.settings.get_line(7)
        shutil.copytree(tmp_path, f"{folder_path}\\traces")