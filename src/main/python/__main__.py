# Author        : Victor BROSSARD
# Description   : Main file

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
from GraphicInterface.MainInterface import MainInterface
from FilesManagement.InitSettingsFile import InitSettingsFile
from FilesManagement.InitSoftFolders import InitSoftFolders
from UsefulFunction.UsefulFunction import run_as_admin
from RCTest.Precondition import Precondition

from FilesManagement.InitTestReportFolder import InitTestReportFolder

#-----------------------------------------------------------------------------------------------------

def __main():
    """ `-`
    `Type:` Procedure
    `Description:` main function that executes all useful parts of the code
    """

    run_as_admin()
    InitSoftFolders()
    InitSettingsFile()
    Precondition().start_precondition()
    test = MainInterface()
    test.mainloop()


def __test():
    """ `-`
    `Type:` Procedure
    `Description:` procedure to test things
    """
    
    InitTestReportFolder("test_1")
    

# Execution of the main function
__main()