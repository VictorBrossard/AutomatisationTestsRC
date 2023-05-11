# Author        : Victor BROSSARD
# Description   : Main file

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
from GraphicInterface.MainInterface import MainInterface

from FilesManagement.Files.ManageSpecificFiles import ManageSpecificFiles
from FilesManagement.Files.TestPiecesFile import TestPiecesFile

from FilesManagement.Folders.ManageFolders import ManageFolders

from UsefulFunction.UsefulFunction import run_as_admin

from Database.Database import Database
from FilesManagement.Files.ManageReportFile import ManageReportFile

#-----------------------------------------------------------------------------------------------------

def __main():
    """ `-`
    `Type:` Procedure
    `Description:` main function that executes all useful parts of the code
    """

    run_as_admin()
    ManageFolders().create_soft_folders()
    ManageSpecificFiles().create_soft_settings_file()
    TestPiecesFile()
    database = Database()
    test = MainInterface(database)
    test.mainloop()


def __test():
    """ `-`
    `Type:` Procedure
    `Description:` procedure to test things
    """

    database = Database()

    database.test_execution(
        "SELECT w.DateBegin, w.DateEnd FROM (workorders wo JOIN workorderrecipemachines worm ON wo.IdWorkOrder = worm.IdWorkOrder) JOIN works w ON worm.IdWorkOrderRecipeMachine = w.IdWorkOrderRecipeMachine WHERE wo.Name = ?",
        ["2_cartes_2023-05-11_12h32m31s"]
    )


    
# Execution of the main function
__main()