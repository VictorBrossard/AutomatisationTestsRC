# Author        : Victor BROSSARD
# Description   : Ouvre simulateur et RC

import PathPopUp
import subprocess
import os
import tkinter.messagebox

from PathPopUp import *
from tkinter import *

class Init(object):

    # Constructor
    def __init__(self):
        self.simu_path = ""
        self.rc_path = ""
        
    #
    def simu_init(self):
        simu_pop_up = PathPopUp("Simulateur")
        simu_pop_up.mainloop()
        return simu_pop_up.get_path()
    
    #
    def rc_init(self):
        rc_pop_up = PathPopUp("RC")
        rc_pop_up.mainloop()
        return rc_pop_up.get_path()
    
    #
    def start_simu(self):
        try:
            os.chdir(self.simu_path)
            subprocess.run(['start', 'simulat.exe'], shell=True)
        except Exception as e:
            tkinter.messagebox.showinfo('ERROR chemin Simulateur',e)

    #
    def start_rc(self):
        try:
            os.chdir(self.rc_path)
            subprocess.run(['start', 'rc5.exe'], shell=True)
        except Exception as e:
            tkinter.messagebox.showinfo('ERROR chemin RC',e)

    #
    def get_simu_path(self):
        return self.simu_path
    
    #
    def get_rc_path(self):
        return self.rc_path
    
class InitWhithPaths(Init):

    # Constructor
    def __init__(self, simu_way, rc_way):
        Init.__init__(self)

        self.simu_path = simu_way
        self.rc_path = rc_way
        
        self.start_simu()
        self.start_rc()

class InitWithoutPaths(Init):

    # Constructor
    def __init__(self):
        Init.__init__(self)

        self.simu_path = self.simu_init()
        self.rc_path = self.rc_init()
        
        self.start_simu()
        self.start_rc()