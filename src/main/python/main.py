# Author        : Victor BROSSARD
# Description   : Main file

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import sys

from GraphicInterface.MainInterface import MainInterface

from FilesManagement.Files.ManageSpecificFiles import ManageSpecificFiles
from FilesManagement.Files.TestPiecesFile import TestPiecesFile

from FilesManagement.Folders.ManageFolders import ManageFolders

from Interaction.Command import Command

#-----------------------------------------------------------------------------------------------------

def main(args):
    """ `-`
    `Type:` Procedure
    `Description:` main function that executes all useful parts of the code
    """

    ManageFolders().create_soft_folders()
    ManageSpecificFiles().create_soft_settings_file()
    TestPiecesFile()

    if args == []:
        test = MainInterface()
        test.mainloop()
    else:
        Command().translations_args(args)

    
# Execution of the main function
if __name__ == "__main__":
    args = sys.argv[1:]
    main(args)