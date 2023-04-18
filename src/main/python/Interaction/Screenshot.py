# Author        : Victor BROSSARD
# Description   : 

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import time
import os
import datetime

from FilesManagement.InitFolders import CONSTANT_SCREENSHOTS_FOLDER_PATH
from PIL import ImageGrab

#-----------------------------------------------------------------------------------------------------
#
class Screenshot:

    # Constructor
    def __init__(self):
        self.take_screenshot()

    #
    def take_screenshot(self):
        #
        time.sleep(1)

        ###### PREND LA PHOTO
        screen = ImageGrab.grab()

        #
        file_name = self.create_screenshot_path()
        screen_name = self.find_name(file_name) + ".png"
        os.chdir(CONSTANT_SCREENSHOTS_FOLDER_PATH + "\\" + file_name)
        screen.save(screen_name)

    ###### VA CHERCHER LE DOSSIER POUR STOCKER LE FICHIER S'IL EST PAS CREE ALORS ON LE FAIT SINON ON RENVOIE JUSTE LA DATE D AUJOURD HUI CAR ON STOCK SELON LA DATE
    def create_screenshot_path(self):
        #
        today_date = str(datetime.date.today())

        #
        if not os.path.exists(CONSTANT_SCREENSHOTS_FOLDER_PATH + "\\" + today_date):
            #
            os.chdir(CONSTANT_SCREENSHOTS_FOLDER_PATH)
            os.makedirs(today_date)
            return today_date
        else:
            return today_date

    ####### RAJOUTE UN NUMERO DERRIERE LA DATE D AUJOURD HUI POUR STOCKER LES IMAGES. ON DETERMINE LE NUMERO EN COMPTANT LE NOMBRE DE FICHIER DANS LE DOSSIER
    def find_name(self, file_name):
        os.chdir(CONSTANT_SCREENSHOTS_FOLDER_PATH)
        file_list = os.listdir(file_name)
        nb_files = len(file_list) + 1
        name = file_name + "(" + str(nb_files) + ")"
        return name