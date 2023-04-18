# Author        : Victor BROSSARD
# Description   : Main file

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import subprocess
import os
import PathsFile

from Interface.MainInterface import MainInterface
from PathsFile.PathsFile import PathsFile

#-----------------------------------------------------------------------------------------------------
# Main function that executes all useful parts of the code
def main():
    PathsFile()
    test = MainInterface()
    test.mainloop()

# Execution of the main function
main()