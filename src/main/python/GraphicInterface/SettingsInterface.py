# Author        : Victor BROSSARD
# Description   : Settings graphical interface

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import tkinter as tk
import ctypes

from tkinter import ttk

from Useful.UsefulFunction import cant_close

from FilesManagement.Files.ManipulationSettingsFile import ManipulationSettingsFile

from GraphicInterface.ChangeKeyInterface import ChangeKeyInterface

from Useful.AllConstant import CONSTANT_LABEL_COLUMN
from Useful.AllConstant import CONSTANT_ENTRY_COLUMN
from Useful.AllConstant import CONSTANT_TITLE_COLUMN
from Useful.AllConstant import CONSTANT_BUTTON_COLUMN

from Useful.AllConstant import CONSTANT_SETTINGS_TITLE_LINE
from Useful.AllConstant import CONSTANT_TEST_TITLE_LINE

from Useful.AllConstant import CONSTANT_SIMU_EXE_LINE
from Useful.AllConstant import CONSTANT_RC_EXE_LINE
from Useful.AllConstant import CONSTANT_SIMU_PATH_LINE
from Useful.AllConstant import CONSTANT_RC_PATH_LINE
from Useful.AllConstant import CONSTANT_FOLDER_PATH_LINE
from Useful.AllConstant import CONSTANT_RC_WINDOW_NAME_LINE
from Useful.AllConstant import CONSTANT_STOP_KEY_LINE

from Useful.AllConstant import CONSTANT_BUTTON_LINE

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

        self.is_listening = False

        # Window size and position
        height = 600
        width = 400
        user = ctypes.windll.user32                             # User information
        x = int((user.GetSystemMetrics(0) / 2) - (height / 2))  # int() = any type to int
        y = int((user.GetSystemMetrics(1) / 2) - (width / 2))   # user32.GetSystemMetrics() = screen size (0 = height and 1 = width)

        # Interface initialization
        self.title('Settings Interface')
        self.geometry(str(height) + "x" + str(width) + "+" + str(x) + "+" + str(y)) # Set window size and position | str() = any type to string
        self.resizable(width=0, height=0)                                           # Prevents any modification of window size
        self.protocol("WM_DELETE_WINDOW", cant_close)                               # Prevents the window from being closed by the red cross
        self.wm_attributes("-topmost", True)                                        # Prioritize the window

        # Variable that stores the default values
        self.line_settings_file = ManipulationSettingsFile() # read the file that contains the parameters
        self.var_list = []

        for i in range(0, self.line_settings_file.get_nb_line()):
            self.var_list.append(tk.StringVar(value= self.line_settings_file.get_line(i)))


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
        exit_button.grid(column= CONSTANT_BUTTON_COLUMN, row= CONSTANT_BUTTON_LINE, **padding)    # Object position

        stop_key_button = ttk.Button(self, text='Change Key', command=self.__change_test_stop_key)
        stop_key_button.grid(column= CONSTANT_BUTTON_COLUMN, row= CONSTANT_STOP_KEY_LINE, **padding)   

        # Label
        # Title
        settings_title_label = ttk.Label(self, text="General Settings")                                             # Creation of the label
        settings_title_label.grid(column= CONSTANT_TITLE_COLUMN, row= CONSTANT_SETTINGS_TITLE_LINE, **padding)    # Object position

        test_title_label = ttk.Label(self, text="Test Settings")              
        test_title_label.grid(column= CONSTANT_TITLE_COLUMN, row= CONSTANT_TEST_TITLE_LINE, **padding)

        # Description
        simu_exe_label = ttk.Label(self, text="simu_exe")              
        simu_exe_label.grid(column= CONSTANT_LABEL_COLUMN, row= CONSTANT_SIMU_EXE_LINE, **padding)

        rc_exe_label = ttk.Label(self, text="rc_exe")              
        rc_exe_label.grid(column= CONSTANT_LABEL_COLUMN, row= CONSTANT_RC_EXE_LINE, **padding)

        simu_path_label = ttk.Label(self, text="simu_path")              
        simu_path_label.grid(column= CONSTANT_LABEL_COLUMN, row= CONSTANT_SIMU_PATH_LINE, **padding)

        rc_path_label = ttk.Label(self, text="rc_path")              
        rc_path_label.grid(column= CONSTANT_LABEL_COLUMN, row= CONSTANT_RC_PATH_LINE, **padding)

        folder_path_label = ttk.Label(self, text="folder_path")              
        folder_path_label.grid(column= CONSTANT_LABEL_COLUMN, row= CONSTANT_FOLDER_PATH_LINE, **padding)

        rc_window_name_label = ttk.Label(self, text="rc window")              
        rc_window_name_label.grid(column= CONSTANT_LABEL_COLUMN, row= CONSTANT_RC_WINDOW_NAME_LINE, **padding)

        stop_key_label = ttk.Label(self, text="stop key")              
        stop_key_label.grid(column= CONSTANT_LABEL_COLUMN, row= CONSTANT_STOP_KEY_LINE, **padding)         

        # Entry 
        simu_exe_entry = ttk.Entry(self, textvariable=self.var_list[0])                                    # Creation of the entry
        simu_exe_entry.grid(column= CONSTANT_ENTRY_COLUMN, row= CONSTANT_SIMU_EXE_LINE, **padding)    # Object position

        rc_exe_entry = ttk.Entry(self, textvariable=self.var_list[1])  
        rc_exe_entry.grid(column= CONSTANT_ENTRY_COLUMN, row= CONSTANT_RC_EXE_LINE, **padding)

        simu_path_entry = ttk.Entry(self, textvariable=self.var_list[2])  
        simu_path_entry.grid(column= CONSTANT_ENTRY_COLUMN, row= CONSTANT_SIMU_PATH_LINE, **padding)

        rc_path_entry = ttk.Entry(self, textvariable=self.var_list[3])  
        rc_path_entry.grid(column= CONSTANT_ENTRY_COLUMN, row= CONSTANT_RC_PATH_LINE, **padding)

        folder_path_entry = ttk.Entry(self, textvariable=self.var_list[4])  
        folder_path_entry.grid(column= CONSTANT_ENTRY_COLUMN, row= CONSTANT_FOLDER_PATH_LINE, **padding)
        folder_path_entry.config(state="disabled")     

        rc_window_name_entry = ttk.Entry(self, textvariable=self.var_list[5])  
        rc_window_name_entry.grid(column= CONSTANT_ENTRY_COLUMN, row= CONSTANT_RC_WINDOW_NAME_LINE, **padding) 

        test_stop_key_entry = ttk.Entry(self, textvariable=self.var_list[6])  
        test_stop_key_entry.grid(column= CONSTANT_ENTRY_COLUMN, row= CONSTANT_STOP_KEY_LINE, **padding)  
        test_stop_key_entry.config(state="disabled")              
        

    def __close_interface(self):
        """ `-`
        `Type:` Procedure
        `Description:` close only the interface and change the value of the settings file
        """

        # Save possible new values
        #self.line_settings_file.manage_file(new_list)

        self.destroy()

    
    def __change_test_stop_key(self):
        """ `-`
        `Type:` Procedure
        `Description:` turns on the interface that changes the test stop button
        """

        self.destroy()
        ck_inter = ChangeKeyInterface()
        ck_inter.mainloop()
        self.__init__()
        self.mainloop()        