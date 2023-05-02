# Author        : Victor BROSSARD
# Description   : Class that manages the postconditions of the tests

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
from RCTest.ManagesSoftwares.ManageSoftwares import ManageSoftwares

#-----------------------------------------------------------------------------------------------------

class PostCondition(object):
    """ `+`
    :class:`PostCondition` manages the postconditions of the tests
    """

    def __init__(self):
        """ `-`
        `Type:` Constructor
        """

        self.softwares = ManageSoftwares()


    def start_postcondition(self):
        """ `+`
        `Type:` Function
        `Description:` launches the selected postcondition
        """

        self.softwares.close_soft()