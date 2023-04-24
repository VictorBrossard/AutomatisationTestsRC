# Author        : Victor BROSSARD
# Description   : General graphical interface of the project

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import tkinter as tk
import tkinter.messagebox
import subprocess
import ctypes
import os

from tkinter import ttk
from Interaction.Interaction import Interaction
from FilesManagement.ManipulationSettingsFile import ManipulationSettingsFile
from FilesManagement.InitFolders import CONSTANT_TESTS_FOLDER_PATH
from UsefulFunction.UsefulFunction import cant_close
from UsefulFunction.UsefulFunction import do_nothing
from UsefulFunction.UsefulFunction import is_soft_open

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
        self.title('Interface Principale')
        self.geometry(str(height) + "x" + str(width) + "+" + str(x) + "+" + str(y)) # Set window size and position | str() = any type to string
        self.resizable(width=0, height=0)                                           # Prevents any modification of window size
        self.protocol("WM_DELETE_WINDOW", cant_close)                               # Prevents the window from being closed by the red cross
        self.wm_attributes("-topmost", True)                                        # Prioritize the window

        # List of test names stored in the test folder
        self.test_list = os.listdir(CONSTANT_TESTS_FOLDER_PATH)

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
        exit_button.grid(column=2, row=3, **padding)                                # Object position

        destroy_button = ttk.Button(self, text='Destroy', command=self.__close_interface)
        destroy_button.grid(column=2, row=4, **padding)

        start_button = ttk.Button(self, text='Start', command=self.__start_test)
        start_button.grid(column=1, row=1, **padding)

        screenshot_button = ttk.Button(self, text='Screenshot', command=self.__screenshot)
        screenshot_button.grid(column=2, row=0, **padding)

        record_button = ttk.Button(self, text='Record Tests', command=self.__record_tests)
        record_button.grid(column=2, row=1, **padding)

        settings_button = ttk.Button(self, text='Settings', command=self.__settings)
        settings_button.grid(column=0, row=3, **padding)

        # Combobox
        self.display_test_list = ttk.Combobox(self, values=self.test_list, state="readonly")
        self.display_test_list.current(0)
        self.display_test_list.bind("<<ComboboxSelected>>", do_nothing)
        self.display_test_list.grid(column=1, row=0, **padding)

    
    def __close_softwares(self):
        """ `-`
        `Type:` Procedure
        `Description:` close software and the interface
        """

        line_settings_file = ManipulationSettingsFile() # read the file that contains the parameters

        # Close softwares
        try:
            if is_soft_open(line_settings_file.get_rc_exe()):
                self.wm_state('iconic')                         # Minimization of the main interface window
                Interaction().close_rc()
        except Exception as e:
            tkinter.messagebox.showinfo('RC Closing ERROR', e)  # Displaying the error message for the user

        try:
            if is_soft_open(line_settings_file.get_simu_exe()):
                subprocess.run(['taskkill', '/f', '/im', line_settings_file.get_simu_exe()], shell=True)    # Shell command to close the simulator
        except Exception as e:
            tkinter.messagebox.showinfo('Simulator Closing ERROR', e)                                       # Displaying the error message for the user

        self.destroy() # Closing the interface

    
    def __close_interface(self):
        """ `-`
        `Type:` Procedure
        `Description:` close only the interface
        """

        self.destroy()


    def __start_test(self):
        """ `-`
        `Type:` Procedure
        `Description:` start test select
        """

        #self.destroy()
        self.wm_state('iconic') # Minimization of the main interface window
        Interaction().execute_test(self.display_test_list.get())
        self.wm_state('normal') # Reset the interface to normal
        #self.__init__()

    
    def __screenshot(self):
        """ `-`
        `Type:` Procedure
        `Description:` take a screenshot
        """

        self.destroy()
        Interaction().screenshot()
        self.__init__()

    
    def __record_tests(self):
        """ `-`
        `Type:` Procedure
        `Description:` start test recording
        """

        self.destroy()
        Interaction().write_test()
        self.__init__() # Opening the interface


    def __settings(self):
        """ `-`
        `Type:` Procedure
        `Description:` open the settings interface
        """

        self.destroy()
        Interaction().settings()
        self.__init__()
