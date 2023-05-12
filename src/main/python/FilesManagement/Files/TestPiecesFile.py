# Author        : Victor BROSSARD
# Description   : Class that creates the useful test pieces to do the real tests

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
from FilesManagement.Files.ManageAnyFile import ManageAnyFile

from FilesManagement.Folders.ManageFolders import CONSTANT_TEST_PIECES_FOLDER_PATH

#-----------------------------------------------------------------------------------------------------

class TestPiecesFile(ManageAnyFile):
    """ `+`
    :class:`TestPiecesFile` creates the useful test pieces to do the real tests
    """
    
    def __init__(self):
        """ `-`
        `Type:` Constructor
        """

        self.__partial_prod()
        self.__complete_prod()
        self.__name_prod()
        self.__nb_card_to_make_prod()
        self.__nb_card_make_prod()
        self.__validate_prod()
        self.__start_prod()
        self.__stop_prod()


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
            "Key;tab;1683117226.0307345"
        ]

        self.create_file(CONSTANT_TEST_PIECES_FOLDER_PATH, "partial_prod.txt", execute_list)


    def __complete_prod(self):
        """ `-`
        `Type:` Function
        `Description:` creates the file to turn on the machine in complete mode
        `Return:` file path
        """

        execute_list = [

        ]

        self.create_file(CONSTANT_TEST_PIECES_FOLDER_PATH, "complete_prod.txt", execute_list)
    

    def __name_prod(self):
        """ `-`
        `Type:` Function
        `Description:` deletes the name of the production
        `Return:` file path
        """

        execute_list = [
            "Click;left;0.359375;0.21296296296296297;1683187807.883292",
            "Release;left;0.359375;0.21296296296296297;1683187808.0112479",
            "Key;delete;1683187809.2044904"
        ]

        self.create_file(CONSTANT_TEST_PIECES_FOLDER_PATH, "name_prod.txt", execute_list)
    

    def __nb_card_to_make_prod(self):
        """ `-`
        `Type:` Function
        `Description:` removes the number of cards to be made
        `Return:` file path
        """

        execute_list = [
            "Key;down;1683191945.778898",
            "Key;delete;1683191946.6426668"
        ]

        self.create_file(CONSTANT_TEST_PIECES_FOLDER_PATH, "nb_card_to_make_prod.txt", execute_list)
    

    def __nb_card_make_prod(self):
        """ `-`
        `Type:` Function
        `Description:` removes the number of cards made
        `Return:` file path
        """

        execute_list = [
            "Key;down;1683191945.778898",
            "Key;delete;1683191945.900000"
        ]

        self.create_file(CONSTANT_TEST_PIECES_FOLDER_PATH, "nb_card_make_prod.txt", execute_list)


    def __validate_prod(self):
        """ `-`
        `Type:` Function
        `Description:` validate production
        `Return:` file path
        """

        execute_list = [
            "Click;left;0.3984375;0.7981481481481482;1683875857.9951065",
            "Release;left;0.3984375;0.7981481481481482;1683875858.1147294",
            "Key;tab;1683875858.2000000"
        ]

        self.create_file(CONSTANT_TEST_PIECES_FOLDER_PATH, "validate_prod.txt", execute_list)

    
    def __start_prod(self):
        """ `-`
        `Type:` Function
        `Description:` starts production
        `Return:` file path
        """

        execute_list = [
            "Click;left;0.9291666666666667;0.1648148148148148;1683875899.458727",
            "Release;left;0.9291666666666667;0.1648148148148148;1683875899.5305402",
            "Key;tab;1683875902.109196"
        ]

        self.create_file(CONSTANT_TEST_PIECES_FOLDER_PATH, "start_prod.txt", execute_list)


    def __stop_prod(self):
        """ `-`
        `Type:` Function
        `Description:` ends production
        `Return:` file path
        """

        execute_list = [
            "Click;left;0.9135416666666667;0.2101851851851852;1683268464.5933928",
            "Release;left;0.9135416666666667;0.2101851851851852;1683268464.6497576",
            "Key;tab;1683268467.7141564"
        ]

        self.create_file(CONSTANT_TEST_PIECES_FOLDER_PATH, "stop_prod.txt", execute_list)