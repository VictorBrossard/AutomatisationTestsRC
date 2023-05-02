# Author        : Victor BROSSARD
# Description   : Graphical interface that allows you to change the test stop key

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import tkinter as tk
import tkinter.messagebox
import ctypes

from UsefulFunction.UsefulFunction import cant_close

from FilesManagement.ManipulationSettingsFile import ManipulationSettingsFile

from pynput import keyboard
from pynput.keyboard import Key
from pynput.keyboard import KeyCode

from Interaction.InputRecorder import CONSTANT_CANT_USE_THESE_KEYS

#-----------------------------------------------------------------------------------------------------

class ChangeKeyInterface(tk.Tk):
    """ `+`
    :class:`ChangeKeyInterface` allows you to change the test stop key
    """

    def __init__(self):
        """ `-`
        `Type:` Constructor
        """

        super().__init__()

        self.settings_f = ManipulationSettingsFile() # Useful for modifying the settings file

        # Window size and position
        height = 300
        width = 100
        user = ctypes.windll.user32                             # User information
        x = int((user.GetSystemMetrics(0) / 2) - (height / 2))  # int() = any type to int
        y = int((user.GetSystemMetrics(1) / 2) - (width / 2))   # user32.GetSystemMetrics() = screen size (0 = height and 1 = width)

        self.title('Key Interface')
        self.geometry(str(height) + "x" + str(width) + "+" + str(x) + "+" + str(y)) # Set window size and position | str() = any type to string
        self.protocol("WM_DELETE_WINDOW", cant_close)                               # Prevents the window from being closed by the red cross
        self.wm_attributes("-topmost", True)                                        # Prioritize the window

        # Label
        ck_label = tk.Label(self, text='Press a key to change')
        ck_label.pack()

        # Listener
        self.listener = keyboard.Listener(on_press=self.__on_press)
        self.listener.start()
        

    def __on_press(self, key: (Key | KeyCode | None)):
        """ `-`
        `Type:` Procedure
        `Description:` recording of the key pressed
        :param:`key:` keyboard key pressed
        """

        try:
            key_name = key.char
        except AttributeError:
            key_name = key.name
    
        if key_name not in CONSTANT_CANT_USE_THESE_KEYS:
            # Change settings file with new key
            self.settings_f.manage_file(self.settings_f.get_simu_exe(), self.settings_f.get_rc_exe(), self.settings_f.get_simu_path(), 
                                    self.settings_f.get_rc_path(), self.settings_f.get_folder_path(), self.settings_f.get_rc_window_name(), key_name)
            self.listener.stop()
            self.destroy()
        else:
            tkinter.messagebox.showinfo("Cannot choose this key","You cannot choose this key because it is useful for keyboard shortcuts")