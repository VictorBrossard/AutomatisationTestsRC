# Author        : Victor BROSSARD
# Description   : Main file

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
from GraphicInterface.MainInterface import MainInterface
from FilesManagement.PathsFile import PathsFile
from FilesManagement.InitFolders import InitFolders
from FilesManagement.InitFolders import CONSTANT_TESTS_FOLDER_PATH
from Interaction.InputRecorder import InputRecorder
from UsefulFunction.UsefulFunction import run_as_admin
from Interaction.TestsReading import TestReading

#-----------------------------------------------------------------------------------------------------
# Main function that executes all useful parts of the code
def __main():
    run_as_admin()
    InitFolders()
    PathsFile()
    test = MainInterface()
    test.mainloop()

def __test():
    #InputRecorder("c'est juste un test", CONSTANT_TESTS_FOLDER_PATH).start_record()
    TestReading().read_test_file("c'est juste un test")

# Execution of the main function
__main()