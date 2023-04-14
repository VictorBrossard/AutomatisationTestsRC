# Author        : Victor BROSSARD
# Description   : Ouvre simulateur et RC

import PathPopUp
import subprocess
import os

from PathPopUp import *
from tkinter import *

class Init:

    # Constructor
    def __init__(self):
        simuPath = self.simuInit()
        rcPath = self.rcInit()

        try:
            os.chdir(simuPath)
            subprocess.run(['start', 'simulat.exe'], shell=True)
        except Exception as e:
            print("WRONG : ", e)

        try:
            os.chdir(rcPath)
            subprocess.run(['start', 'rc5.exe'], shell=True)
        except Exception as e:
            print("WRONG 2", e)

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