# Author        : Victor BROSSARD
# Description   : Class that manages the preconditions of the tests

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
from Interaction.ManageSoftwares import ManageSoftwares

from FilesManagement.Files.ManipulationSettingsFile import ManipulationSettingsFile
from FilesManagement.Folders.ManageFolders import ManageFolders

from Database.Database import Database

#-----------------------------------------------------------------------------------------------------

class Precondition(object):
    """ `+`
    :class:`Precondition` manages the preconditions of the tests
    """

    def __init__(self, database: Database):
        """ `-`
        `Type:` Constructor
        :param:`database:` object that manages the interaction with the database
        """

        self.settings = ManipulationSettingsFile()
        self.softwares = ManageSoftwares()
        self.database = database


    def start_precondition_prod_test(self) -> str:
        """ `+`
        `Type:` Function
        `Description:` launches the selected precondition
        `Return:` name of the last program loaded in RC
        """

        prg = self.__get_loaded_program()

        tmp_path = self.settings.get_line(7)

        self.softwares.close_soft()

        ManageFolders().delete_inside_folder(tmp_path)
        self.database.deletes_all_tuples()

        self.softwares.open_soft()

        return prg


    def __get_loaded_program(self) -> str:
        """ `-`
        `Type:` Function
        `Description:` Get the name of the last program loaded in RC
        `Return:` name of the last program loaded in RC
        """

        # get the value in the database
        try:
            prg = self.database.get_tuples(
                "SELECT RecipeName FROM workorderrecipemachines ORDER BY IdWorkOrderRecipeMachine DESC LIMIT 1;",
                []
            )

            return prg[0][0]
        except Exception:
            return ""