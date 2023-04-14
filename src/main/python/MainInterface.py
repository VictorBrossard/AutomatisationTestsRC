# Author        : Victor BROSSARD
# Description   : Interface graphique général du projet

import tkinter as tk
import tkinter.messagebox
import subprocess

from tkinter import *
from tkinter import ttk
from Init import *

class MainInterface(tk.Tk):
    
    # Constructor
    def __init__(self):
        super().__init__()

        self.title('Interface Principale')
        self.geometry("400x100")
        self.resizable(width=0, height=0)
        self.protocol("WM_DELETE_WINDOW", cantClose)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.implementation()

    def implementation(self):

        # Padding
        padding = {'padx': 5, 'pady': 5}

        # Button
        exitButton = ttk.Button(self, text='EXIT', command=self.execute)
        exitButton.grid(column=1, row=1, **padding)

    #
    def execute(self):
        #try:
        #    subprocess.run(['taskkill', '/f', '/im', 'rc5.exe'], shell=True)
        #except Exception as e:
        #    print(e)

        try:
            subprocess.run(['taskkill', '/f', '/im', 'simulat.exe'], shell=True)
        except Exception as e:
            print(e)

        self.destroy()


def cantClose():
    tkinter.messagebox.showinfo('Fermeture de la fenêtre impossible','Appuyer sur EXIT pour quitter')