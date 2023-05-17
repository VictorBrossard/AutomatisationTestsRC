# Author        : Victor BROSSARD
# Description   : General graphical interface of the project

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import tkinter as tk
import ctypes
import os

from tkinter import ttk
from tkinter import filedialog

from Interaction.Interaction import Interaction
from Interaction.ManageSoftwares import ManageSoftwares

from GraphicInterface.SimpleQuestionInterface import SimpleQuestionInterface
from GraphicInterface.LoopTestInterface import LoopTestInterface
from GraphicInterface.SettingsInterface import SettingsInterface
from GraphicInterface.MessageBox import MessageBox
from GraphicInterface.UserEntryPopUp import UserEntryPopUp

from FilesManagement.Folders.ManageFolders import ManageFolders

from FilesManagement.Files.ManageAnyFile import ManageAnyFile
from FilesManagement.Files.ManageSpecificFiles import ManageSpecificFiles

from Useful.UsefulFunction import cant_close
from Useful.UsefulFunction import get_program_list

from Database.Database import Database

from Useful.AllConstant import CONSTANT_TEST_AVAILABLE_FOLDER_PATH

#-----------------------------------------------------------------------------------------------------

class MainInterface(tk.Tk):
    """ `+`
    :class:`MainInterface` manages the main interface of the project
    """

    def __init__(self, database: Database):
        """ `-`
        `Type:` Constructor
        :param:`database:` object that manages the interaction with the database
        """

        # Parent constructor
        super().__init__()

        self.data = database # Database object

        # Window size and position
        height = 600
        width = 250
        user = ctypes.windll.user32                             # User information
        x = int((user.GetSystemMetrics(0) / 2) - (height / 2))  # int() = any type to int
        y = int((user.GetSystemMetrics(1) / 2) - (width / 2))   # user32.GetSystemMetrics() = screen size (0 = height and 1 = width)

        # Interface initialization
        self.title('Main Interface')
        self.geometry(str(height) + "x" + str(width) + "+" + str(x) + "+" + str(y)) # Set window size and position | str() = any type to string
        self.resizable(width=0, height=0)                                           # Prevents any modification of window size
        self.protocol("WM_DELETE_WINDOW", cant_close)                               # Prevents the window from being closed by the red cross
        self.wm_attributes("-topmost", True)                                        # Prioritize the window

        # Configuring the placement of interface objects
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        # Adds interface objects to the interface
        self.__implementation()


    def __implementation(self):
        """ `-`
        `Type:` Procedure
        `Description:` adds interface objects to the interface
        """

        # Padding
        padding = {'padx': 5, 'pady': 5}

        # Button
        exit_button = ttk.Button(self, text='Exit', command=self.__close)   # Creation of the button
        exit_button.grid(column=2, row=2, **padding)                        # Object position

        create_test_button = ttk.Button(self, text='Create Test', command=self.__create_test)
        create_test_button.grid(column=1, row=1, **padding)

        delete_test_button = ttk.Button(self, text='Delete Test', command=self.__delete_test)
        delete_test_button.grid(column=2, row=0, **padding)

        start_test_button = ttk.Button(self, text='Start Test', command=self.__start_test)
        start_test_button.grid(column=1, row=0, **padding)

        test_pieces_button = ttk.Button(self, text='Test Pieces', command=self.__test_pieces)
        test_pieces_button.grid(column=2, row=1, **padding)

    
    def __close(self):
        """ `-`
        `Type:` Procedure
        `Description:` close software and the interface
        """

        ManageSoftwares().close_soft()
        self.data.close_connection()
        self.destroy()

    
    def __create_test(self):
        """ `-`
        `Type:` Procedure
        `Description:` start test recording
        """

        self.destroy()

        # pop-up asking for the name of the file we are going to create to save the test
        pop_up = UserEntryPopUp(
            "Create Tests", 
            ["Entrez le nom du test :", "Type du test"], 
            [3, 2], 
            [["production"]]
        )
        pop_up.mainloop()

        if pop_up.get_user_entries() != []:
            Interaction().create_test(is_command=False, user_entry_list=pop_up.get_user_entries())

        self.__init__(self.data) # Opening the interface
        self.mainloop()


    def __delete_test(self):
        """ `-`
        `Type:` Procedure
        `Description:` delete test
        """

        # Selection of files by the user
        file_paths = filedialog.askopenfilenames(initialdir=CONSTANT_TEST_AVAILABLE_FOLDER_PATH, title="Select folders")

        # checking if it is empty or not
        if file_paths:
            file_paths_list = list(file_paths) # turns the tuple into a list
            self.destroy()

            # Verification of the origin of the files
            for fil in file_paths_list:
                # We separate the name of the file and its path to be able to handle it better later
                file_path_without_name = os.path.dirname(fil)
                file_name = os.path.basename(fil)

                # checking if the file is in the right folder otherwise it is not a test
                if os.path.abspath(file_path_without_name) != os.path.abspath(CONSTANT_TEST_AVAILABLE_FOLDER_PATH):
                    MessageBox("ERREUR Sélection Fichier Test", f"[ERREUR] Le fichier {file_name} n'est pas un fichier test.")
                    self.__init__(self.data)
                    self.mainloop()
                    return

                # open the file that has the path to the folder to be deleted
                try:
                    open_file = open(fil, 'r')
                    path_file_to_delete = open_file.readlines()[0].rstrip()
                    open_file.close()
                except Exception as e:
                    MessageBox("ERREUR Fichier", f"[ERREUR] {e}").mainloop()
                    self.__init__(self.data)
                    self.mainloop()
                    return
                
                # delete folder
                folder = ManageFolders()
                folder.delete_inside_folder(path_file_to_delete)
                folder.delete_folder(path_file_to_delete)

                # delete file
                ManageAnyFile().delete_file(fil)

            MessageBox("Information", "[INFO] Tous les fichiers ont bien été supprimé.").mainloop()
            self.__init__(self.data)
            self.mainloop()


    def __start_test(self):
        """ `-`
        `Type:` Procedure
        `Description:` run one or more tests in a row
        """

        # Selection of files by the user
        file_paths = filedialog.askopenfilenames(initialdir=CONSTANT_TEST_AVAILABLE_FOLDER_PATH, title="Select folders")

        # checking if it is empty or not
        if file_paths:
            file_paths_list = list(file_paths) # turns the tuple into a list
            self.destroy()

            # Verification of the origin of the files
            for fil in file_paths_list:
                # We separate the name of the file and its path to be able to handle it better later
                file_path_without_name = os.path.dirname(fil)
                file_name = os.path.basename(fil)

                # checking if the file is in the right folder otherwise it is not a test
                if os.path.abspath(file_path_without_name) != os.path.abspath(CONSTANT_TEST_AVAILABLE_FOLDER_PATH):
                    MessageBox("ERREUR Sélection Fichier Test", f"[ERREUR] Le fichier {file_name} n'est pas un fichier test.")
                    self.__init__(self.data)
                    self.mainloop()
                    return

            # asks the user if he wants to loop on some tests
            simple_question = SimpleQuestionInterface("Question", "Est-ce que vous voulez jouer un test plusieurs fois d'affilée ?")
            simple_question.mainloop()

            # checks the user's response
            if simple_question.get_is_yes():
                # management of the number of times a test is performed
                loop = LoopTestInterface("Loop", file_paths_list)
                loop.mainloop()

                # new test list that has n times the test in the list, where n is the number entered as parameter by the user
                file_paths_list = loop.get_new_test_list()
            
            prg_list = get_program_list()

            for i, fil in enumerate(file_paths_list):                
                test_file = open(fil, 'r')
                test_folder_path = test_file.readlines()[0].rstrip()
                test_file.close()

                fil_name = os.path.basename(fil)

                pop_up = UserEntryPopUp(
                    f"{fil_name}",
                    ["Nombre de cartes à produire :", "Nombre de cartes faites :", "Initialisation de la machine :", "Programme :"],
                    [1, 1, 2, 2],
                    [["Partielle"], prg_list]
                )

                pop_up.mainloop()
                user_entry_list = pop_up.get_user_entries()

                if user_entry_list == []:
                    return

                new_file = ManageSpecificFiles()
                new_file.create_file(test_folder_path, f"test_{i}.txt", user_entry_list)

            # Launch of all tests
            Interaction().execute_test(self.data, file_paths_list)

            self.__init__(self.data)
            self.mainloop()


    def __test_pieces(self):
        """ `-`
        `Type:` Procedure
        `Description:` create a test piece
        """

        self.destroy()
        Interaction().test_pieces()
        self.__init__(self.data)
        self.mainloop()