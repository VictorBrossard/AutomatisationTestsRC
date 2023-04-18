# Author        : Victor BROSSARD
# Description   : Main file

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import subprocess
import os

from Interface.MainInterface import MainInterface
from FilesManagement.PathsFile import PathsFile
from FilesManagement.InitFolders import InitFolders

#-----------------------------------------------------------------------------------------------------
# Main function that executes all useful parts of the code
def main():
    InitFolders()
    PathsFile()
    test = MainInterface()
    test.mainloop()

# Execution of the main function
main()