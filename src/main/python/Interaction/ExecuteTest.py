# Author        : Victor BROSSARD
# Description   : 

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import tkinter.messagebox
import time

from pynput.mouse import Button
from pynput.mouse import Controller as MouseController
from pynput.keyboard import Key
from pynput.keyboard import KeyCode
from pynput.keyboard import Controller as KeyboardController
from FilesManagement.InitFolders import CONSTANT_TESTS_FOLDER_PATH
from Interaction.KeyTranslation import KeyTranslation

#-----------------------------------------------------------------------------------------------------
#
class ExecuteTest():

    def __init__(self):
        """
        Constructor
        """
        self.mouse = MouseController()
        self.keyboard = KeyboardController()

    def read_test_file(self, file_name):
        """
        """
        file_path = CONSTANT_TESTS_FOLDER_PATH + "\\" + file_name + ".txt"

        try:
            test_file = open(file_path, "r")
            first_line = test_file.readline()

            first_word_list = first_line.split(";")
            self.__find_action(first_word_list, [])

            before_word_list = first_word_list

            time.sleep(1)

            for line in test_file:
                now_word_list = line.split(";")
                self.__find_action(now_word_list, before_word_list)
                before_word_list = now_word_list
        except Exception as e:
            tkinter.messagebox.showinfo('ERROR File',e)

    def __find_action(self, now_word_list, before_word_list):
        """
        """
        first_word = now_word_list[0]

        if first_word == "Click":
            self.__click_input(now_word_list, before_word_list) 
        if first_word == "Key":
            self.__key_input(now_word_list, before_word_list)
        if first_word == "Scroll":
            self.__scroll_input(now_word_list, before_word_list)

    def __click_input(self, now_word_list, before_word_list):
        """
        """
        if before_word_list != []:
            wait_time = self.__find_wait_time(now_word_list, before_word_list)
            time.sleep(wait_time)

        button = now_word_list[1]
        x = now_word_list[2]
        y = now_word_list[3]

        if button == "left":
            self.mouse.position = (x,y)
            self.mouse.click(Button.left)

        if button == "right":
            self.mouse.position = (x,y)
            self.mouse.click(Button.right)

        if button == "middle":
            self.mouse.position = (x,y)
            self.mouse.click(Button.middle)

    def __key_input(self, now_word_list, before_word_list):
        """
        """
        if before_word_list != []:
            wait_time = self.__find_wait_time(now_word_list, before_word_list)
            time.sleep(wait_time)

        key_char = now_word_list[1]

        if key_char != "None":
            key = KeyTranslation(key_char).get_key()

            self.keyboard.press(key)
            time.sleep(1)
            self.keyboard.release(key)

    def __scroll_input(self, now_word_list, before_word_list):
        """
        
        """
        if before_word_list != []:
            wait_time = self.__find_wait_time(now_word_list, before_word_list)
            time.sleep(wait_time)

        x = now_word_list[1]
        y = now_word_list[2]
        dx = now_word_list[3]
        dy = now_word_list[3]

        self.mouse.position = (x, y)
        self.mouse.scroll(dx, dy)

    def __find_wait_time(self, now_word_list, before_word_list):
        """
        """
        now = now_word_list[0]
        before = before_word_list[0]

        if now == "Click":
            now_time = now_word_list[4]
        else:
            if now == "Key":
                now_time = now_word_list[2]
            else:
                now_time = now_word_list[5]

        if before == "Click":
            before_time = before_word_list[4]
        else:
            if before == "Key":
                before_time = before_word_list[2]
            else:
                before_time = before_word_list[5]

        wait_time = float(now_time) - float(before_time)

        return int(wait_time)