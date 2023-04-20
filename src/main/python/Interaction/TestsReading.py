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
                self.__find_action(line)
        except Exception as e:
            tkinter.messagebox.showinfo('ERROR chemin RC',e)

    def __find_action(self, line):
        """
        """
        first_word = line.split(";")[0]

        if first_word == "Click":
            self.__click_input(line) 
        if first_word == "Key":
            self.__key_input(line)
        if first_word == "Scroll":
            self.__scroll_input(line)

    def __click_input(self, line):
        """
        """
        print(line)

    def __key_input(self, line):
        """
        """
        print(line)

    def __scroll_input(self, line):
        """
        """
        print(line)