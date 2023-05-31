# Author        : Victor BROSSARD
# Description   : File that stores all the constants of the software

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import os
import sys

#-----------------------------------------------------------------------------------------------------
# Initialization of constants

# ManageSpecificFiles
CONSTANT_NAME_SETTINGS_FILE = "settings.txt"
CONSTANT_NAME_DATABASE_FILE = "database_settings.txt"
CONSTANT_ENCRYPTION_KEY = "GEJvRguUGA1y8cPK"

#######################################################################################################

# ReadTraceFile
CONSTANT_START_PROD_FILE = "f1.txt"
CONSTANT_TRACE_FILE_NAME = "ieee"

#######################################################################################################

# ManageFolders

def find_path_to_store_files(stop_path: str) -> str:
    """
    """

    parent_path = sys.path[0]

    while os.path.basename(parent_path) != stop_path:
        parent_path = os.path.dirname(parent_path)

    return parent_path

CONSTANT_INIT_PATH = find_path_to_store_files("AutomatisationTestsRC")

CONSTANT_FILES_FOLDER_PATH = CONSTANT_INIT_PATH + "\\software files"

CONSTANT_TESTS_FOLDER_PATH = CONSTANT_FILES_FOLDER_PATH + "\\tests" 
CONSTANT_SETTINGS_FOLDER_PATH = CONSTANT_FILES_FOLDER_PATH + "\\settings"

CONSTANT_REPORTS_FOLDER_PATH = CONSTANT_TESTS_FOLDER_PATH + "\\reports"
CONSTANT_TEST_PIECES_FOLDER_PATH = CONSTANT_TESTS_FOLDER_PATH + "\\test_pieces"
CONSTANT_EXECUTION_FOLDER_PATH = CONSTANT_TESTS_FOLDER_PATH + "\\execution"

#######################################################################################################

# CheckTest
CONSTANT_FORMAT_DATES_DATABASE = "%Y-%m-%d %H:%M:%S.%f"
CONSTANT_SHORT_FORMAT_DATES_DATABASE = "%Y-%m-%d %H:%M:%S"

#######################################################################################################

# InputRecorder
CONSTANT_KEYBOARD_SHORTCUTS = ["ctrl", "ctrl_l", "ctrl_r", "alt", "alt_r", "alt_l", "cmd", "cmd_l", "cmd_r"]

#######################################################################################################

# Command
CONSTANT_USER_COMMAND = ["-start", "-help", "-prg"]
CONSTANT_TEST_SETTINGS_FILE_NAME = "test_settings.txt"

#######################################################################################################

# Interaction
CONSTANT_RC_WINDOW_NAME = "Menu Général"

#######################################################################################################

# TestPiecesFile
CONSTANT_NB_TEST_PIECES_FILES = 16

#######################################################################################################

# Test name
CONSTANT_TEST_NAME = [
    "Production"
]

#######################################################################################################

# ReadTraceFile

# line of the trace file that we want to find to be able to execute certain files
CONSTANT_TRACE_DICTIONNARY = {
    "ClgMyDialog::OnInitDialog() : PRDBD_IDD_SUIVI_LOT" : "name.txt",                   # "ouverture de l'interface de saisie de lot"
    "CFX Trace : CTrSui::RecipeActivated" : CONSTANT_START_PROD_FILE,                   # "validation de l'interface de saisie de lot"
    "ClgMyDialog::OnInitDialog() : PRG_IDD_SELECTION" : "program_name.txt",             # "ouverture de l'interface de changement de programme"
    "ClgMyDialog::OnInitDialog() : RC_IDD_LOCAL_LIST" : "local_list_boxes.txt",         # "ouvrir l'interface de liste locale pour les boîtes"
    #"ClgMyDialog::OnDestroy() : IU_IDD_MAINMENU_PROD" : "destroy"                      # "fermeture de RC"
}