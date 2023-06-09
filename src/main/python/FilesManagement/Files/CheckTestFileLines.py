# Author        : Victor BROSSARD
# Description   : class that checks whether the line in the file containing the tests to be performed is correct

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
from Useful.AllConstant import CONSTANT_TEST_NAME

from Useful.UsefulFunction import get_program_list

#-----------------------------------------------------------------------------------------------------

class CheckTestFileLines(object):
    """ `+`
    :class:`CheckTestFileLines` checks whether the line in the file containing the tests to be performed is correct
    """
    
    def __init__(self):
        """ `-`
        `Type:` Constructor
        """

        pass


    def check_line_informations(self, line: list[str]) -> tuple[list[str], bool]:
        """ `+`
        `Type:` Function
        `Description:` executes the correct function according to the test
        `Return:` a Boolean and the list of user data to be saved in the test settings folder
        """

        if line[0] == CONSTANT_TEST_NAME[0]:
            return self.__check_line_informations_prod_test(line)
        
        return ([], False)


    def __check_line_informations_prod_test(self, line: list[str]) -> tuple[list[str], bool]:
        """ `-`
        `Type:` Function
        `Description:` checks that all the information in the given line is correct
        `Return:` a Boolean and the list of user data to be saved in the test settings folder
        """

        try:
            user_entry_list = [
                line[0], # test name
                line[2], # number of cards to produce
                line[3], # number of cards made
                line[4]  # program to run
            ]

            is_correct = (
                line[0] in CONSTANT_TEST_NAME               # name of the test file
                and int(line[1]) > 0                        # number of test iterations
                and int(line[2]) > 0                        # number of cards to produce
                and int(line[3]) >= 0                       # number of cards made
                and line[4].rstrip() in get_program_list()  # program to run
            )

            return (user_entry_list, is_correct)
            
        except Exception:
            return ([], False)