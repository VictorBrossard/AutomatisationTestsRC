# Author        : Victor BROSSARD
# Description   : Object that opens simulator and RC

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
import subprocess
import os
import tkinter.messagebox

from GraphicInterface.SettingsInterface import SettingsInterface
from FilesManagement.ManipulationSettingsFile import ManipulationSettingsFile
from UsefulFunction.UsefulFunction import is_soft_open

#-----------------------------------------------------------------------------------------------------

class OpenSoftwares(object):
    """ `+`
    :class:`OpenSoftwares` uses software paths to open them
    """

    def __init__(self):
        """ `-`
        `Type:` Constructor
        """

        pass
    

    def __start_simu(self):
        """ `-`
        `Type:` Procedure
        `Description:` open the simulator
        """

        line_settings_file = ManipulationSettingsFile() # read the file that contains the parameters

        try:
            # Opening the software 
            os.chdir(line_settings_file.get_simu_path())                                # Change the current working directory by giving the path
            subprocess.run(['start', line_settings_file.get_simu_exe()], shell=True)    # Open the software using the start command
        except Exception as e:
            tkinter.messagebox.showinfo('Simulator Path ERROR',e)                       # Displaying the error message for the user
            settings = SettingsInterface()
            settings.mainloop()
            self._start_simu()
            
    
    def __start_rc(self):
        """ `-`
        `Type:` Procedure
        `Description:` open RC
        """

        line_settings_file = ManipulationSettingsFile() # read the file that contains the parameters

        try:
            # Opening the software
            os.chdir(line_settings_file.get_rc_path())                                  # Change the current working directory by giving the path
            subprocess.run(['start', line_settings_file.get_rc_exe()], shell=True)      # Open the software using the start command
        except Exception as e:
            tkinter.messagebox.showinfo('RC Path ERROR',e)                              # Displaying the error message for the user
            settings = SettingsInterface()
            settings.mainloop()
            self._start_rc()        


    def open_soft(self):
        """ `+`
        `Type:` Procedure
        `Description:` open both softwares
        """

        line_settings_file = ManipulationSettingsFile() # read the file that contains the parameters

        # Open software if closed
        if not is_soft_open(line_settings_file.get_simu_exe()):
            self.__start_simu()
            
        if not is_soft_open(line_settings_file.get_rc_exe()):
            self.__start_rc()