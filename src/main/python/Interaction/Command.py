# Author        : Victor BROSSARD
# Description   : Class that handles the arguments after the main class when executing the program with a line of code

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
import subprocess
import os

from Useful.AllConstant import CONSTANT_USER_COMMAND
from Useful.AllConstant import CONSTANT_TEST_AVAILABLE_FOLDER_PATH

from Database.Database import Database

from Interaction.Interaction import Interaction

from Useful.UsefulFunction import get_program_list

#-----------------------------------------------------------------------------------------------------

class Command(object):
    """ `+`
    :class:`Command` handles the arguments after the main class when executing the program with a line of code
    """
    
    def __init__(self, database: Database):
        """ `-`
        `Type:` Constructor
        :param:`database:` object that manages the interaction with the database
        """

        self.database = database
        self.interaction = Interaction()


    def translations_args(self, args: list[str]):
        """ `+`
        `Type:` Procedure
        `Description:` find the right function associated with the right argument
        :param:`args:` arguments given at the execution of the command
        """

        if args[0] not in CONSTANT_USER_COMMAND:
            print("[ERREUR] La commande n'est pas bonne.")
            return
        
        if args[0] == "-help":
            self.__help_command()

        if args[0] == "-start":
            self.__start_command(args)


    def __start_command(self, args: list[str]):
        """ `-`
        `Type:` Procedure
        `Description:` run one or more tests in a row
        :param:`args:` arguments given at the execution of the command

        `Command:` py main.py -start "path of the file"

        """

        if len(args) > 2:
            print("[ERREUR] Il y a trop d'arguments.")
            return
        
        try:
            fil = open(args[1], 'r')
            lines = fil.readlines()
            fil.close()
        except Exception as e:
            print("[ERREUR]", e)
            return

        for line in lines:
            decompose_line = line.split(";")
            is_correct = self.__check_informations_file(decompose_line)

            if not is_correct:
                return
            
            # à continuer

        self.interaction.execute_test(self.database, [])
            

    def __check_informations_file(self, line: list[str]) -> bool:
        """ `-`
        `Type:` Function
        `Description:` checks that all the information in the given line is correct
        `Return:` bool
        """

        try:
            return (
                not os.path.exists(f"{CONSTANT_TEST_AVAILABLE_FOLDER_PATH}\\{line[0]}.txt") 
                or int(line[1]) < 0 
                or int(line[2]) < 0 
                or int(line[3]) < 0
                or line[4] == "Partielle"
                or line[5] not in get_program_list()
            )
            
        except Exception as e:
            print("[ERREUR] Fichier mal rempli :", e)
            return False

    
    def __help_command(self):
        """ `-`
        `Type:` Procedure
        `Description:` helps the user by displaying all available commands

        `Command:` py main.py -help

        """

        print(CONSTANT_USER_COMMAND)