# Author        : Victor BROSSARD
# Description   : Class that allows the creation of the file that contains all the parameters

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
import os

from GraphicInterface.UserEntryPopUp import UserEntryPopUp

from FilesManagement.InitFolder import CONSTANT_SETTINGS_FOLDER_PATH  # path where we store the settings file
from FilesManagement.InitFolder import CONSTANT_INIT_PATH
from FilesManagement.InitFile import InitFile

#-----------------------------------------------------------------------------------------------------
# Initialization of constants
CONSTANT_NAME_SETTINGS_FILE = 'settings.txt'

#-----------------------------------------------------------------------------------------------------

class InitSettingsFile(InitFile):
    """ `+`
    :class:`InitSettingsFile` manages the creation of the file that contains all the parameters
    """
    
    def __init__(self):
        """ `-`
        `Type:` Constructor
        """

        super().__init__()

        # Check if the file exists
        if not os.path.exists(f"{CONSTANT_SETTINGS_FOLDER_PATH}\\{CONSTANT_NAME_SETTINGS_FILE}"):
            # Opening the pop-up that asks the user for the path
            simu_pop_up = UserEntryPopUp("Simulateur", ["Entrez le chemin d'accès au simulateur :"])
            simu_pop_up.mainloop()

            # Opening the pop-up that asks the user for the path
            rc_pop_up = UserEntryPopUp("RC", ["Entrez le chemin d'accès à RC :"])
            rc_pop_up.mainloop()

            settings_list = ["Simulat.exe\n",                               # Simulator software name
                         "rc5.exe\n",                                       # RC software name
                         f"{simu_pop_up.get_user_entries()[0]}\n",          # Simulator Path
                         f"{rc_pop_up.get_user_entries()[0]}\n",            # RC Path
                         f"{CONSTANT_INIT_PATH}\n",                         # Init Folder Path
                         "Menu général\n",                                  # RC window name
                         "tab\n",                                           # Key to end test recording
                         "C:\\EUROPLACER\\ep\\epi\\RCARRETPROPRE.txt\n",    # file that asks you to make a report when you kill RC
                         "C:\\EUROPLACER\\ep\\tmp\n"                        # file where there are traces of RC
                         ]   

            self.create_file(CONSTANT_SETTINGS_FOLDER_PATH, CONSTANT_NAME_SETTINGS_FILE, settings_list)