# Author        : Victor BROSSARD
# Description   : Useful function that is not part of an object

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import tkinter
import tkinter.messagebox
import ctypes
import sys
import subprocess

#-----------------------------------------------------------------------------------------------------

def cant_close():
    """ `+`
    `Type:` Procedure
    `Description:` returns a pop up to warn that the interface cannot be closed in this way
    """

    tkinter.messagebox.showinfo("Window cannot be closed","Can't close the window this way")


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


def is_soft_open(soft_name: str) -> bool:
    """ `+`
    `Type:` Function
    `Description:` check that the given software is open
    :param:`soft_name:` name of the software to open (in .exe)
    `Return:` True or False
    """

    # Exécuter la commande tasklist pour obtenir la liste des processus en cours
    process_list = subprocess.check_output('tasklist', shell=True).decode('cp1252').split('\n')

    is_open = False

    # Vérifier si le logiciel "notepad.exe" est dans la liste des processus
    for process in process_list:
        if soft_name in process:
            is_open = True
            break
    
    return is_open


def str_list_to_int_list(str_list: list) -> list:
    """ `+`
    `Type:` Function
    `Description:` transforms a list of strings into a list of integers. Useful to know the number of loops to do on a test
    :param:`str_list:` list of strings to transform
    `Return:` int list
    """

    int_list = []

    # string list walkthrough
    for string in str_list:
        try:
            new_int = int(string)
        except Exception:
            new_int = 1 # if there is an error in the user's input, will play the test at least once

        int_list.append(new_int) # adds to the list

    return int_list