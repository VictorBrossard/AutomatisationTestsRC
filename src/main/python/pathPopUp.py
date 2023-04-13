# Author        : Victor BROSSARD
# Description   : Interface graphique du pop-up pour demander le chemin

import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
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

    def implementation(self,fileName):

        # padding
        padding = {'padx': 5, 'pady': 5}

        # Label
        ttk.Label(self, text = "Entrez le chemin "+ fileName +": ").grid(column = 0, row = 0, **padding)

        # Entry 
        text_entry = ttk.Entry(self, textvariable=self.path)
        text_entry.grid(column=1, row=0, **padding)
        text_entry.focus()

        # Button
        ok_button = ttk.Button(self, text='Ok', command=self.execute)
        ok_button.grid(column=2, row=0, **padding)

    def execute(self):
        #self.output_label.config(text=self.path.get())
        self.destroy()

    def getPath(self):
        return self.path.get()
    
def cantClose():
    tkinter.messagebox.showinfo('Fermeture de la fenêtre impossible','Entrez un chemin pour fermer le pop-up.')

#if __name__ == "init":   
popu = PathPopUp("Simulateur")
popu.mainloop()
print(popu.getPath())