# Author        : Victor BROSSARD
# Description   : Class that allows the creation of any file

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
import subprocess
import os

from FilesManagement.Folders.ManageFolders import CONSTANT_SETTINGS_FOLDER_PATH  # path where we store the settings file
from FilesManagement.Folders.ManageFolders import CONSTANT_INIT_PATH

from GraphicInterface.UserEntryPopUp import UserEntryPopUp

#-----------------------------------------------------------------------------------------------------
# Initialization of constants
CONSTANT_NAME_SETTINGS_FILE = 'settings.txt'

#-----------------------------------------------------------------------------------------------------

class ManageFiles(object):
    """ `+`
    :class:`ManageFiles` manage the creation of any file
    """
    
    def __init__(self):
        """ `-`
        `Type:` Constructor
        """

        pass


    def create_file(self, path: str, file_name: str, line_list: list):
        """ `+`
        `Type:` Procedure
        `Description:` creates a txt file
        :param:`path:` path where you save the file
        :param:`file_name:` file name
        :param:`line_list:` line to write in the file
        """

        if os.path.exists(f"{path}\\{file_name}"):
            return

        # Creation of the file 
        os.chdir(path) # Change the current working directory by giving the path
        subprocess.run(['type', 'nul', '>', file_name], shell=True)                     

        # Save the values in the file we have created
        os.chdir(path)
        file_path = open(file_name, 'w') # Opening the file in write mode ('w')

        if line_list != []:
            for line in line_list:
                file_path.write(f"{line}\n")

        file_path.close()


    def create_executing_file(self, path: str, file_name: str, str_to_transform: str):
        """ `+`
        `Type:` Porcedure
        `Description:`
        :param:`path:` folder where we will store the file
        :param:`file_name:` name of the file you are creating
        :param:`str_to_transform:` string to transform into a file InputRecorder
        """

        file_line_list = []
        tme = 0.000

        # creation of the instruction list
        for chr in str_to_transform:
            file_line_list.append(f"Key;{chr};{tme}")
            tme = tme + 0.001

        if os.path.exists(f"{path}\\{file_name}"):
            os.remove(f"{path}\\{file_name}")

        # file creation
        self.create_file(path, file_name, file_line_list)


    def create_settings_soft_file(self):
        """ `+`
        `Type:` Procedure
        `Description:` create the file that contains all the parameters
        """

        # Check if the file exists
        if not os.path.exists(f"{CONSTANT_SETTINGS_FOLDER_PATH}\\{CONSTANT_NAME_SETTINGS_FILE}"):
            # Opening the pop-up that asks the user for the path
            simu_pop_up = UserEntryPopUp("Simulateur", ["Entrez le chemin d'accès au simulateur :"], [0])
            simu_pop_up.mainloop()

            # Opening the pop-up that asks the user for the path
            rc_pop_up = UserEntryPopUp("RC", ["Entrez le chemin d'accès à RC :"], [0])
            rc_pop_up.mainloop()

            settings_list = [
                "Simulat.exe",                                  # Simulator software name
                "rc5.exe",                                      # RC software name
                f"{simu_pop_up.get_user_entries()[0]}",         # Simulator Path
                f"{rc_pop_up.get_user_entries()[0]}",           # RC Path
                f"{CONSTANT_INIT_PATH}",                        # Init Folder Path
                "Menu général",                                 # RC window name
                "tab",                                          # Key to end test recording
                "C:\\EUROPLACER\\ep\\epi\\RCARRETPROPRE.txt",   # file that asks you to make a report when you kill RC
                "C:\\EUROPLACER\\ep\\tmp"                       # file where there are traces of RC
            ]   

            self.create_file(CONSTANT_SETTINGS_FOLDER_PATH, CONSTANT_NAME_SETTINGS_FILE, settings_list)


    def delete_file(self, path: str):
        """ `+`
        `Type:` Procedure
        `Description:` delete the file
        :param:`path:` path of the file
        """

        os.remove(path)
        