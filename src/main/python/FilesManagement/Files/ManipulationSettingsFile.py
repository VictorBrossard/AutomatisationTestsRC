# Author        : Victor BROSSARD
# Description   : Object that manipulates the settings file

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
import subprocess
import os
import sys

from Useful.AllConstant import CONSTANT_NAME_SETTINGS_FILE
from Useful.AllConstant import CONSTANT_SETTINGS_FOLDER_PATH # path where we store the settings file

#-----------------------------------------------------------------------------------------------------

class ManipulationSettingsFile(object):
    """ `+`
    :class:`ManipulationSettingsFile` manipulates the settings file
    """

    def __init__(self):
        """ `-`
        `Type:` Constructor
        """

        with open(f"{CONSTANT_SETTINGS_FOLDER_PATH}\\{CONSTANT_NAME_SETTINGS_FILE}", 'r') as f:
            lines = f.readlines()

        self.nb_lines = len(lines)


    def __read_line(self, path: str, file_name: str, nb_line: int) -> str:
        """ `-`
        `Type:` Function
        `Description:` read line nb_line of file file_name
        :param:`path:` path of the file to read
        :param:`file_name:` name of the file to read
        :param:`nb_line:` number of the line that we want to retrieve in the file
        `Return:` line nb_line of the file
        """

        try:
            # get line nb_line of file
            os.chdir(path)
            file_path = open(file_name, 'r')                    # Opening the file in read mode ('r')
            line = file_path.readlines()[nb_line].rstrip()      # rstrip removes the line break which is automatically taken into account with the readlines function
            file_path.close()

            return line
        except Exception as e:
            print("[ERREUR]", e)
            sys.exit()
    

    def manage_file(self, settings_list: list):
        """ `+`
        `Type:` Procedure 
        `Description:` create the parameter file if it does not exist otherwise we modify it
        :param:`settings_list:` list of all parameters
        """

        if not os.path.exists(f"{CONSTANT_SETTINGS_FOLDER_PATH}\\{CONSTANT_NAME_SETTINGS_FILE}"):
            # Creation of the file 
            os.chdir(CONSTANT_SETTINGS_FOLDER_PATH) # Change the current working directory by giving the path
            subprocess.run(['type', 'nul', '>', CONSTANT_NAME_SETTINGS_FILE], shell=True)
        else:
            os.chdir(CONSTANT_SETTINGS_FOLDER_PATH)
            os.remove(CONSTANT_NAME_SETTINGS_FILE) # Delete the file 
            subprocess.run(['type', 'nul', '>', CONSTANT_NAME_SETTINGS_FILE], shell=True)

        # Save the paths in the file we have created
        os.chdir(CONSTANT_SETTINGS_FOLDER_PATH)
        file_path = open(CONSTANT_NAME_SETTINGS_FILE, 'w') # Opening the file in write mode ('w')

        for setting in settings_list:
            file_path.write(f"{setting}\n")

        file_path.close()


    def get_line(self, nb_line: int) -> str:
        """ `+`
        `Type:` Function
        `Description:` getter that returns the variable on the line nb_line
        `Return:` item in line nb_line
        """

        return self.__read_line(CONSTANT_SETTINGS_FOLDER_PATH, CONSTANT_NAME_SETTINGS_FILE, nb_line)
    
    
    def get_nb_line(self) -> int:
        """ `+`
        `Type:` Function
        `Description:` getter that returns the variable nb_lines
        `Return:` nb_lines
        """

        return self.nb_lines