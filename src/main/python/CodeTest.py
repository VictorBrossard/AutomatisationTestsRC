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

import pyautogui

print(pyautogui.position())
pyautogui.click(1857,295)