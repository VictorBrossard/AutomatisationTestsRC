# Author        : Victor BROSSARD
# Description   : Settings graphical interface

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import tkinter as tk
import subprocess
import ctypes
import time
import os

from tkinter import ttk
from UsefulFunction.UsefulFunction import cant_close

#-----------------------------------------------------------------------------------------------------
# Initialization of constants
# Column
_CONSTANT_LABEL_COLUMN = int(0)
_CONSTANT_ENTRY_COLUMN = int(2)
_CONSTANT_TITLE_COLUMN = int(1)
_CONSTANT_BUTTON_COLUMN = int(1)

# Title
_CONSTANT_SETTINGS_TITLE_LINE = int(0)
_CONSTANT_TEST_TITLE_LINE = int(7)

# Line
_CONSTANT_SIMU_EXE_LINE = _CONSTANT_SETTINGS_TITLE_LINE + 1
_CONSTANT_RC_EXE_LINE = _CONSTANT_SIMU_EXE_LINE + 1
_CONSTANT_SIMU_PATH_LINE = _CONSTANT_RC_EXE_LINE + 1
_CONSTANT_RC_PATH_LINE = _CONSTANT_SIMU_PATH_LINE + 1
_CONSTANT_FOLDER_PATH_LINE = _CONSTANT_RC_PATH_LINE + 1
_CONSTANT_RC_WINDOW_NAME_LINE = _CONSTANT_FOLDER_PATH_LINE + 1
_CONSTANT_STOP_KEY_LINE = _CONSTANT_TEST_TITLE_LINE + 1

# Button
_CONSTANT_BUTTON_LINE = _CONSTANT_STOP_KEY_LINE + 1

#-----------------------------------------------------------------------------------------------------

class SettingsInterface(tk.Tk):
    """ `+`
    :class:`SettingsInterface` manages the settings interface of the project
    """

    def __init__(self):
        """ `-`
        `Type:` Constructor
        """

        # Parent constructor
        super().__init__()

        # Window size and position
        height = 500
        width = 350
        user = ctypes.windll.user32                             # User information
        x = int((user.GetSystemMetrics(0) / 2) - (height / 2))  # int() = any type to int
        y = int((user.GetSystemMetrics(1) / 2) - (width / 2))   # user32.GetSystemMetrics() = screen size (0 = height and 1 = width)

        # Interface initialization
        self.title('Interface Principale')
        self.geometry(str(height) + "x" + str(width) + "+" + str(x) + "+" + str(y)) # Set window size and position | str() = any type to string
        self.resizable(width=0, height=0)                                           # Prevents any modification of window size
        self.protocol("WM_DELETE_WINDOW", cant_close)                               # Prevents the window from being closed by the red cross
        self.wm_attributes("-topmost", True)                                        # Prioritize the window

        # Variable that stores the value given by the user
        self.simu_exe = tk.StringVar()

        self.simu_path = tk.StringVar()

        self.rc_exe = tk.StringVar()

        self.rc_path = tk.StringVar()

        self.rc_window_name = tk.StringVar()

        self.folder_path = tk.StringVar()

        self.test_stop_key = tk.StringVar()


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
        exit_button = ttk.Button(self, text='Exit', command=self.__close_interface)                 # Creation of the button
        exit_button.grid(column= _CONSTANT_BUTTON_COLUMN, row= _CONSTANT_BUTTON_LINE, **padding)    # Object position

        # Label
        # Title
        settings_title_label = ttk.Label(self, text="General Settings") # Creation of the label
        settings_title_label.grid(column= _CONSTANT_TITLE_COLUMN, row= _CONSTANT_SETTINGS_TITLE_LINE, **padding)         # Object position

        test_title_label = ttk.Label(self, text="Test Settings")              
        test_title_label.grid(column= _CONSTANT_TITLE_COLUMN, row= _CONSTANT_TEST_TITLE_LINE, **padding)

        # Description
        simu_exe_label = ttk.Label(self, text="simu_exe")              
        simu_exe_label.grid(column= _CONSTANT_LABEL_COLUMN, row= _CONSTANT_SIMU_EXE_LINE, **padding)

        rc_exe_label = ttk.Label(self, text="rc_exe")              
        rc_exe_label.grid(column= _CONSTANT_LABEL_COLUMN, row= _CONSTANT_RC_EXE_LINE, **padding)

        simu_path_label = ttk.Label(self, text="simu_path")              
        simu_path_label.grid(column= _CONSTANT_LABEL_COLUMN, row= _CONSTANT_SIMU_PATH_LINE, **padding)

        rc_path_label = ttk.Label(self, text="rc_path")              
        rc_path_label.grid(column= _CONSTANT_LABEL_COLUMN, row= _CONSTANT_RC_PATH_LINE, **padding)

        folder_path_label = ttk.Label(self, text="folder_path")              
        folder_path_label.grid(column= _CONSTANT_LABEL_COLUMN, row= _CONSTANT_FOLDER_PATH_LINE, **padding)

        rc_window_name_label = ttk.Label(self, text="rc window")              
        rc_window_name_label.grid(column= _CONSTANT_LABEL_COLUMN, row= _CONSTANT_RC_WINDOW_NAME_LINE, **padding)

        stop_key_label = ttk.Label(self, text="stop key")              
        stop_key_label.grid(column= _CONSTANT_LABEL_COLUMN, row= _CONSTANT_STOP_KEY_LINE, **padding)         

        # Entry 
        simu_exe_entry = ttk.Entry(self, textvariable=self.simu_exe)                                    # Creation of the entry
        simu_exe_entry.grid(column= _CONSTANT_ENTRY_COLUMN, row= _CONSTANT_SIMU_EXE_LINE, **padding)  # Object position

        rc_exe_entry = ttk.Entry(self, textvariable=self.rc_exe)  
        rc_exe_entry.grid(column= _CONSTANT_ENTRY_COLUMN, row= _CONSTANT_RC_EXE_LINE, **padding)

        simu_path_entry = ttk.Entry(self, textvariable=self.simu_path)  
        simu_path_entry.grid(column= _CONSTANT_ENTRY_COLUMN, row= _CONSTANT_SIMU_PATH_LINE, **padding)

        rc_path_entry = ttk.Entry(self, textvariable=self.rc_path)  
        rc_path_entry.grid(column= _CONSTANT_ENTRY_COLUMN, row= _CONSTANT_RC_PATH_LINE, **padding)

        folder_path_entry = ttk.Entry(self, textvariable=self.folder_path)  
        folder_path_entry.grid(column= _CONSTANT_ENTRY_COLUMN, row= _CONSTANT_FOLDER_PATH_LINE, **padding) 

        rc_window_name_entry = ttk.Entry(self, textvariable=self.rc_window_name)  
        rc_window_name_entry.grid(column= _CONSTANT_ENTRY_COLUMN, row= _CONSTANT_RC_WINDOW_NAME_LINE, **padding) 

        test_stop_key_entry = ttk.Entry(self, textvariable=self.test_stop_key)  
        test_stop_key_entry.grid(column= _CONSTANT_ENTRY_COLUMN, row= _CONSTANT_STOP_KEY_LINE, **padding)                
        

    def __close_interface(self):
        """ `-`
        `Type:` Procedure
        `Description:` close only the interface
        """

        self.destroy()