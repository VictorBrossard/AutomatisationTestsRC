# Author        : Victor BROSSARD
# Description   : Class that creates the useful test pieces to do the real tests

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
import os

from FilesManagement.InitFile import InitFile
from FilesManagement.InitFolder import CONSTANT_TEST_PIECES_FOLDER_PATH

#-----------------------------------------------------------------------------------------------------

class TestPieces(InitFile):
    """ `+`
    :class:`TestPieces` creates the useful test pieces to do the real tests
    """
    
    def __init__(self):
        """ `-`
        `Type:` Constructor
        """

        self.partial = self.__partial_prod()
        self.complete = self.__complete_prod()


    def __partial_prod(self):
        """ `-`
        `Type:` Function
        `Description:` creates the file to turn on the machine in partial mode
        `Return:` file path
        """

        execute_list = [
            "Click;left;0.7770833333333333;0.7888888888888889;1683117215.4386811",
            "Release;left;0.7770833333333333;0.7888888888888889;1683117215.502193",
            "Click;left;0.50625;0.5768518518518518;1683117217.0307155",
            "Release;left;0.50625;0.5768518518518518;1683117217.102244",
            "Click;left;0.50625;0.5768518518518518;1683117226.0307345",
            "Release;left;0.50625;0.5768518518518518;1683117226.1266954"
        ]

        full_path = f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\partial_prod.txt"

        if os.path.exists(full_path):
            os.remove(full_path)

        return self.create_file(CONSTANT_TEST_PIECES_FOLDER_PATH, "partial_prod.txt", execute_list)


    def __complete_prod(self):
        """ `-`
        `Type:` Function
        `Description:` creates the file to turn on the machine in complete mode
        `Return:` file path
        """

        execute_list = []

        full_path = f"{CONSTANT_TEST_PIECES_FOLDER_PATH}\\complete_prod.txt"

        if os.path.exists(full_path):
            os.remove(full_path)

        return self.create_file(CONSTANT_TEST_PIECES_FOLDER_PATH, "complete_prod.txt", execute_list)