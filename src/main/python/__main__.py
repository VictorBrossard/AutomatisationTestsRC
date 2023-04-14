# Author        : Victor BROSSARD
# Description   : Classe principal

import Init
import MainInterface
import tkinter
import subprocess
import os

from Init import *
from MainInterface import *
from tkinter import *

def createPathFile():
    pathFileStorePaths = os.getcwd()

    if os.path.exists(pathFileStorePaths + '/pathFile.txt'):
        pass
    else:
        os.chdir(pathFileStorePaths)
        subprocess.run(['type', 'nul', '>' ,'pathFile.txt'], shell=True)
        pathsToStore = Init()

        #
        os.chdir(pathFileStorePaths)
        subprocess.run(['echo', pathsToStore.getSimuPath(), '>' ,'pathFile.txt'], shell=True)

        #
        os.chdir(pathFileStorePaths)
        subprocess.run(['echo', pathsToStore.getRCPath(), '>' ,'pathFile.txt'], shell=True)

def main():
    createPathFile()
    test = MainInterface()
    test.mainloop()

main()