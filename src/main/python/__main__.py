# Author        : Victor BROSSARD
# Description   : Main file

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
from GraphicInterface.MainInterface import MainInterface
from FilesManagement.InitSettingsFile import InitSettingsFile
from FilesManagement.InitFolders import InitFolders
from OpenSoftwares.OpenSoftwares import OpenSoftwares
from UsefulFunction.UsefulFunction import run_as_admin

from FilesManagement.ManipulationSettingsFile import ManipulationSettingsFile
from UsefulFunction.UsefulFunction import str_list_to_int_list
from Interaction.Interaction import Interaction

#-----------------------------------------------------------------------------------------------------

def __main():
    """ `-`
    `Type:` Procedure
    `Description:` main function that executes all useful parts of the code
    """

    run_as_admin()
    InitFolders()
    InitSettingsFile()
    OpenSoftwares().open_soft()
    test = MainInterface()
    test.mainloop()


def __test():
    """ `-`
    `Type:` Procedure
    `Description:` procedure to test things
    """
    
    Interaction().write_test()
    

# Execution of the main function
__main()