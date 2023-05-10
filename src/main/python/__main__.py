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
        "SELECT DateCreation FROM workorders WHERE NAME = ?",
        ["test4_2023-05-10_16h35m27s"]
    )

    liste = database.get_tuples(
        "SELECT DateCreation FROM workorders WHERE NAME = ?",
        ["test4_2023-05-10_16h35m27s"]
    )

    print(liste[0][0])

    
# Execution of the main function
__main()