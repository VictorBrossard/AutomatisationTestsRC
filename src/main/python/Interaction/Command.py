# Author        : Victor BROSSARD
# Description   : Class that handles the arguments after the main class when executing the program with a line of code

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
from Useful.AllConstant import CONSTANT_USER_COMMAND
from Useful.AllConstant import CONSTANT_EXECUTION_FOLDER_PATH
from Useful.AllConstant import CONSTANT_TEST_NAME
from Useful.AllConstant import CONSTANT_TEST_SETTINGS_FILE_NAME

from Database.Database import Database

from Interaction.Interaction import Interaction

from Useful.UsefulFunction import get_program_list

from FilesManagement.Files.ManageSpecificFiles import ManageSpecificFiles
from FilesManagement.Files.CheckTestFileLines import CheckTestFileLines

from FilesManagement.Folders.ManageFolders import ManageFolders

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
        """ `+`
        `Type:` Procedure
        `Description:` find the right function associated with the right argument
        :param:`args:` arguments given at the execution of the command
        """

        if args[0] not in CONSTANT_USER_COMMAND:
            print("[ERREUR] La commande n'est pas bonne. [-help]")
            return
        
        # help command
        if args[0] == CONSTANT_USER_COMMAND[0]:
            self.__help_command()

        # start command
        if args[0] == CONSTANT_USER_COMMAND[1]:
            self.start_command(args)
        
        # prg command
        if args[0] == CONSTANT_USER_COMMAND[2]:
            self.__prg_command()

        # test piece command
        if args[0] == CONSTANT_USER_COMMAND[3]:
            self.__test_piece_command()

        # test list command
        if args[0] == CONSTANT_USER_COMMAND[4]:
            self.__test_list_command()


    def start_command(self, args: list[str]):
        """ `-`
        `Type:` Procedure
        `Description:` run one or more tests in a row
        :param:`args:` arguments given at the execution of the command

        `Command:` py main.py -start "path of the file"

        """

        # Intialization of variables
        database = Database()
        interaction = Interaction()

        # verification of the number of arguments
        if len(args) > 2:
            print("[ERREUR] Il y a trop d'arguments. [-help]")
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
        manage_files = ManageSpecificFiles()
        manage_folder = ManageFolders()
        check_lines = CheckTestFileLines()
        has_a_problem = False

        # decomposition of each line of the file
        for i, line in enumerate(lines):
            decompose_line = line.split(";")

            user_entry_list, is_line_correct = check_lines.check_line_informations(decompose_line)

            # guard that prevents errors
            if not is_line_correct or user_entry_list == []:
                print(f"[ERREUR] Fichier mal rempli à la ligne {i+1}.")
                has_a_problem = True
            
            if not has_a_problem:
                # creates a temporary folder to store all test pieces 
                manage_folder.delete_inside_folder(CONSTANT_EXECUTION_FOLDER_PATH)
                new_path_folder = manage_folder.create_folder(f"{user_entry_list[0]}", CONSTANT_EXECUTION_FOLDER_PATH)

                manage_files.create_file(new_path_folder, CONSTANT_TEST_SETTINGS_FILE_NAME, user_entry_list)

                # insertion of the test in the list according to the number put in the file
                for _ in range(0, int(decompose_line[1])):
                    file_paths_list.append(new_path_folder)

                interaction.execute_test(user_entry_list[0], database, file_paths_list)

                # deletion of files and folders temporarily created for testing purposes
                manage_folder.delete_inside_folder(new_path_folder)
                manage_folder.delete_folder(new_path_folder)

                file_paths_list.clear()

        database.close_connection()

    
    def __help_command(self):
        """ `-`
        `Type:` Procedure
        `Description:` helps the user by displaying all available commands

        `Command:` py main.py -help

        """

        print("Commande disponible :")

        for command in CONSTANT_USER_COMMAND:
            if command == "-start":
                print(". -start [chemin du fichier qui contient les instructions d'exécution des tests]")
            else:
                print(f". {command}")


    def __prg_command(self):
        """ `-`
        `Type:` Procedure
        `Description:` displays all available programs in RC

        `Command:` py main.py -prg
        
        """

        prg_list = get_program_list()

        print("Programme disponible :")

        for prg in prg_list:
            print(f". {prg}")


    def __test_piece_command(self):
        """ `-`
        `Type:` Procedure
        `Description:` launches the creation of a test piece

        `Command:` py main.py -testpiece
        
        """

        Interaction().create_test_piece()


    def __test_list_command(self):
        """ `-`
        `Type:` Procedure
        `Description:` displays all possible tests

        `Command:` py main.py -testlist
        
        """

        print("Test disponible :")

        for test in CONSTANT_TEST_NAME:
            print(f". {test}")