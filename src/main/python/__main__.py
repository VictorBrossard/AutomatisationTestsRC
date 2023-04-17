# Author        : Victor BROSSARD
# Description   : Classe principal

import Init
import MainInterface
import tkinter
import subprocess
import os
import PathsFile

from Init import *
from MainInterface import *
from tkinter import *
from PathsFile import *

def main():
    PathsFile()
    test = MainInterface()
    test.mainloop()

main()