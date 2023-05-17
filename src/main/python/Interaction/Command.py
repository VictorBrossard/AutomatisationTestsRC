# Author        : Victor BROSSARD
# Description   : Class that handles the arguments after the main class when executing the program with a line of code

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
import subprocess
import os

#-----------------------------------------------------------------------------------------------------

class Command(object):
    """ `+`
    :class:`Command` handles the arguments after the main class when executing the program with a line of code
    """
    
    def __init__(self):
        """ `-`
        `Type:` Constructor
        """

        pass


    def translations_args(self, args: list[str]):
        """
        """

        print(args)