# Author        : Victor BROSSARD
# Description   : Useful function that is not part of an object

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import subprocess
import os

from GraphicInterface.MessageBox import MessageBox

from FilesManagement.Files.ManipulationSettingsFile import ManipulationSettingsFile

#-----------------------------------------------------------------------------------------------------

def cant_close():
    """ `+`
    `Type:` Procedure
    `Description:` returns a pop up to warn that the interface cannot be closed in this way
    """

    MessageBox("Fenêtre", "[INFO] Vous ne pouvez pas fermer la fenêtre de cette façon.").mainloop()


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


def validate_int(value: str) -> bool:
    """ `+`
    `Type:` Function
    `Description:` checks if the input value is an int
    :param:`value:` string to check
    `Return:` bool
    """

    if value == "":
        return True
    try:
        int(value)
        return True
    except ValueError:
        return False


def get_program_list() -> list[str]:
    """ `+`
    `Type:` Function
    `Description:` will fetch the list of programs locally
    `Return:` list of programs
    """

    # path of the folder where the programs are
    folder_path = ManipulationSettingsFile().get_line(8)
    files_with_dp_extension = []

    # recovery of the list of program names 
    for file_name_with_extension in os.listdir(folder_path):
        if file_name_with_extension.endswith(".dp"):
            file_name, _ = os.path.splitext(os.path.basename(file_name_with_extension))
            files_with_dp_extension.append(file_name)

    return files_with_dp_extension