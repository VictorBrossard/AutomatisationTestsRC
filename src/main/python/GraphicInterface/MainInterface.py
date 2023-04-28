# Author        : Victor BROSSARD
# Description   : General graphical interface of the project

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import tkinter as tk
import tkinter.messagebox
import subprocess
import ctypes

from tkinter import ttk
from tkinter import filedialog

from Interaction.Interaction import Interaction

from GraphicInterface.SimpleQuestionInterface import SimpleQuestionInterface
from GraphicInterface.LoopTestInterface import LoopTestInterface

from FilesManagement.ManipulationSettingsFile import ManipulationSettingsFile
from FilesManagement.InitFolders import CONSTANT_TESTS_FOLDER_PATH

from UsefulFunction.UsefulFunction import cant_close
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

        destroy_button = ttk.Button(self, text='Destroy', command=self.__close_interface)
        destroy_button.grid(column=2, row=3, **padding)

        start_test_button = ttk.Button(self, text='Start Test', command=self.__start_test)
        start_test_button.grid(column=1, row=0, **padding)

        screenshot_button = ttk.Button(self, text='Screenshot', command=self.__screenshot)
        screenshot_button.grid(column=2, row=0, **padding)

        record_button = ttk.Button(self, text='Record Tests', command=self.__record_tests)
        record_button.grid(column=2, row=1, **padding)

        settings_button = ttk.Button(self, text='Settings', command=self.__settings)
        settings_button.grid(column=0, row=2, **padding)

    
    def __close_softwares(self):
        """ `-`
        `Type:` Procedure
        `Description:` close software and the interface
        """

        self.destroy()
        simple_question = SimpleQuestionInterface("Close softwares", "Are you on the home page of RC to be able to close it without any problem?")
        simple_question.mainloop()

        if simple_question.get_is_yes():
            line_settings_file = ManipulationSettingsFile() # read the file that contains the parameters

            # Close softwares
            try:
                if is_soft_open(line_settings_file.get_rc_exe()):
                    Interaction().close_rc()
            except Exception as e:
                tkinter.messagebox.showinfo('RC Closing ERROR', e)  # Displaying the error message for the user

            try:
                if is_soft_open(line_settings_file.get_simu_exe()):
                    subprocess.run(['taskkill', '/f', '/im', line_settings_file.get_simu_exe()], shell=True)    # Shell command to close the simulator
            except Exception as e:
                tkinter.messagebox.showinfo('Simulator Closing ERROR', e)                                       # Displaying the error message for the user
        else:
            self.__init__()

    
    def __close_interface(self):
        """ `-`
        `Type:` Procedure
        `Description:` close only the interface
        """

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

    
    def __record_tests(self):
        """ `-`
        `Type:` Procedure
        `Description:` start test recording
        """

        self.destroy()
        Interaction().write_test()
        self.__init__() # Opening the interface
        self.mainloop()


    def __settings(self):
        """ `-`
        `Type:` Procedure
        `Description:` open the settings interface
        """

        self.destroy()
        Interaction().settings()
        self.__init__()
        self.mainloop()


    def __start_test(self):
        """ `-`
        `Type:` Procedure
        `Description:` run one or more tests in a row
        """

        # Selection of files by the user
        file_paths = filedialog.askopenfilenames(initialdir= CONSTANT_TESTS_FOLDER_PATH, title="Select files")

        # checking if it is empty or not
        if file_paths:
            file_paths_list = list(file_paths) # turns the tuple into a list
            self.destroy()

            # asks the user if he wants to loop on some tests
            simple_question = SimpleQuestionInterface("Question", "Do you want to test several times in a row?")
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