# Author        : Victor BROSSARD
# Description   : Graphical interface that asks a question that can be answered with yes or no

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
import tkinter as tk
import ctypes

from tkinter import ttk
from UsefulFunction.UsefulFunction import cant_close

#-----------------------------------------------------------------------------------------------------

class SimpleQuestionInterface(tk.Tk):
    """ `+`
    :class:`SimpleQuestionInterface` asks a question that can be answered with yes or no
    """

    def __init__(self, name: str, question: str):
        """ `-`
        `Type:` Constructor
        :param:`name:` window name
        :param:`question:` question we want to ask the user
        """

        # Parent constructor
        super().__init__()

        self.is_yes = False # variable that lets you know the user's answer

        # Window size and position
        height = 300
        width = 100
        user32 = ctypes.windll.user32                               # User information
        x = int((user32.GetSystemMetrics(0) / 2) - (height / 2))    # int() = any type to int
        y = int((user32.GetSystemMetrics(1) / 2) - (width / 2))     # user32.GetSystemMetrics() = screen size (0 = height and 1 = width)

        # Interface initialization
        self.title(name)
        self.geometry(str(height) + "x" + str(width) + "+" + str(x) + "+" + str(y))     # Set window size and position | str() = type to string
        self.resizable(width=0, height=0)                                               # Prevents any modification of window size
        self.protocol("WM_DELETE_WINDOW", cant_close)                                   # Prevents the window from being closed by the red cross

        self.__implementation(question)

    
    def __implementation(self, question: str):
        """ `-`
        `Type:` Procedure
        `Description:` adds interface objects to the interface
        :param:`question:` question we want to ask the user
        """

        # Label
        question_label = ttk.Label(self, text=question)
        question_label.pack(side=tk.TOP, pady=10)

        # Frame
        button_frame = tk.Frame(self)
        button_frame.pack(side=tk.TOP)  

        # Button
        yes_button = ttk.Button(button_frame, text="Yes", command=lambda: self.__answer("yes"))
        yes_button.pack(side=tk.LEFT, padx=10)

        no_button = ttk.Button(button_frame, text="No", command=lambda: self.__answer("no"))    
        no_button.pack(side=tk.LEFT, padx=10)


    def __answer(self, answer: str):
        """ `-`
        `Type:` Procedure
        `Description:` changes the value of the is_yes variable depending on the user's answer
        :param:`answer:` user's answer
        """

        if answer == "yes":
            self.is_yes = True
        
        self.destroy()


    def get_is_yes(self):
        """ `+`
        `Type:` Function
        `Description:` getter that returns the variable is_yes
        `Return:` is_yes (Boolean)
        """

        return self.is_yes