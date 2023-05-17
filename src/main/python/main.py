# Author        : Victor BROSSARD
# Description   : Main file

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import sys

from GraphicInterface.MainInterface import MainInterface

from FilesManagement.Files.ManageSpecificFiles import ManageSpecificFiles
from FilesManagement.Files.TestPiecesFile import TestPiecesFile

from FilesManagement.Folders.ManageFolders import ManageFolders

from Useful.UsefulFunction import run_as_admin

from Database.Database import Database

#-----------------------------------------------------------------------------------------------------

def main(args):
    """ `-`
    `Type:` Procedure
    `Description:` main function that executes all useful parts of the code
    """

    if args == []:
        run_as_admin()
        ManageFolders().create_soft_folders()
        ManageSpecificFiles().create_soft_settings_file()
        TestPiecesFile()
        database = Database()
        test = MainInterface(database)
        test.mainloop()

    
# Execution of the main function
if __name__ == "__main__":
    args = sys.argv[1:]
    main(args)