# Author        : Victor BROSSARD
# Description   : Class that creates an interface that displays a message to the user

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
import tkinter as tk
import ctypes

from tkinter import ttk

#-----------------------------------------------------------------------------------------------------

class MessageBox(tk.Tk):
    """ `+`
    :class:`MessageBox` creates an interface that displays a message to the user
    """

    def __init__(self, name: str, msg: str):
        """ `-`
        `Type:` Constructor
        :param:`name:` window name
        :param:`msg:` message to be displayed to the user
        """

        # Parent constructor
        super().__init__()

        # Interface initialization
        self.title(name)
        self.wm_attributes("-topmost", True) # Prioritize the window

        self.__implementation(msg)

    
    def __implementation(self, msg: str):
        """ `-`
        `Type:` Procedure
        `Description:` adds interface objects to the interface
        :param:`msg:` message to be displayed to the user
        """

        # Label
        question_label = ttk.Label(self, text=msg)
        question_label.pack(side=tk.TOP, pady=10)

        # Button
        ok_button = ttk.Button(self, text="OK", command=self.__close)
        ok_button.pack(side=tk.TOP, padx=10)

        self.__init_size(msg)

    
    def __init_size(self, msg: str):
        """ `-`
        `Type:` Procedure
        `Description:` manages the size of the interface according to the size of the message
        :param:`msg:` message to be displayed to the user
        """

        string_length = len(msg)

        # Window size and position
        height = string_length * 5 + 200
        width = 100
        user32 = ctypes.windll.user32                               # User information
        x = int((user32.GetSystemMetrics(0) / 2) - (height / 2))    # int() = any type to int
        y = int((user32.GetSystemMetrics(1) / 2) - (width / 2))     # user32.GetSystemMetrics() = screen size (0 = height and 1 = width)

        self.geometry(str(height) + "x" + str(width) + "+" + str(x) + "+" + str(y))     # Set window size and position | str() = type to string
        self.resizable(width=0, height=0)                                               # Prevents any modification of window size


    def __close(self):
        """ `-`
        `Type:` Procedure
        `Description:` close the interface
        """
        
        self.destroy()
