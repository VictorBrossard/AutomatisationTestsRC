# Author        : Victor BROSSARD
# Description   : Object that takes a screenshot

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import time
import os

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

        pass

    
    def take_screenshot(self, path: str, file_name: str):
        """ `-`
        `Type:` Procedure
        `Description:` take the picture
        :param:`path:` path where you save the screenshot
        :param:`file_name:` file name
        """
        
        time.sleep(1)               # waiting time otherwise the photo taking is too fast
        screen = ImageGrab.grab()   # take the picture

        # saving the picture
        screen_name = file_name + ".png"
        os.chdir(str(path)) # Change the current working directory by giving the path
        screen.save(screen_name)


    def find_name(self, path: str, file_name: str) -> str:
        """ `-`
        `Type:` Function
        `Description:` add a number to the file name to avoid duplicates
        :param:`path:` path where you save the screenshot
        :param:`file_name:` beginning of the file name
        `Return:` name of the file
        """

        os.chdir(path) # Change the current working directory by giving the path

        # find the file number
        file_list = os.listdir(file_name)
        nb_files = len(file_list) + 1
        name = file_name + "(" + str(nb_files) + ")"
        return name