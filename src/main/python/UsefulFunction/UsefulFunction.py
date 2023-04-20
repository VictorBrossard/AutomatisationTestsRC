# Author        : Victor BROSSARD
# Description   : GUI pop-up to request path

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import tkinter
import tkinter.messagebox
import ctypes
import sys

#-----------------------------------------------------------------------------------------------------
# Function that returns a pop up to warn that the interface cannot be closed in this way
def cant_close():
    tkinter.messagebox.showinfo('Fermeture de la fenêtre impossible','Appuyer sur EXIT pour quitter')

#
def run_as_admin():
    ######Demande une autorisation d'administrateur et redémarre le script.
    if ctypes.windll.shell32.IsUserAnAdmin():
        return
    else:
        ######## Redémarre le script avec des droits d'administrateur
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        sys.exit(0)

def do_nothing():
    """
    Cette fonction ne fait rien
    """
    pass

def starts_with(chr, prefix):
        """
        Renvoie True si la chaîne de caractères 'string' commence par la chaîne de caractères 'prefix',
        sinon renvoie False.
        """
        return chr[:len(prefix)] == prefix