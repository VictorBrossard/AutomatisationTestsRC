# Author        : Victor BROSSARD
# Description   : Class that allows the creation of any file

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
import subprocess
import os
import sys
import base64
import hashlib

from cryptography.fernet import Fernet

from FilesManagement.Folders.ManageFolders import CONSTANT_SETTINGS_FOLDER_PATH  # path where we store the settings file
from FilesManagement.Folders.ManageFolders import CONSTANT_INIT_PATH

from GraphicInterface.UserEntryPopUp import UserEntryPopUp
from GraphicInterface.MessageBox import MessageBox

#-----------------------------------------------------------------------------------------------------
# Initialization of constants
CONSTANT_NAME_SETTINGS_FILE = "settings.txt"
CONSTANT_NAME_DATABASE_FILE = "database_settings.txt"
CONSTANT_ENCRYPTION_KEY = "GEJvRguUGA1y8cPK"

#-----------------------------------------------------------------------------------------------------

class ManageFiles(object):
    """ `+`
    :class:`ManageFiles` manage the creation of any file
    """
    
    def __init__(self):
        """ `-`
        `Type:` Constructor
        """

        pass


    def create_file(self, path: str, file_name: str, line_list: list):
        """ `+`
        `Type:` Procedure
        `Description:` creates a txt file
        :param:`path:` path where you save the file
        :param:`file_name:` file name
        :param:`line_list:` line to write in the file
        """

        if os.path.exists(f"{path}\\{file_name}"):
            return

        # Creation of the file 
        os.chdir(path) # Change the current working directory by giving the path
        subprocess.run(['type', 'nul', '>', file_name], shell=True)                     

        # Save the values in the file we have created
        os.chdir(path)
        file_path = open(file_name, 'w') # Opening the file in write mode ('w')

        if line_list != []:
            for line in line_list:
                file_path.write(f"{line}\n")

        file_path.close()


    def create_executing_file(self, path: str, file_name: str, str_to_transform: str):
        """ `+`
        `Type:` Porcedure
        `Description:`
        :param:`path:` folder where we will store the file
        :param:`file_name:` name of the file you are creating
        :param:`str_to_transform:` string to transform into a file InputRecorder
        """

        file_line_list = []
        tme = 0.000

        # creation of the instruction list
        for chr in str_to_transform:
            file_line_list.append(f"Key;{chr};{tme}")
            tme = tme + 0.001

        if os.path.exists(f"{path}\\{file_name}"):
            os.remove(f"{path}\\{file_name}")

        # file creation
        self.create_file(path, file_name, file_line_list)


    def create_soft_settings_file(self):
        """ `+`
        `Type:` Procedure
        `Description:` create the file that contains all the parameters
        """

        # Check if the file exists
        if not os.path.exists(f"{CONSTANT_SETTINGS_FOLDER_PATH}\\{CONSTANT_NAME_SETTINGS_FILE}"):
            # Opening the pop-up that asks the user for the paths
            pop_up = UserEntryPopUp("Simulateur", ["Entrez le chemin d'accès au simulateur :", "Entrez le chemin d'accès à RC :"], [0, 0])
            pop_up.mainloop()

            user_entry_list = pop_up.get_user_entries()

            # verification that the user has given us a value
            for entries in user_entry_list:
                if entries == "":
                    MessageBox("ERREUR Manque d'information", "[ERREUR] Vous n'avez pas remplis toutes les cases.").mainloop()
                    self.create_soft_settings_file()
                    return

            settings_list = [
                "Simulat.exe",                                  # Simulator software name
                "rc5.exe",                                      # RC software name
                f"{user_entry_list[0]}",                        # Simulator Path
                f"{user_entry_list[1]}",                        # RC Path
                f"{CONSTANT_INIT_PATH}",                        # Init Folder Path
                "Menu général",                                 # RC window name
                "tab",                                          # Key to end test recording
                "C:\\EUROPLACER\\ep\\epi\\RCARRETPROPRE.txt",   # file that asks you to make a report when you kill RC
                "C:\\EUROPLACER\\ep\\tmp"                       # file where there are traces of RC
            ]   

            self.create_file(CONSTANT_SETTINGS_FOLDER_PATH, CONSTANT_NAME_SETTINGS_FILE, settings_list)


    def create_database_settings_file(self):
        """ `+`
        `Type:` Procedure
        `Description:` create the file that contains all the database parameters
        """

        # Check if the file exists
        if not os.path.exists(f"{CONSTANT_SETTINGS_FOLDER_PATH}\\{CONSTANT_NAME_DATABASE_FILE}"):
            # Opening the pop-up that asks the user for the parameters
            pop_up = UserEntryPopUp("Simulateur", ["Username :", "Password :", "Host :", "Port :", "Database :"], [0, 0, 0, 1, 0])
            pop_up.mainloop()

            user_entry_list = pop_up.get_user_entries()

            # verification that the user has given us a value
            for entries in user_entry_list:
                if entries == "":
                    MessageBox("ERREUR Manque d'information", "[ERREUR] Vous n'avez pas remplis toutes les cases.").mainloop()
                    self.create_database_settings_file()
                    return

            settings_list = [
                f"{user_entry_list[0]}",                                                # Username
                f"{self.__encryption(user_entry_list[1], CONSTANT_ENCRYPTION_KEY)}",    # Encrypted password
                f"{user_entry_list[2]}",                                                # Host
                f"{user_entry_list[3]}",                                                # Port
                f"{user_entry_list[4]}"                                                 # Database
            ]   

            self.create_file(CONSTANT_SETTINGS_FOLDER_PATH, CONSTANT_NAME_DATABASE_FILE, settings_list)


    def get_database_lines(self) -> list:
        """ `+`
        `Type:` Function
        `Description:` get all the lines of the database file 
        `Return:` list of file lines
        """

        lines_list = []

        try:
            fil = open(f"{CONSTANT_SETTINGS_FOLDER_PATH}\\{CONSTANT_NAME_DATABASE_FILE}", "r")
            lines = fil.readlines()
            fil.close()
        except Exception:
            MessageBox("ERREUR", "[ERREUR] Problème avec le fichier database.").mainloop()
            sys.exit(1)

        # recovery of all the lines of the file without the \n and modification of the line of the password
        for i, line in enumerate(lines):
            original_line = line.rstrip() # line without back to the line

            if i == 1: # Password
                decryption_sentence = self.__decryption(line, CONSTANT_ENCRYPTION_KEY)
                lines_list.append(decryption_sentence)
            else:
                lines_list.append(original_line)

        return lines_list
    

    def __encryption(self, sentence: str, key: str) -> str:
        """ `-`
        `Type:` Function
        `Description:` encrypts a sentence with a key
        :param:`sentence:` sentence to encrypted
        :param:`key:` encryption key
        `Return:` string encrypted sentence
        """

        # obtaining a valid key in 32 bytes encoded in base64
        key_bytes = key.encode("utf-8")
        key_valid_bytes = hashlib.sha256(key_bytes).digest()

        # encryption of the sentence with the key
        cipher = Fernet(base64.urlsafe_b64encode(key_valid_bytes))
        encrypted_sentence_bytes = cipher.encrypt(sentence.encode("utf-8"))

        # returns the key encrypted in string and not in byte
        return encrypted_sentence_bytes.decode("utf-8")


    def __decryption(self, sentence: str, key: str) -> str:
        """ `-`
        `Type:` Function
        `Description:` decodes a sentence with a key
        :param:`sentence:` sentence to be decoded
        :param:`key:` encryption key
        `Return:` sentence decoded in string
        """

        # obtaining a valid key in 32 bytes encoded in base64
        key_bytes = key.encode("utf-8")
        key_valid_bytes = hashlib.sha256(key_bytes).digest()

        # decryption of the sentence with the key
        cipher = Fernet(base64.urlsafe_b64encode(key_valid_bytes))
        decoded_sentence_bytes = cipher.decrypt(sentence.encode("utf-8"))

        # returns the decrypted key in string and not in byte
        return decoded_sentence_bytes.decode("utf-8")


    def delete_file(self, path: str):
        """ `+`
        `Type:` Procedure
        `Description:` delete the file
        :param:`path:` path of the file
        """

        os.remove(path)
        