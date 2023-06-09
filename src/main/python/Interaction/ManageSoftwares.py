# Author        : Victor BROSSARD
# Description   : Object that opens simulator and RC

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
import subprocess
import os

from FilesManagement.Files.ManipulationSettingsFile import ManipulationSettingsFile
from FilesManagement.Files.ManageAnyFile import ManageAnyFile

from Useful.UsefulFunction import is_soft_open

from Useful.AllConstant import CONSTANT_SETTINGS_FOLDER_PATH
from Useful.AllConstant import CONSTANT_NAME_SETTINGS_FILE

#-----------------------------------------------------------------------------------------------------

class ManageSoftwares(object):
    """ `+`
    :class:`OpenSoftwares` uses software paths to open them
    """

    def __init__(self):
        """ `-`
        `Type:` Constructor
        """

        self.settings = ManipulationSettingsFile() # read the file that contains the parameters
    

    def __start_simu(self):
        """ `-`
        `Type:` Procedure
        `Description:` open the simulator
        """

        simu_exe = self.settings.get_line(0)
        simu_path = self.settings.get_line(2)

        try:
            # Opening the software 
            os.chdir(simu_path)                                 # Change the current working directory by giving the path
            subprocess.run(['start', simu_exe], shell=True)     # Open the software using the start command
        except Exception as e:
            print(f"[ERREUR] {e}")                              # Displaying the error message for the user
            ManageAnyFile().delete_file(f"{CONSTANT_SETTINGS_FOLDER_PATH}\\{CONSTANT_NAME_SETTINGS_FILE}")
            
    
    def __start_rc(self):
        """ `-`
        `Type:` Procedure
        `Description:` open RC
        """

        rc_exe = self.settings.get_line(1)
        rc_path = self.settings.get_line(3)

        try:
            # Opening the software
            os.chdir(rc_path)                               # Change the current working directory by giving the path
            subprocess.run(['start', rc_exe], shell=True)   # Open the software using the start command
        except Exception as e:
            print(f"[ERREUR] {e}")                          # Displaying the error message for the user
            ManageAnyFile().delete_file(f"{CONSTANT_SETTINGS_FOLDER_PATH}\\{CONSTANT_NAME_SETTINGS_FILE}")      


    def open_soft(self):
        """ `+`
        `Type:` Procedure
        `Description:` open both softwares
        """

        simu_exe = self.settings.get_line(0)
        rc_exe = self.settings.get_line(1)

        # Open software if closed
        if not is_soft_open(simu_exe):
            self.__start_simu()
            
        if not is_soft_open(rc_exe):
            self.__start_rc()


    def close_soft(self):
        """ `+`
        `Type:` Procedure
        `Description:` close both softwares
        """

        simu_exe = self.settings.get_line(0)
        rc_exe = self.settings.get_line(1)
        file_to_delete = self.settings.get_line(6) # file that asks you to make a report when you kill RC

        # Close softwares
        try:
            if is_soft_open(rc_exe):
                subprocess.run(['taskkill', '/f', '/im', rc_exe], shell=True)   # Shell command to close RC

            if os.path.isfile(file_to_delete):
                os.remove(file_to_delete)
        except Exception as e:
            print(f"[ERREUR] {e}")                                              # Displaying the error message for the user
            return

        try:
            if is_soft_open(simu_exe):
                subprocess.run(['taskkill', '/f', '/im', simu_exe], shell=True) # Shell command to close the simulator
        except Exception as e:
            print(f"[ERREUR] {e}")                                              # Displaying the error message for the user
            return