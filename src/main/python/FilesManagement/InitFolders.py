# Author        : Victor BROSSARD
# Description   : 

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import os

#-----------------------------------------------------------------------------------------------------
# Initialization of constants
CONSTANT_INIT_PATH = "C:\Program Files"
CONSTANT_MAIN_FOLDER_PATH = "C:\Program Files\AutomatisationRC"
CONSTANT_FILES_FOLDER_PATH = "C:\Program Files\AutomatisationRC\Files"
CONSTANT_PATHFILE_FOLDER_PATH = "C:\Program Files\AutomatisationRC\Files\pathFile"
CONSTANT_SCREENSHOTS_FOLDER_PATH = "C:\Program Files\AutomatisationRC\Files\screenshots"
CONSTANT_TOOLS_FOLDER_PATH = "C:\Program Files\AutomatisationRC\Files\\tools"
CONSTANT_NAMES_FOLDER_PATH = "C:\Program Files\AutomatisationRC\Files\\tools\\names"
CONSTANT_TESTS_FOLDER_PATH = "C:\Program Files\AutomatisationRC\Files\\tools\\tests"   ######## \\ car \ ne fonctionne pas tout seul quand il y a un t ou un n

#-----------------------------------------------------------------------------------------------------
#
class InitFolders:

    # Constructor
    def __init__(self):
        self.create_folder("AutomatisationRC", CONSTANT_INIT_PATH)
        self.create_folder("Files", CONSTANT_MAIN_FOLDER_PATH)
        self.create_folder("pathFile", CONSTANT_FILES_FOLDER_PATH)
        self.create_folder("screenshots", CONSTANT_FILES_FOLDER_PATH)
        self.create_folder("tools", CONSTANT_FILES_FOLDER_PATH)
        self.create_folder("names", CONSTANT_TOOLS_FOLDER_PATH)
        self.create_folder("tests", CONSTANT_TOOLS_FOLDER_PATH)

    #    
    def create_folder(self, name_folder, path):
        #
        if not os.path.exists(path + "\\" + name_folder):
            #
            os.chdir(path)
            os.makedirs(name_folder) ####### crée le dossier
