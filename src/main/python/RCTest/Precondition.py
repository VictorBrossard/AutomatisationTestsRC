# Author        : Victor BROSSARD
# Description   : Class that manages the preconditions of the tests

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import os

from RCTest.ManageSoftwares import ManageSoftwares

from FilesManagement.Files.ManipulationSettingsFile import ManipulationSettingsFile
from FilesManagement.Folders.ManageFolders import ManageFolders

from Database.Database import Database

#-----------------------------------------------------------------------------------------------------

class Precondition(object):
    """ `+`
    :class:`Precondition` manages the preconditions of the tests
    """

    def __init__(self):
        """ `-`
        `Type:` Constructor
        """

        self.settings = ManipulationSettingsFile()
        self.softwares = ManageSoftwares()


    def start_precondition(self, database: Database):
        """ `+`
        `Type:` Function
        `Description:` launches the selected precondition
        :param:`database:` object that manages the interaction with the database
        """

        tmp_path = self.settings.get_line(8)

        self.softwares.close_soft()

        ManageFolders().delete_inside_folder(tmp_path)
        database.deletes_all_tuples()

        self.softwares.open_soft()