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

from FilesManagement.Files.ManageAnyFile import ManageAnyFile

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
        
        # help command
        if args[0] == "-help":
            self.__help_command()

        # start command
        if args[0] == "-start":
            self.__start_command(args)


    def __start_command(self, args: list[str]):
        """ `-`
        `Type:` Procedure
        `Description:` run one or more tests in a row
        :param:`args:` arguments given at the execution of the command

        `Command:` py main.py -start "path of the file"

        """

        # verification of the number of arguments
        if len(args) > 2:
            print("[ERREUR] Il y a trop d'arguments.")
            return
        
        # recovery of the lines of the file of the tests that we want to make
        try:
            fil = open(args[1], 'r')
            lines = fil.readlines()
            fil.close()
        except Exception as e:
            print("[ERREUR]", e)
            return
        
        # initialization of variables 
        file_paths_list = []
        new_file = ManageAnyFile()

        # decomposition of each line of the file
        for i, line in enumerate(lines):
            decompose_line = line.split(";")
            is_correct = self.__check_informations_file(decompose_line)

            # guard that prevents errors
            if not is_correct:
                print(f"[ERREUR] Fichier mal rempli à la ligne {i}.")
                return

            user_entry_list = [
                decompose_line[2], # number of cards to produce
                decompose_line[3], # number of cards made
                decompose_line[4], # initialization of the machine
                decompose_line[5]  # program to run
            ]

            # test folder path
            test_file = open(f"{CONSTANT_TEST_AVAILABLE_FOLDER_PATH}\\{decompose_line[0]}.txt", 'r')
            test_folder_path = test_file.readlines()[0].rstrip()
            test_file.close()

            # insertion of the test in the list according to the number put in the file
            for j in range(0, int(decompose_line[1])):
                file_paths_list.append(f"{CONSTANT_TEST_AVAILABLE_FOLDER_PATH}\\{decompose_line[0]}.txt")
                new_file.create_file(test_folder_path, f"test_{j}.txt", user_entry_list)

        self.interaction.execute_test(self.database, file_paths_list)
            

    def __check_informations_file(self, line: list[str]) -> bool:
        """ `-`
        `Type:` Function
        `Description:` checks that all the information in the given line is correct
        `Return:` bool
        """

        try:
            return (
                os.path.exists(f"{CONSTANT_TEST_AVAILABLE_FOLDER_PATH}\\{line[0]}.txt") # name of the test file
                and int(line[1]) > 0                                                    # number of test iterations
                and int(line[2]) > 0                                                    # number of cards to produce
                and int(line[3]) >= 0                                                   # number of cards made
                and line[4] == "Partielle"                                              # initialization of the machine
                and line[5] in get_program_list()                                       # program to run
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