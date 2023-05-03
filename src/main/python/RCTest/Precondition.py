# Author        : Victor BROSSARD
# Description   : Class that manages the preconditions of the tests

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import os

from RCTest.ManageSoftwares import ManageSoftwares

from FilesManagement.ManipulationSettingsFile import ManipulationSettingsFile

#-----------------------------------------------------------------------------------------------------

class Precondition(object):
    """ `+`
    :class:`Precondition` manages the preconditions of the tests
    """

    def __init__(self):
        """ `-`
        `Type:` Constructor
        """

        self.settings = ManipulationSettingsFile()
        self.softwares = ManageSoftwares()


    def __delete_files_and_folder(self, path: str):
        """ `-`
        `Type:` Procedure
        `Description:` deletes files and folders in a folder
        :param:`path:` path of the folder we want to make empty
        """

        # path of all elements of the folder
        for element in os.listdir(path):
            element_path = os.path.join(path, element)
            
            # check if it is a folder or not
            # if it is the case you have to delete these files before deleting it
            if os.path.isdir(element_path):
            
                for sub_element in os.listdir(element_path):
                    sub_element_path = os.path.join(element_path, sub_element)

                    if os.path.isfile(sub_element_path):
                        os.remove(sub_element_path)
                    else:
                        self.__delete_files_and_folder(sub_element_path)
                        os.rmdir(sub_element_path)
                
                os.rmdir(element_path)
            elif os.path.isfile(element_path):
                os.remove(element_path)


    def start_precondition(self):
        """ `+`
        `Type:` Function
        `Description:` launches the selected precondition
        """

        tmp_path = self.settings.get_line(8)

        self.softwares.close_soft()

        self.__delete_files_and_folder(tmp_path)

        self.softwares.open_soft()