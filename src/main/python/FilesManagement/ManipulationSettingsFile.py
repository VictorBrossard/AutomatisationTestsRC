# Author        : Victor BROSSARD
# Description   : Object that manipulates the settings file

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
import subprocess
import os

from FilesManagement.InitFolders import CONSTANT_SETTINGS_FOLDER_PATH  # path where we store the settings file
from FilesManagement.InitFolders import CONSTANT_NAME_SETTINGS_FILE

#-----------------------------------------------------------------------------------------------------

class ManipulationSettingsFile(object):
    """ `+`
    :class:`ManipulationSettingsFile` manipulates the settings file
    """

    def __init__(self):
        """ `-`
        `Type:` Constructor
        """

        # Read all lines from file
        self.simu_exe = self.__read_line(CONSTANT_SETTINGS_FOLDER_PATH, CONSTANT_NAME_SETTINGS_FILE, 0)
        self.rc_exe = self.__read_line(CONSTANT_SETTINGS_FOLDER_PATH, CONSTANT_NAME_SETTINGS_FILE, 1)
        self.simu_path = self.__read_line(CONSTANT_SETTINGS_FOLDER_PATH, CONSTANT_NAME_SETTINGS_FILE, 2)
        self.rc_path = self.__read_line(CONSTANT_SETTINGS_FOLDER_PATH, CONSTANT_NAME_SETTINGS_FILE, 3)
        self.folder_path = self.__read_line(CONSTANT_SETTINGS_FOLDER_PATH, CONSTANT_NAME_SETTINGS_FILE, 4)
        self.rc_window_name = self.__read_line(CONSTANT_SETTINGS_FOLDER_PATH, CONSTANT_NAME_SETTINGS_FILE, 5)
        self.test_stop_key = self.__read_line(CONSTANT_SETTINGS_FOLDER_PATH, CONSTANT_NAME_SETTINGS_FILE, 6)


    def __read_line(self, path: str, file_name: str, nb_line: int) -> str:
        """ `-`
        `Type:` Function
        `Description:` read line nb_line of file file_name
        :param:`path:` path of the file to read
        :param:`file_name:` name of the file to read
        :param:`nb_line:` number of the line that we want to retrieve in the file
        `Return:` line nb_line of the file
        """

        # get line nb_line of file
        os.chdir(path)
        file_path = open(file_name, 'r')                    # Opening the file in read mode ('r')
        line = file_path.readlines()[nb_line].rstrip()      # rstrip removes the line break which is automatically taken into account with the readlines function
        file_path.close()

        return line
    

    def manage_file(self, simu_exe: str, rc_exe: str, simu_path: str, rc_path: str, folder_path: str, rc_window_name: str, test_stop_key: str):
        """ `+`
        `Type:` Procedure
        `Description:` create the parameter file if it does not exist otherwise we modify it
        :param:`simu_exe:` simulator .exe name
        :param:`rc_exe:` RC .exe name
        :param:`simu_path:` path where the .exe of the simulator is located
        :param:`rc_path:` path where the .exe of the RC is located
        :param:`folder_path:` path of the folders where we store our files
        :param:`rc_window_name:` RC window name
        :param:`test_stop_key:`key that allows the stop of the recording and the execution of the tests
        """

        if not os.path.exists(CONSTANT_SETTINGS_FOLDER_PATH + '\\' + CONSTANT_NAME_SETTINGS_FILE):
            # Creation of the file 
            os.chdir(CONSTANT_SETTINGS_FOLDER_PATH) # Change the current working directory by giving the path
            subprocess.run(['type', 'nul', '>', CONSTANT_NAME_SETTINGS_FILE], shell=True)
        else:
            os.chdir(CONSTANT_SETTINGS_FOLDER_PATH)
            os.remove(CONSTANT_NAME_SETTINGS_FILE)  # Delete the file 
            subprocess.run(['type', 'nul', '>', CONSTANT_NAME_SETTINGS_FILE], shell=True)

        # Save the paths in the file we have created
        os.chdir(CONSTANT_SETTINGS_FOLDER_PATH)
        file_path = open(CONSTANT_NAME_SETTINGS_FILE, 'w')      # Opening the file in write mode ('w')
        file_path.write(f"{simu_exe} \n")                       # Simulator software name
        file_path.write(f"{rc_exe} \n")                         # RC software name
        file_path.write(f"{simu_path} \n")                      # Simulator Path
        file_path.write(f"{rc_path} \n")                        # RC Path
        file_path.write(f"{folder_path} \n")                    # Init Folder Path
        file_path.write(f"{rc_window_name} \n")                 # RC window name
        file_path.write(f"{test_stop_key} \n")                  # Key to end test recording
        file_path.close()


    def get_simu_exe(self) -> str:
        """ `+`
        `Type:` Function
        `Description:` getter that returns the variable simu_exe
        `Return:` simu_exe
        """

        return self.simu_exe
    
    
    def get_rc_exe(self) -> str:
        """ `+`
        `Type:` Function
        `Description:` getter that returns the variable rc_exe
        `Return:` rc_exe
        """

        return self.rc_exe
    

    def get_simu_path(self) -> str:
        """ `+`
        `Type:` Function
        `Description:` getter that returns the variable simu_path
        `Return:` simu_path
        """

        return self.simu_path


    def get_rc_path(self) -> str:
        """ `+`
        `Type:` Function
        `Description:` getter that returns the variable rc_path
        `Return:` rc_path
        """

        return self.rc_path
    

    def get_folder_path(self) -> str:
        """ `+`
        `Type:` Function
        `Description:` getter that returns the variable folder_path
        `Return:` folder_path
        """

        return self.folder_path
    

    def get_rc_window_name(self) -> str:
        """ `+`
        `Type:` Function
        `Description:` getter that returns the variable rc_window_name
        `Return:` rc_window_name
        """

        return self.rc_window_name
    

    def get_test_stop_key(self) -> str:
        """ `+`
        `Type:` Function
        `Description:` getter that returns the variable test_stop_key
        `Return:` test_stop_key
        """

        return self.test_stop_key
    