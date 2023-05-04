# Author        : Victor BROSSARD
# Description   : Main file

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
from GraphicInterface.MainInterface import MainInterface
from GraphicInterface.MessageBox import MessageBox

from FilesManagement.InitSettingsFile import InitSettingsFile
from FilesManagement.InitSoftFolders import InitSoftFolders
from FilesManagement.TestFiles.TestPieces import TestPieces

from UsefulFunction.UsefulFunction import run_as_admin

import tkinter.messagebox
#-----------------------------------------------------------------------------------------------------

def __main():
    """ `-`
    `Type:` Procedure
    `Description:` main function that executes all useful parts of the code
    """

    run_as_admin()
    InitSoftFolders()
    InitSettingsFile()
    TestPieces()
    test = MainInterface()
    test.mainloop()


def __test():
    """ `-`
    `Type:` Procedure
    `Description:` procedure to test things
    """

    MessageBox("test", "test").mainloop()
    

# Execution of the main function
__main()