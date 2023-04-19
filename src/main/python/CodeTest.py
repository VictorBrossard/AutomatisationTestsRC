"""import tkinter as tk

from tkinter import *
 
def quitter():
    fen = Toplevel(root)
    fen.grab_set()
    fen.focus_set()
    b = Button(fen, text = "Ok", command = root.quit).pack()
 
root = Tk()
root.geometry("400x100")
bouton = Button(root, text = "quitter", command=quitter).pack()
root.mainloop()

OptionList = [
"Aries",
"Taurus",
"Gemini",
"Cancer"
] 

app = tk.Tk()

app.geometry('100x200')

variable = tk.StringVar(app)
variable.set(OptionList[0])

opt = tk.OptionMenu(app, variable, *OptionList)
opt.config(width=90, font=('Helvetica', 12))
opt.pack()

app.mainloop()"""

import tkinter as tk
from Interaction.InputRecorder import InputRecorder
from FilesManagement.InitFolders import CONSTANT_TESTS_FOLDER_PATH

# Fonction appelée lorsque le bouton est cliqué

def ouvrir_fenetre():
    def fermer_fenetre():
        fenetre_enfant.destroy()

    def autre():
        InputRecorder("test225258858528", CONSTANT_TESTS_FOLDER_PATH).start_record()

    # Création de la fenêtre enfant
    fenetre_enfant = tk.Toplevel(fenetre_principale)

    # Ajout d'un bouton pour fermer la fenêtre enfant
    bouton_fermer = tk.Button(fenetre_enfant, text="Fermer", command=fermer_fenetre)
    bouton_fermer.pack()

    bouton_ferm = tk.Button(fenetre_enfant, text="dab", command=autre)
    bouton_ferm.pack()



# Création de la fenêtre principale
fenetre_principale = tk.Tk()

bouton_fermer = tk.Button(fenetre_principale, text="Ouvre", command=ouvrir_fenetre)
bouton_fermer.pack()

# Affichage des fenêtres
fenetre_principale.mainloop()
