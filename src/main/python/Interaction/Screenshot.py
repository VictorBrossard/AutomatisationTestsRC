# Author        : Victor BROSSARD
# Description   : Object that takes a screenshot

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import time
import os
import datetime

from FilesManagement.Folders.ManageFolders import CONSTANT_SCREENSHOTS_FOLDER_PATH

from PIL import ImageGrab

#-----------------------------------------------------------------------------------------------------
#
class Screenshot(object):
    """ `+`
    :class:`Screenshot` takes a screenshot
    """

    def __init__(self):
        """ `-`
        `Type:` Constructor
        """

        self.__take_screenshot()

    
    def __take_screenshot(self):
        """ `-`
        `Type:` Procedure
        `Description:` take the picture
        """
        
        time.sleep(1)               # waiting time otherwise the photo taking is too fast
        screen = ImageGrab.grab()   # take the picture

        # saving the picture
        file_name = self.__create_screenshot_path()
        screen_name = self.__find_name(file_name) + ".png"
        os.chdir(CONSTANT_SCREENSHOTS_FOLDER_PATH + "\\" + file_name) # Change the current working directory by giving the path
        screen.save(screen_name)

    
    def __create_screenshot_path(self) -> str:
        """ `-`
        `Type:` Fonction
        `Description:` look for the folder to store the file if it is not created then we do it otherwise 
                we just return today's date because we store according to the date
        `Return:` the folder name
        """

        today_date = str(datetime.date.today()) # turn today's date into a string

        # check that the folder does not exist to create it
        if not os.path.exists(CONSTANT_SCREENSHOTS_FOLDER_PATH + "\\" + today_date):
            os.chdir(CONSTANT_SCREENSHOTS_FOLDER_PATH)  # Change the current working directory by giving the path
            os.makedirs(today_date)                     # create the folder
            return today_date
        else:
            return today_date


    def __find_name(self, file_name: str) -> str:
        """ `-`
        `Type:` Function
        `Description:` add a number to the file name to avoid duplicates
        :param:`file_name:` beginning of the file name
        `Return:` name of the file
        """

        os.chdir(CONSTANT_SCREENSHOTS_FOLDER_PATH) # Change the current working directory by giving the path

        # find the file number
        file_list = os.listdir(file_name)
        nb_files = len(file_list) + 1
        name = file_name + "(" + str(nb_files) + ")"
        return name