# Author        : Victor BROSSARD
# Description   : Interface graphique du pop-up pour demander le chemin

import tkinter as tk
import tkinter.messagebox

from tkinter import ttk
from tkinter import *

class PathPopUp(tk.Tk):

    # Constructor
    def __init__(self, name):
        super().__init__()

        self.title('Chemin ' + name)
        self.geometry("400x50")
        self.resizable(width=0, height=0)
        self.protocol("WM_DELETE_WINDOW", cantClose)

        self.path = tk.StringVar()

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.implementation(name)

    #
    def implementation(self,fileName):

        # Padding
        padding = {'padx': 5, 'pady': 5}

        # Label
        ttk.Label(self, text = "Entrez le chemin "+ fileName +": ").grid(column = 0, row = 0, **padding)

        # Entry 
        textEntry = ttk.Entry(self, textvariable=self.path)
        textEntry.grid(column=1, row=0, **padding)
        textEntry.focus()

        # Button
        okButton = ttk.Button(self, text='Ok', command=self.execute)
        okButton.grid(column=2, row=0, **padding)

    #
    def execute(self):
        self.destroy()

    #
    def getPath(self):
        return self.path.get()
    
def cantClose():
    tkinter.messagebox.showinfo('Fermeture de la fenêtre impossible','Entrez un chemin pour fermer le pop-up.')
