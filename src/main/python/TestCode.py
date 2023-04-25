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

# créer la fenêtre
window = tk.Tk()

# créer une liste des options
options = ['option 1', 'option 2', 'option 3', 'option 4']

# créer un dictionnaire pour stocker l'état des Checkbuttons
option_vars = {}

# créer une fonction pour mettre à jour le dictionnaire des états
def update_option_vars(option):
    option_vars[option].set(not option_vars[option].get())

# créer une fonction pour afficher les options sélectionnées
def show_selected_options():
    selected_options = [option for option, var in option_vars.items() if var.get()]
    print("Options sélectionnées : ", selected_options)

# créer une combobox personnalisée
def open_dropdown():
    # créer une fenêtre de liste déroulante
    dropdown = tk.Toplevel()
    
    # ajouter un Checkbutton pour chaque option
    for option in options:
        option_vars[option] = tk.BooleanVar()
        checkbutton = tk.Checkbutton(dropdown, text=option, variable=option_vars[option], command=lambda option=option: update_option_vars(option))
        checkbutton.pack()

    # ajouter un bouton pour fermer la fenêtre de liste déroulante et afficher les options sélectionnées
    close_button = tk.Button(dropdown, text="Fermer", command=lambda: [dropdown.destroy(), show_selected_options()])
    close_button.pack()

# créer une combobox personnalisée
combo = ttk.Combobox(window, state="readonly")
combo["values"] = ["Sélectionner des options..."]
combo.pack()
combo.bind("<Button-1>", lambda event: open_dropdown())

# afficher la fenêtre
window.mainloop()



