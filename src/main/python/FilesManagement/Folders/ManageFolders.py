# Author        : Victor BROSSARD
# Description   : Class that allows you to manage any type of folder

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import os

from Useful.AllConstant import CONSTANT_INIT_PATH
from Useful.AllConstant import CONSTANT_FILES_FOLDER_PATH
from Useful.AllConstant import CONSTANT_TESTS_FOLDER_PATH

#-----------------------------------------------------------------------------------------------------

class ManageFolders(object):
    """ `+`
    :class:`ManageFolders` allows you to manage any type of folder
    """

    def __init__(self):
        """ `-`
        `Type:` Constructor
        """

        pass


    def create_folder(self, name_folder: str, path: str) -> str:
        """ `+`
        `Type:` Function
        `Description:` create a folder with its name and path
        :param:`name_folder:` name of the folder to be created
        :param:`path:` path where we create the folder
        `Return:` the path of the folder if it has been created
        """
        
        full_path = f"{path}\\{name_folder}"

        # Check that the file doesn't exist
        if not os.path.exists(full_path):
            os.chdir(path)              # Change the current working directory by giving the path
            os.makedirs(name_folder)    # Create the folder
            return full_path
        else:
            return ""
    

    def create_soft_folders(self):
        """ `+`
        `Type:` Procedure
        `Description:` creates all the folders where we will store our files
        """

        self.create_folder("software files", CONSTANT_INIT_PATH)

        self.create_folder("tests", CONSTANT_FILES_FOLDER_PATH)
        self.create_folder("settings", CONSTANT_FILES_FOLDER_PATH)

        self.create_folder("reports", CONSTANT_TESTS_FOLDER_PATH)
        self.create_folder("test_pieces", CONSTANT_TESTS_FOLDER_PATH)
        self.create_folder("execution", CONSTANT_TESTS_FOLDER_PATH)


    def delete_inside_folder(self, path: str):
        """ `+`
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
                        self.delete_inside_folder(sub_element_path)
                        os.rmdir(sub_element_path)
                
                os.rmdir(element_path)
            elif os.path.isfile(element_path):
                os.remove(element_path)


    def delete_folder(self, path: str):
        """ `+`
        `Type:` Procedure
        `Description:` delete the folder
        :param:`path:` path of the folder
        """

        os.rmdir(path)


    def count_nb_files_in_folder(self, folder_path: str) -> int:
        """ `+`
        `Type:` Function
        `Description:` calculates the number of files in a folder
        :param:`folder_path:` folder _path
        `Return:` number of files in folder
        """

        nb_file = 0

        for _ in os.listdir(folder_path):
            nb_file = nb_file + 1

        return nb_file