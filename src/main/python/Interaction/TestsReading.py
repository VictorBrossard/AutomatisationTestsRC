# Author        : Victor BROSSARD
# Description   : 

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import tkinter.messagebox

from FilesManagement.InitFolders import CONSTANT_TESTS_FOLDER_PATH

#-----------------------------------------------------------------------------------------------------
#
class TestReading():

    def __init__(self):
        """
        Constructor
        """
        pass

    def read_test_file(self, file_name):
        """
        """
        file_path = CONSTANT_TESTS_FOLDER_PATH + "\\" + file_name + ".txt"

        try:
            test_file = open(file_path, "r")

            for line in test_file:
                self.find_action(line)
        except Exception as e:
            tkinter.messagebox.showinfo('ERROR chemin RC',e)

    def find_action(self, line):
        """
        """
        first_word = line.split(";")[0]

        if first_word == "Click":
            self.click_input(line) 
        if first_word == "Key":
            self.key_input(line)
        if first_word == "Scroll":
            self.scroll_input(line)

    def click_input(self, line):
        """
        """
        print(line)

    def key_input(self, line):
        """
        """
        print(line)

    def scroll_input(self, line):
        """
        """
        print(line)