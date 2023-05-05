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

from GraphicInterface.SimpleQuestionInterface import SimpleQuestionInterface
from GraphicInterface.LoopTestInterface import LoopTestInterface
from GraphicInterface.SettingsInterface import SettingsInterface
from GraphicInterface.MessageBox import MessageBox

from FilesManagement.Folders.ManageFolders import CONSTANT_TEST_AVAILABLE_FOLDER_PATH

from UsefulFunction.UsefulFunction import cant_close

from RCTest.ManageSoftwares import ManageSoftwares

#-----------------------------------------------------------------------------------------------------

class MainInterface(tk.Tk):
    """ `+`
    :class:`MainInterface` manages the main interface of the project
    """

    def __init__(self):
        """ `-`
        `Type:` Constructor
        """

        # Parent constructor
        super().__init__()

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
        exit_button = ttk.Button(self, text='Exit', command=self.__close_softwares) # Creation of the button
        exit_button.grid(column=2, row=2, **padding)                                # Object position

        start_test_button = ttk.Button(self, text='Start Test', command=self.__start_test)
        start_test_button.grid(column=1, row=0, **padding)

        screenshot_button = ttk.Button(self, text='Screenshot', command=self.__screenshot)
        screenshot_button.grid(column=2, row=0, **padding)

        create_button = ttk.Button(self, text='Create Test', command=self.__create_test)
        create_button.grid(column=1, row=1, **padding)

        delete_button = ttk.Button(self, text='Delete Test', command=self.__delete_test)
        delete_button.grid(column=0, row=2, **padding)

        pieces_button = ttk.Button(self, text='Test Pieces', command=self.__test_pieces)
        pieces_button.grid(column=2, row=1, **padding)

    
    def __close_softwares(self):
        """ `-`
        `Type:` Procedure
        `Description:` close software and the interface
        """

        ManageSoftwares().close_soft()
        self.destroy()

    
    def __screenshot(self):
        """ `-`
        `Type:` Procedure
        `Description:` take a screenshot
        """

        self.destroy()
        Interaction().screenshot()
        self.__init__()
        self.mainloop()

    
    def __create_test(self):
        """ `-`
        `Type:` Procedure
        `Description:` start test recording
        """

        self.destroy()
        Interaction().create_test()
        self.__init__() # Opening the interface
        self.mainloop()


    def __delete_test(self):
        """ `-`
        `Type:` Procedure
        `Description:` delete test
        """

        self.destroy()
        self.__init__()
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
                    self.__init__()
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
                new_list = loop.get_new_test_list()

                if new_list != []:
                    Interaction().execute_test(new_list)
            else:
                Interaction().execute_test(file_paths_list)

            self.__init__()
            self.mainloop()


    def __test_pieces(self):
        """ `-`
        `Type:` Procedure
        `Description:` create a test piece
        """

        self.destroy()
        Interaction().test_pieces()
        self.__init__()
        self.mainloop()