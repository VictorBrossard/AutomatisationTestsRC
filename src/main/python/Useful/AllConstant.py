# Author        : Victor BROSSARD
# Description   : File that stores all the constants of the software

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import os

#-----------------------------------------------------------------------------------------------------
# Initialization of constants

# ManageSpecificFiles
CONSTANT_NAME_SETTINGS_FILE = "settings.txt"
CONSTANT_NAME_DATABASE_FILE = "database_settings.txt"
CONSTANT_ENCRYPTION_KEY = "GEJvRguUGA1y8cPK"

#######################################################################################################

# ReadTraceFile
CONSTANT_START_PROD_FILE = "start_prod.txt"

#######################################################################################################

# ManageFolders
CONSTANT_INIT_PATH = f"C:\\Users\\{os.getlogin()}\\Documents"

CONSTANT_MAIN_FOLDER_PATH = CONSTANT_INIT_PATH + "\\AutomatisationRC"

CONSTANT_FILES_FOLDER_PATH = CONSTANT_MAIN_FOLDER_PATH + "\\Files"

CONSTANT_TESTS_FOLDER_PATH = CONSTANT_FILES_FOLDER_PATH + "\\tests" 
CONSTANT_SETTINGS_FOLDER_PATH = CONSTANT_FILES_FOLDER_PATH + "\\settings"

CONSTANT_REPORTS_FOLDER_PATH = CONSTANT_TESTS_FOLDER_PATH + "\\reports"
CONSTANT_EXCUTABLE_TESTS_FOLDER_PATH = CONSTANT_TESTS_FOLDER_PATH + "\\executable_tests"
CONSTANT_TEST_PIECES_FOLDER_PATH = CONSTANT_TESTS_FOLDER_PATH + "\\test_pieces"
CONSTANT_TEST_AVAILABLE_FOLDER_PATH = CONSTANT_TESTS_FOLDER_PATH + "\\test_available"

#######################################################################################################

# SettingsInterface
    # Column
CONSTANT_LABEL_COLUMN = int(0)
CONSTANT_ENTRY_COLUMN = int(2)
CONSTANT_TITLE_COLUMN = int(1)
CONSTANT_BUTTON_COLUMN = int(1)

    # Title
CONSTANT_SETTINGS_TITLE_LINE = int(0)
CONSTANT_TEST_TITLE_LINE = int(7)

    # Line
CONSTANT_SIMU_EXE_LINE = CONSTANT_SETTINGS_TITLE_LINE + 1
CONSTANT_RC_EXE_LINE = CONSTANT_SIMU_EXE_LINE + 1
CONSTANT_SIMU_PATH_LINE = CONSTANT_RC_EXE_LINE + 1
CONSTANT_RC_PATH_LINE = CONSTANT_SIMU_PATH_LINE + 1
CONSTANT_FOLDER_PATH_LINE = CONSTANT_RC_PATH_LINE + 1
CONSTANT_RC_WINDOW_NAME_LINE = CONSTANT_FOLDER_PATH_LINE + 1
CONSTANT_STOP_KEY_LINE = CONSTANT_TEST_TITLE_LINE + 1

    # Button
CONSTANT_BUTTON_LINE = CONSTANT_STOP_KEY_LINE + 1

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

#######################################################################################################

# Interaction
CONSTANT_RC_WINDOW_NAME = "Menu Général"