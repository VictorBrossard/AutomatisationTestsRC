# Author        : Victor BROSSARD
# Description   : Main file

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import subprocess
import os
import ctypes
import sys

from Interface.MainInterface import MainInterface
from FilesManagement.PathsFile import PathsFile
from FilesManagement.InitFolders import InitFolders

from FilesManagement.InitFolders import CONSTANT_TESTS_FOLDER_PATH
from Interaction.InputRecorder import InputRecorder

#-----------------------------------------------------------------------------------------------------

def run_as_admin():
    ######Demande une autorisation d'administrateur et redémarre le script.
    if ctypes.windll.shell32.IsUserAnAdmin():
        return
    else:
        ######## Redémarre le script avec des droits d'administrateur
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        sys.exit(0)

#-----------------------------------------------------------------------------------------------------
# Main function that executes all useful parts of the code
def main():
    run_as_admin()
    InitFolders()
    PathsFile()
    test = MainInterface()
    test.mainloop()

def test():
    InputRecorder("lol", CONSTANT_TESTS_FOLDER_PATH).start_record()

# Execution of the main function
test()