# Author        : Victor BROSSARD
# Description   : 

import Init
import MainInterface
import tkinter
import subprocess
import os

from Init import *
from MainInterface import *
from tkinter import *

CONSTANT_NAME_FILE = 'pathFile.txt'
CONSTANT_PATH_FILE_STORE_PATHS = os.getcwd()

class PathsFile(object):

    # Constructor
    def __init__(self):
        if os.path.exists(CONSTANT_PATH_FILE_STORE_PATHS + '/' + CONSTANT_NAME_FILE):
            self.open_paths_file()
        else:
            self.create_paths_file()

    #
    def create_paths_file(self):
        os.chdir(CONSTANT_PATH_FILE_STORE_PATHS)
        subprocess.run(['type', 'nul', '>', CONSTANT_NAME_FILE], shell=True)

        #
        paths_to_store = InitWithoutPaths()

        #
        os.chdir(CONSTANT_PATH_FILE_STORE_PATHS)
        path_file = open(CONSTANT_NAME_FILE, 'w')
        path_file.write(paths_to_store.get_simu_path() + "\n" + paths_to_store.get_rc_path())
        path_file.close()

    #
    def open_paths_file(self):
        #
        os.chdir(CONSTANT_PATH_FILE_STORE_PATHS)
        path_file = open(CONSTANT_NAME_FILE, 'r')
        simu_path = path_file.readlines()[0].rstrip()
        path_file.close()

        #
        os.chdir(CONSTANT_PATH_FILE_STORE_PATHS)
        path_file = open(CONSTANT_NAME_FILE, 'r')
        rc_path = path_file.readlines()[1].rstrip()
        path_file.close()

        InitWhithPaths(simu_path, rc_path)