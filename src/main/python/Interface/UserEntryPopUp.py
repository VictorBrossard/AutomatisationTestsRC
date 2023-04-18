# Author        : Victor BROSSARD
# Description   : GUI pop-up to request path

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
import tkinter as tk
import tkinter.messagebox
import ctypes

from tkinter import ttk

#-----------------------------------------------------------------------------------------------------
# Class that handles software path pop-ups
class UserEntryPopUp(tk.Tk):

    # Constructor
    def __init__(self, name, desc):
        # Parent constructor
        super().__init__()

        # Window size and position
        height = 500
        width = 125
        user32 = ctypes.windll.user32                               # User information
        x = int((user32.GetSystemMetrics(0) / 2) - (height / 2))    # int() = any type to int
        y = int((user32.GetSystemMetrics(1) / 2) - (width / 2))     # user32.GetSystemMetrics() = screen size (0 = height and 1 = width)

        # Interface initialization
        self.title(name)
        self.geometry(str(height) + "x" + str(width) + "+" + str(x) + "+" + str(y))     # Set window size and position | str() = type to string
        self.resizable(width=0, height=0)                                               # Prevents any modification of window size
        self.protocol("WM_DELETE_WINDOW", cant_close)                                   # Prevents the window from being closed by the red cross

        # Variable that stores the path given by the user
        self.user_entry = tk.StringVar()

        # Configuring the placement of interface objects
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        # Adds interface objects to the interface
        self.implementation(desc)

    # Function that adds interface objects to the interface
    def implementation(self, desc):

        # Padding
        padding = {'padx': 5, 'pady': 5}

        # Label
        text_label = ttk.Label(self, text=desc)                 # Creation of the label
        text_label.grid(column = 1, row = 0, **padding)         # Object position

        # Entry 
        text_entry = ttk.Entry(self, textvariable=self.user_entry)  # Creation of the entry
        text_entry.grid(column=1, row=1, **padding)                 # Object position
        text_entry.focus_set()                                      # Set focus to text input

        # Button
        ok_button = ttk.Button(self, text='OK', command=self.close_pop_up)  # Creation of the button
        ok_button.grid(column=1, row=2, **padding)                          # Object position

    # Function that closes the interface
    def close_pop_up(self):
        self.destroy()

    # Function that returns the variable path
    def get_user_entry(self):
        return self.user_entry.get()
    
#-----------------------------------------------------------------------------------------------------
# Function that returns a pop up to warn that the interface cannot be closed in this way
def cant_close():
    tkinter.messagebox.showinfo('Fermeture de la fenêtre impossible','Entrez un chemin pour fermer le pop-up.')
