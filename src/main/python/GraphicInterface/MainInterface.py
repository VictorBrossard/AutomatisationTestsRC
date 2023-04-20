# Author        : Victor BROSSARD
# Description   : General graphical interface of the project

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import tkinter as tk
import subprocess
import ctypes
import time
import os

from tkinter import ttk
from Interaction.Interaction import Interaction
from UsefulFunction.UsefulFunction import cant_close
from FilesManagement.InitFolders import CONSTANT_TESTS_FOLDER_PATH
from UsefulFunction.UsefulFunction import do_nothing

#-----------------------------------------------------------------------------------------------------
# Class that manages the main interface
class MainInterface(tk.Tk):
    
    # Constructor
    def __init__(self):
        # Parent constructor
        super().__init__()

        # Window size and position
        height = 600
        width = 250
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
        self.test_list = os.listdir(CONSTANT_TESTS_FOLDER_PATH)

        # Configuring the placement of interface objects
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        # Adds interface objects to the interface
        self.__implementation()

    # Function that adds interface objects to the interface
    def __implementation(self):

        # Padding
        padding = {'padx': 5, 'pady': 5}

        # Button
        exit_button = ttk.Button(self, text='Exit', command=self.__close_softwares)   # Creation of the button
        exit_button.grid(column=2, row=3, **padding)                                # Object position

        destroy_button = ttk.Button(self, text='Destroy', command=self.__close_interface) # Creation of the button
        destroy_button.grid(column=2, row=4, **padding)                                 # Object position

        start_button = ttk.Button(self, text='Start', command=self.__start_test)
        start_button.grid(column=1, row=1, **padding)

        screenshot_button = ttk.Button(self, text='Screenshot', command=self.__screenshot)
        screenshot_button.grid(column=2, row=0, **padding)

        record_button = ttk.Button(self, text='Record Tests', command=self.__record_tests)
        record_button.grid(column=2, row=1, **padding)

        record_button = ttk.Button(self, text='Settings', command=self.__settings)
        record_button.grid(column=0, row=3, **padding)

        # Combobox
        self.display_test_list = ttk.Combobox(self, values=self.test_list, state="readonly")
        self.display_test_list.current(0)
        self.display_test_list.bind("<<ComboboxSelected>>", do_nothing)
        self.display_test_list.grid(column=1, row=0, **padding)

    # Function that closes software and the interface
    def __close_softwares(self):
        # Close software
        try:
            self.wm_state('iconic')
            Interaction().close_rc()
        except Exception:
            pass

        try:
            subprocess.run(['taskkill', '/f', '/im', 'simulat.exe'], shell=True)
        except Exception:
            pass

        # Close interface
        self.destroy()

    #
    def __close_interface(self):
        self.destroy()

    # 
    def __start_test(self):
        ################ Minimisation de la fenêre de l'interface principal
        self.wm_state('iconic')

        Interaction().execute_test(self.display_test_list.get())

        self.wm_state('normal')

    #
    def __screenshot(self):
        self.wm_state('iconic')
        Interaction().screenshot()
        self.wm_state('normal') ######### remise à la normale

    #
    def __record_tests(self):
        self.destroy()
        
        Interaction().write_test()
        
        self.__init__()

    def __settings(self):
        self.destroy()
        
        self.__init__()
