# Author        : Victor BROSSARD
# Description   : File that allows the creation or reading of the file that stores the software paths
#                 Useful to avoid giving all the time the paths

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
import subprocess
import os

from GraphicInterface.UserEntryPopUp import UserEntryPopUp
from FilesManagement.InitSoftFolders import CONSTANT_SETTINGS_FOLDER_PATH  # path where we store the settings file
from FilesManagement.InitSoftFolders import CONSTANT_NAME_SETTINGS_FILE
from FilesManagement.InitSoftFolders import CONSTANT_INIT_PATH

#-----------------------------------------------------------------------------------------------------
# Initialization of constants

#-----------------------------------------------------------------------------------------------------

class InitSettingsFile(object):
    """ `+`
    :class:`PathsFile` manages the file that stores the software paths
    """
    
    def __init__(self):
        """ `-`
        `Type:` Constructor
        """

        # Check if the file exists
        if not os.path.exists(CONSTANT_SETTINGS_FOLDER_PATH + '\\' + CONSTANT_NAME_SETTINGS_FILE):
            self.__create_file()

    
    def __create_file(self):
        """ `-`
        `Type:` Procedure
        `Description:` create the file that stores the paths in case it does not exist and opens the programs thanks to these paths
        """

        # Creation of the file 
        os.chdir(CONSTANT_SETTINGS_FOLDER_PATH) # Change the current working directory by giving the path
        subprocess.run(['type', 'nul', '>', CONSTANT_NAME_SETTINGS_FILE], shell=True)

        # Opening the pop-up that asks the user for the path
        simu_pop_up = UserEntryPopUp("Simulator Path", ["Enter the path to access the simulator : "])
        simu_pop_up.mainloop()

        # Opening the pop-up that asks the user for the path
        rc_pop_up = UserEntryPopUp("RC Path", ["Enter the path to access RC : "])
        rc_pop_up.mainloop()

        settings_list = ["Simulat.exe\n",                                   # Simulator software name
                         "rc5.exe\n",                                       # RC software name
                         f"{simu_pop_up.get_user_entry()}\n",               # Simulator Path
                         f"{rc_pop_up.get_user_entry()}\n",                 # RC Path
                         f"{CONSTANT_INIT_PATH}\n",                         # Init Folder Path
                         "Menu général\n",                                  # RC window name
                         "tab\n",                                           # Key to end test recording
                         "C:\\EUROPLACER\\ep\\epi\\RCARRETPROPRE.txt\n",    # file that asks you to make a report when you kill RC
                         "C:\\EUROPLACER\\ep\\tmp\n"                        # file where there are traces of RC
                         ]                        

        # Save the values in the file we have created
        os.chdir(CONSTANT_SETTINGS_FOLDER_PATH)
        file_path = open(CONSTANT_NAME_SETTINGS_FILE, 'w')              # Opening the file in write mode ('w')

        for setting in settings_list:
            file_path.write(setting)

        file_path.close()