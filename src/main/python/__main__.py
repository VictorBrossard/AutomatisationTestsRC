# Author        : Victor BROSSARD
# Description   : Main file

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
from GraphicInterface.MainInterface import MainInterface
from FilesManagement.InitSettingsFile import InitSettingsFile
from FilesManagement.InitFolders import InitFolders
from FilesManagement.InitFolders import CONSTANT_TESTS_FOLDER_PATH
from Interaction.InputRecorder import InputRecorder
from UsefulFunction.UsefulFunction import run_as_admin
from Interaction.ExecuteTest import ExecuteTest
from Interaction.KeyTranslation import KeyTranslation

#-----------------------------------------------------------------------------------------------------

def __main():
    """ `-`
    `Type:` Procedure
    `Description:` main function that executes all useful parts of the code
    """

    run_as_admin()
    InitFolders()
    InitSettingsFile()
    test = MainInterface()
    test.mainloop()


def __test():
    """ `-`
    `Type:` Procedure
    `Description:` procedure to test things
    """

    #InputRecorder("c'est juste un test", CONSTANT_TESTS_FOLDER_PATH).start_record()
    print(KeyTranslation("alt"))

# Execution of the main function
__main()