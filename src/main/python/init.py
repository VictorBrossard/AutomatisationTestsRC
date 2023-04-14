# Author        : Victor BROSSARD
# Description   : Ouvre simulateur et RC

import PathPopUp
import subprocess
import os
import tkinter.messagebox

from PathPopUp import *
from tkinter import *

class Init:

    # Constructor
    def __init__(self):
        self.simuPath = self.simuInit()
        self.rcPath = self.rcInit()

        self.startSimu()
        self.startRC()
        
    #
    def simuInit(self):
        simuPopUp = PathPopUp("Simulateur")
        simuPopUp.mainloop()
        return simuPopUp.getPath()
    
    #
    def rcInit(self):
        rcPopUp = PathPopUp("RC")
        rcPopUp.mainloop()
        return rcPopUp.getPath()
    
    #
    def startSimu(self):
        try:
            os.chdir(self.simuPath)
            subprocess.run(['start', 'simulat.exe'], shell=True)
        except Exception as e:
            tkinter.messagebox.showinfo('ERROR chemin Simulateur',e)

    #
    def startRC(self):
        try:
            os.chdir(self.rcPath)
            subprocess.run(['start', 'rc5.exe'], shell=True)
        except Exception as e:
            tkinter.messagebox.showinfo('ERROR chemin RC',e)

    #
    def getSimuPath(self):
        return self.simuPath
    
    #
    def getRCPath(self):
        return self.rcPath
        