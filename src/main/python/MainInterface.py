# Author        : Victor BROSSARD
# Description   : Interface graphique général du projet

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
import tkinter as tk
import tkinter.messagebox
import subprocess
import ctypes

from tkinter import ttk

#-----------------------------------------------------------------------------------------------------
# Class that manages the main interface
class MainInterface(tk.Tk):
    
    # Constructor
    def __init__(self):
        # Parent constructor
        super().__init__()

        # Window size and position
        height = 400
        width = 100
        user = ctypes.windll.user32                             # User information
        x = int((user.GetSystemMetrics(0) / 2) - (height / 2))  # int() = any type to int
        y = int((user.GetSystemMetrics(1) / 2) - (width / 2))   # user32.GetSystemMetrics() = screen size (0 = height and 1 = width)

        # Interface initialization
        self.title('Interface Principale')
        self.geometry(str(height) + "x" + str(width) + "+" + str(x) + "+" + str(y)) # Set window size and position | str() = any type to string
        self.resizable(width=0, height=0)                                           # Prevents any modification of window size
        self.protocol("WM_DELETE_WINDOW", cant_close)                               # Prevents the window from being closed by the red cross

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
        exit_button.grid(column=1, row=1, **padding)                                # Object position

    # Function that closes software and the interface
    def close_softwares(self):
        # Close software
        #try:
        #    subprocess.run(['taskkill', '/f', '/im', 'rc5.exe'], shell=True)
        #except Exception as e:
        #    pass

        try:
            subprocess.run(['taskkill', '/f', '/im', 'simulat.exe'], shell=True)
        except Exception:
            pass

        # Close interface
        self.destroy()

#-----------------------------------------------------------------------------------------------------
# Function that returns a pop up to warn that the interface cannot be closed in this way
def cant_close():
    tkinter.messagebox.showinfo('Fermeture de la fenêtre impossible','Appuyer sur EXIT pour quitter')