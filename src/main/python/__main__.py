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

    tuples = database.get_tuples(
                        "SELECT MAX(wrms.ExpectedCycleTime), (w.NbUnitsToDo div wrm.NbUnitsPerWork) FROM workorders w JOIN workorderrecipemachines wrm ON w.IdWorkOrder = wrm.IdWorkOrder JOIN workorderrecipemachinestages wrms ON wrm.IdWorkOrderRecipeMachine = wrms.IdWorkOrderRecipeMachine WHERE w.Name = ?", 
                        ["all_test_2023-05-09_16h56m19s"]
                    )
    
    tuple_one = tuples[0]
    (test, test2) = tuple_one

    print(tuple_one)
    print(test)
    print(test2)
    print(tuples)

# Execution of the main function
__main()