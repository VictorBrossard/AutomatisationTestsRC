# Author        : Victor BROSSARD
# Description   : Class that creates the useful test pieces to do the real tests

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
from FilesManagement.Files.ManageAnyFile import ManageAnyFile

from Useful.AllConstant import CONSTANT_TEST_PIECES_FOLDER_PATH

#-----------------------------------------------------------------------------------------------------

class TestPiecesFile(ManageAnyFile):
    """ `+`
    :class:`TestPiecesFile` creates the useful test pieces to do the real tests
    """
    
    def __init__(self):
        """ `-`
        `Type:` Constructor
        """

        # specific action
        self.__partial_prod_no_prg_change()
        self.__partial_prod_prg_change()
        self.__placement_button()
        self.__validate_prod()
        self.__start_prod()
        self.__prod_parameter()
        self.__prod_program()
        self.__local_list_boxes()
        self.__program_change()
        self.__card_recalibration()
        self.__close_rc()

        # global action
        self.__down()
        self.__delete()
        self.__escape()
        self.__f1()
        self.__enter()


    ###################################### Specific action ######################################


    def __partial_prod_no_prg_change(self):
        """ `-`
        `Type:` Procedure
        `Description:` creates the file to turn on the machine in partial mode
        """

        execute_list = [
            "Click;left;0.50625;0.5768518518518518;1683117217.0307155",
            "Release;left;0.50625;0.5768518518518518;1683117217.102244",
            "Key;tab;1683117226.0307345"
        ]

        self.create_file(CONSTANT_TEST_PIECES_FOLDER_PATH, "partial_prod_no_prg_change.txt", execute_list)


    def __partial_prod_prg_change(self):
        """ `-`
        `Type:` Procedure
        `Description:` creates the file to turn on the machine in partial mode
        """

        execute_list = [
            "Click;left;0.5135416666666667;0.5703703703703704;1684230933.116967",
            "Release;left;0.5135416666666667;0.5703703703703704;1684230933.2136316",
            "Key;tab;1684230935.143767"
        ]

        self.create_file(CONSTANT_TEST_PIECES_FOLDER_PATH, "partial_prod_prg_change.txt", execute_list)


    def __placement_button(self):
        """ `-`
        `Type:` Procedure
        `Description:` cick on the placement button
        """

        execute_list = [
            "Click;left;0.7453125;0.7638888888888888;1684230931.7980804",
            "Release;left;0.7453125;0.7638888888888888;1684230931.8852599",
            "Key;tab;1684230933.116967"
        ]

        self.create_file(CONSTANT_TEST_PIECES_FOLDER_PATH, "placement_button.txt", execute_list)


    def __validate_prod(self):
        """ `-`
        `Type:` Procedure
        `Description:` validate production
        """

        execute_list = [
            "Click;left;0.3984375;0.7981481481481482;1683875857.9951065",
            "Release;left;0.3984375;0.7981481481481482;1683875858.1147294",
            "Key;tab;1683875858.2000000"
        ]

        self.create_file(CONSTANT_TEST_PIECES_FOLDER_PATH, "validate_prod.txt", execute_list)

    
    def __start_prod(self):
        """ `-`
        `Type:` Procedure
        `Description:` starts production
        """

        execute_list = [
            "Click;left;0.9291666666666667;0.1648148148148148;1683875899.458727",
            "Release;left;0.9291666666666667;0.1648148148148148;1683875899.5305402",
            "Key;tab;1683875902.109196"
        ]

        self.create_file(CONSTANT_TEST_PIECES_FOLDER_PATH, "start_prod.txt", execute_list)


    def __prod_parameter(self):
        """ `-`
        `Type:` Procedure
        `Description:` click on production parameter
        """

        execute_list = [
            "Click;left;0.3541666666666667;0.21666666666666667;1684219771.4711187",
            "Release;left;0.3541666666666667;0.21666666666666667;1684219771.5595381",
            "Key;tab;1684219771.857579"
        ]

        self.create_file(CONSTANT_TEST_PIECES_FOLDER_PATH, "prod_parameter.txt", execute_list)


    def __prod_program(self):
        """ `-`
        `Type:` Procedure
        `Description:` opening of the program selection interface
        """

        execute_list = [
            "Click;left;0.7578125;0.14074074074074075;1684220137.8726277",
            "Release;left;0.7578125;0.14074074074074075;1684220137.9526374",
            "Key;tab;1684220139.721512"
        ]

        self.create_file(CONSTANT_TEST_PIECES_FOLDER_PATH, "prod_program.txt", execute_list)


    def __local_list_boxes(self):
        """ `-`
        `Type:` Procedure
        `Description:` output of the local list interface for the boxes
        """

        execute_list = [
            "Click;left;0.7359375;0.8101851851851852;1684220772.2257774",
            "Release;left;0.7359375;0.8101851851851852;1684220772.2976933",
            "Key;tab;1684220774.4833186"
        ]

        self.create_file(CONSTANT_TEST_PIECES_FOLDER_PATH, "local_list_boxes.txt", execute_list)


    def __program_change(self):
        """ `-`
        `Type:` Procedure
        `Description:` production launch with the new program
        """

        execute_list = [
            "Click;left;0.5802083333333333;0.5675925925925925;1684220730.1616962",
            "Release;left;0.5802083333333333;0.5675925925925925;1684220730.2657285",
            "Key;tab;1684220732.682872"
        ]

        self.create_file(CONSTANT_TEST_PIECES_FOLDER_PATH, "program_change.txt", execute_list)


    def __card_recalibration(self):
        """ `-`
        `Type:` Procedure
        `Description:` removes the recalibration of the cards otherwise impossible to launch the production if you have changed the program
        """

        execute_list = [
            "Click;left;0.029166666666666667;0.03333333333333333;1684221946.3073158",
            "Release;left;0.029166666666666667;0.03333333333333333;1684221946.3795009",
            "Click;left;0.051041666666666666;0.07407407407407407;1684221947.3393285",
            "Release;left;0.051041666666666666;0.07407407407407407;1684221947.4199312",
            "Click;left;0.22708333333333333;0.5944444444444444;1684221948.9477534",
            "Release;left;0.22708333333333333;0.5944444444444444;1684221949.0194428",
            "Click;left;0.9255208333333333;0.4601851851851852;1684221950.3313127",
            "Release;left;0.9255208333333333;0.4601851851851852;1684221950.4431388",
            "Click;left;0.3734375;0.29074074074074074;1684221951.947336",
            "Release;left;0.3734375;0.29074074074074074;1684221952.0039098",
            "Click;left;0.6276041666666666;0.3509259259259259;1684221953.3557854",
            "Release;left;0.6276041666666666;0.3509259259259259;1684221953.45133",
            "Click;left;0.409375;0.7111111111111111;1684221954.7718697",
            "Release;left;0.409375;0.7111111111111111;1684221954.8193321",
            "Key;tab;1684221955.9157202"
        ]

        self.create_file(CONSTANT_TEST_PIECES_FOLDER_PATH, "card_recalibration.txt", execute_list)


    def __close_rc(self):
        """ `-`
        `Type:` Procedure
        `Description:` close rc
        """

        execute_list = [
            "Click;left;0.9510416666666667;0.8981481481481481;1685093749.9030514",
            "Release;left;0.9510416666666667;0.8981481481481481;1685093749.982205"
        ]

        self.create_file(CONSTANT_TEST_PIECES_FOLDER_PATH, "close_rc.txt", execute_list)
    

    ###################################### Global action ######################################


    def __delete(self):
        """ `-`
        `Type:` Procedure
        `Description:` delete
        """

        execute_list = [
            "Key;delete;0",
            "Key;tab;0.500001"
        ]

        self.create_file(CONSTANT_TEST_PIECES_FOLDER_PATH, "delete.txt", execute_list)


    def __down(self):
        """ `-`
        `Type:` Procedure
        `Description:` down
        """

        execute_list = [
            "Key;down;0",
            "Key;tab;0.500002"
        ]

        self.create_file(CONSTANT_TEST_PIECES_FOLDER_PATH, "down.txt", execute_list)


    def __escape(self):
        """ `-`
        `Type:` Procedure
        `Description:` escape
        """

        execute_list = [
            "Key;esc;0",
            "Key;tab;0.500002"
        ]

        self.create_file(CONSTANT_TEST_PIECES_FOLDER_PATH, "escape.txt", execute_list)


    def __f1(self):
        """ `-`
        `Type:` Procedure
        `Description:` f1
        """

        execute_list = [
            "Key;f1;1685092271.6512675",
            "Key;tab;1685092273.7469528"
        ]

        self.create_file(CONSTANT_TEST_PIECES_FOLDER_PATH, "f1.txt", execute_list)


    def __enter(self):
        """ `-`
        `Type:` Procedure
        `Description:` enter
        """

        execute_list = [
            "Key;enter;0",
            "Key;tab;1"
        ]

        self.create_file(CONSTANT_TEST_PIECES_FOLDER_PATH, "enter.txt", execute_list)