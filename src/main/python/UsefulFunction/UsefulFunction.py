# Author        : Victor BROSSARD
# Description   : Useful function that is not part of an object

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import tkinter
import tkinter.messagebox
import ctypes
import sys

#-----------------------------------------------------------------------------------------------------

def cant_close():
    """ `+`
    `Type:` Procedure
    `Description:` returns a pop up to warn that the interface cannot be closed in this way
    """

    tkinter.messagebox.showinfo('Fermeture de la fenêtre impossible','Appuyer sur EXIT pour quitter')


def run_as_admin():
    """ `+`
    `Type:` Procedure
    `Description:` ask for administrator permission if we don't have it and restart the script
    """

    if ctypes.windll.shell32.IsUserAnAdmin():
        return
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        sys.exit(0)


def do_nothing():
    """ `+`
    `Type:` Procedure
    `Description:` do nothing
    """
    pass


def starts_with(chr: str, prefix: str) -> bool:
    """ `+`
    `Type:` Function
    `Description:` returns True if the string 'chr' begins with the string 'prefix', otherwise returns False.
    :param:`chr:` string to check if it starts with the prefix
    :param:`prefix:` string
    """

    return chr[:len(prefix)] == prefix