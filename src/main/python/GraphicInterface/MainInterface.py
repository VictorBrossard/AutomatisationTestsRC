# Author        : Victor BROSSARD
# Description   : General graphical interface of the project

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import tkinter as tk
import ctypes

from tkinter import ttk

from Interaction.Interaction import Interaction
from Interaction.ManageSoftwares import ManageSoftwares

from GraphicInterface.UserEntryPopUp import UserEntryPopUp

from Interaction.Command import Command

from Useful.UsefulFunction import cant_close

from Database.Database import Database

#-----------------------------------------------------------------------------------------------------

class MainInterface(tk.Tk):
    """ `+`
    :class:`MainInterface` manages the main interface of the project
    """

    def __init__(self):
        """ `-`
        `Type:` Constructor
        :param:`database:` object that manages the interaction with the database
        """

        # Parent constructor
        super().__init__()

        self.data = Database() # Database object

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

        # Adds interface objects to the interface
        self.__implementation()


    def __implementation(self):
        """ `-`
        `Type:` Procedure
        `Description:` adds interface objects to the interface
        """

        # Label
        title_label = ttk.Label(self, text='Interface principal')
        title_label.pack(side=tk.TOP, padx=5, pady=5)

        # Button
        start_test_button = ttk.Button(self, text='Start Test', command=self.__start_test)
        start_test_button.pack(side=tk.TOP, padx=5, pady=5)  

        test_pieces_button = ttk.Button(self, text='Test Pieces', command=self.__test_pieces)
        test_pieces_button.pack(side=tk.TOP, padx=5, pady=5) 

        exit_button = ttk.Button(self, text='Exit', command=self.__close)   # Creation of the button
        exit_button.pack(side=tk.TOP, padx=5, pady=5)                       # Object position

    
    def __close(self):
        """ `-`
        `Type:` Procedure
        `Description:` close software and the interface
        """

        ManageSoftwares().close_soft()
        self.data.close_connection()
        self.destroy()


    def __start_test(self):
        """ `-`
        `Type:` Procedure
        `Description:` run the start command
        """

        self.destroy()

        pop_up = UserEntryPopUp(
            "Chemin du fichier",
            ["Chemin du fichier qui contient les tests à exécuter :"],
            [0]
        )

        pop_up.mainloop()
        user_entry_list = pop_up.get_user_entries()

        Command(self.data).translations_args([
            "-start",
            user_entry_list[0]
        ])

        self.__init__()
        self.mainloop()


    def __test_pieces(self):
        """ `-`
        `Type:` Procedure
        `Description:` create a test piece
        """

        self.destroy()
        Interaction().create_test_piece()
        self.__init__()
        self.mainloop()