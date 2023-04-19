# Author        : Victor BROSSARD
# Description   : General graphical interface of the project

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import tkinter as tk
import tkinter.messagebox
import subprocess
import ctypes
import win32gui
import time

from tkinter import ttk
from Interaction.Interaction import Interaction
from Interaction.Interaction import rc_window_foreground
from Interaction.InputRecorder import InputRecorder
from FilesManagement.InitFolders import CONSTANT_TESTS_FOLDER_PATH
from GraphicInterface.UserEntryPopUpMainInterface import UserEntryPopUpMainInterface

#-----------------------------------------------------------------------------------------------------
# 

testList = [
    'Loup',
    'Chien',
    'Chat'
]

#-----------------------------------------------------------------------------------------------------
# Class that manages the main interface
class MainInterface(tk.Tk):
    
    # Constructor
    def __init__(self):
        # Parent constructor
        super().__init__()

        # Window size and position
        height = 500
        width = 500
        user = ctypes.windll.user32                             # User information
        x = int((user.GetSystemMetrics(0) / 2) - (height / 2))  # int() = any type to int
        y = int((user.GetSystemMetrics(1) / 2) - (width / 2))   # user32.GetSystemMetrics() = screen size (0 = height and 1 = width)

        # Interface initialization
        self.title('Interface Principale')
        self.geometry(str(height) + "x" + str(width) + "+" + str(x) + "+" + str(y)) # Set window size and position | str() = any type to string
        self.resizable(width=0, height=0)                                           # Prevents any modification of window size
        self.protocol("WM_DELETE_WINDOW", cant_close)                               # Prevents the window from being closed by the red cross
        self.wm_attributes("-topmost", True)

        #
        self.input_file_name = tk.StringVar(self)

        # Configuring the placement of interface objects
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        # Adds interface objects to the interface
        self.implementation()

    # Function that adds interface objects to the interface
    def implementation(self):

        # Padding
        padding = {'padx': 5, 'pady': 5}

        # Button
        exit_button = ttk.Button(self, text='EXIT', command=self.close_softwares)   # Creation of the button
        exit_button.grid(column=2, row=3, **padding)                                # Object position

        destroy_button = ttk.Button(self, text='DESTROY', command=self.close_interface) # Creation of the button
        destroy_button.grid(column=2, row=4, **padding)                                 # Object position

        start_button = ttk.Button(self, text='START', command=self.start_test)
        start_button.grid(column=0, row=0, **padding)

        screenshot_button = ttk.Button(self, text='Screenshot', command=self.screenshot)
        screenshot_button.grid(column=2, row=0, **padding)

        record_button = ttk.Button(self, text='Record Tests', command=self.record_test)
        record_button.grid(column=2, row=1, **padding)

        # Menu
        #opt = ttk.OptionMenu(self, self.select, *testList)
        #opt.config(width=90, font=('Helvetica', 12))
        #opt.grid(column=0, row=0, **padding)

    # Function that closes software and the interface
    def close_softwares(self):
        # Close software
        try:
            self.wm_state('iconic')
            Interaction().close_rc()
        except Exception:
            pass

        time.sleep(1)

        try:
            subprocess.run(['taskkill', '/f', '/im', 'simulat.exe'], shell=True)
        except Exception:
            pass

        # Close interface
        self.destroy()

    #
    def close_interface(self):
        self.destroy()

    # 
    def start_test(self):
        ################ Minimisation de la fenêre de l'interface principal
        self.wm_state('iconic')

        rc_window_foreground()

    #
    def screenshot(self):
        self.wm_state('iconic')
        Interaction().screenshot()
        time.sleep(2)
        self.wm_state('normal') ######### remise à la normale

    #
    def record_test(self):
        self.wm_state('iconic')

        #
        pop_up = UserEntryPopUpMainInterface(self, "Record Tests", "Entrez le nom du test : ")
        pop_up.mainloop()

        #
        InputRecorder(pop_up.get_user_entry(), CONSTANT_TESTS_FOLDER_PATH)
        self.wm_state('normal')

#-----------------------------------------------------------------------------------------------------
# Function that returns a pop up to warn that the interface cannot be closed in this way
def cant_close():
    tkinter.messagebox.showinfo('Fermeture de la fenêtre impossible','Appuyer sur EXIT pour quitter')