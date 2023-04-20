"""
import tkinter as tk

# Créer la fenêtre principale
root = tk.Tk()

# Créer la fonction qui sera appelée lorsque l'utilisateur sélectionne une option du menu déroulant
def on_select(option):
    print("Option sélectionnée :", option)

# Créer les options du menu déroulant
options = ["Option 1", "Option 2", "Option 3"]

# Créer la variable pour stocker l'option sélectionnée par l'utilisateur
selected_option = tk.StringVar(root)
selected_option.set(options[0])

# Créer le menu déroulant
dropdown = tk.OptionMenu(root, selected_option, *options, command=on_select)
dropdown.pack()

# Afficher la fenêtre
root.mainloop()
"""
import tkinter as tk
from tkinter import ttk

# Créer la fenêtre principale
root = tk.Tk()

# Créer la fonction qui sera appelée lorsque l'utilisateur sélectionne une option du menu déroulant
def on_select(event):
    print("Option sélectionnée :", combo.get())

# Créer les options du menu déroulant
options = ["Option 1", "Option 2", "Option 3"]

# Créer le menu déroulant
combo = ttk.Combobox(root, values=options, state="readonly")
combo.current(0)
combo.bind("<<ComboboxSelected>>", on_select)
combo.pack()

# Afficher la fenêtre
root.mainloop()

