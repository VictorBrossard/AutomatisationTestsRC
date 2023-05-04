# Author        : Victor BROSSARD
# Description   : Main file

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
from GraphicInterface.MainInterface import MainInterface
from GraphicInterface.MessageBox import MessageBox

from FilesManagement.Files.ManageFiles import ManageFiles
from FilesManagement.Folders.ManageFolders import ManageFolders
from FilesManagement.Files.TestPiecesFile import TestPiecesFile

from UsefulFunction.UsefulFunction import run_as_admin

#-----------------------------------------------------------------------------------------------------

def __main():
    """ `-`
    `Type:` Procedure
    `Description:` main function that executes all useful parts of the code
    """

    run_as_admin()
    ManageFolders().create_soft_folders()
    ManageFiles().create_settings_file()
    TestPiecesFile()
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