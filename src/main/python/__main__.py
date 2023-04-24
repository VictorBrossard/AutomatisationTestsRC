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
    test = ManipulationSettingsFile()
    print(test.get_simu_exe())
    print(test.get_rc_exe())
    print(test.get_simu_path())
    print(test.get_rc_path())
    print(test.get_folder_path())
    print(test.get_rc_window_name())
    print(test.get_test_stop_key())

    

# Execution of the main function
__main()