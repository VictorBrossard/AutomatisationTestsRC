# Author        : Victor BROSSARD
# Description   : Object that executes the tests made by the user

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import tkinter.messagebox
import time
import pyautogui

from pynput.mouse import Button
from pynput.mouse import Controller as MouseController
from pynput.keyboard import Key
from pynput.keyboard import Controller as KeyboardController
from Interaction.KeyTranslation import KeyTranslation
from Interaction.Screenshot import Screenshot

from FilesManagement.InitFolders import CONSTANT_TESTS_FOLDER_PATH

#-----------------------------------------------------------------------------------------------------

class ExecuteTest(object):
    """ `+`
    :class:`ExecuteTest` runs the tests made by the user
    """

    def __init__(self):
        """ `-`
        `Type:` Constructor
        """

        self.screen_width, self.screen_height = pyautogui.size() # useful screen size so that all tests are feasible on any type of screen

        # Initializing controls
        self.mouse = MouseController()
        self.keyboard = KeyboardController()

    def read_test_file(self, file_name: str):
        """ `+`
        `Type:` Procedure
        `Description:` read all lines from test file
        :param:`file_name:` name of the file to read
        """

        file_path = CONSTANT_TESTS_FOLDER_PATH + "\\" + file_name

        try:
            test_file = open(file_path, "r")

            # Read the first line by itself because there are no prior instructions to know the waiting time
            first_line = test_file.readline()
            first_word_list = first_line.split(";") # Split the sentence for easier manipulation
            self.__find_action(first_word_list, []) 

            before_word_list = first_word_list # We store the line before to know the waiting time between each instruction

            time.sleep(1)

            # We do the same for all the lines of the file
            for line in test_file:
                now_word_list = line.split(";")
                self.__find_action(now_word_list, before_word_list)
                before_word_list = now_word_list
        except Exception as e:
            tkinter.messagebox.showinfo('ERROR File',e)


    def __find_action(self, now_word_list: list, before_word_list: list):
        """ `-`
        `Type:` Procedure
        `Description:` find the action to do based on the first word in the list now_word_list
        :param:`now_word_list:` list of words of the instruction being executed
        :param:`before_word_list:` list of words of the instruction to be executed (useful to know the time between the two actions)
        """

        first_word = now_word_list[0] # the first word in the list contains the action to be done

        if first_word == "Click" or first_word == "Release":
            self.__click_input(now_word_list, before_word_list) 
        if first_word == "Key":
            self.__key_input(now_word_list, before_word_list)
        if first_word == "Scroll":
            self.__scroll_input(now_word_list, before_word_list)
        if first_word == "Move":
            self.__move_input(now_word_list, before_word_list)


    def __click_input(self, now_word_list: list, before_word_list: list):
        """ `-`
        `Type:` Procedure
        `Description:` simulates click action with mouse
        :param:`now_word_list:` list of words of the instruction being executed
        :param:`before_word_list:` list of words of the instruction to be executed (useful to know the time between the two actions)
        """

        # waiting time before doing the instructions so as not to go too fast
        if before_word_list != []:
            wait_time = self.__find_wait_time(now_word_list, before_word_list)
            time.sleep(wait_time)

        action = now_word_list[0]
        button = now_word_list[1]
        nx = now_word_list[2]
        ny = now_word_list[3]

        # x, y depending on screen size
        x = float(nx) * self.screen_width
        y = float(ny) * self.screen_height

        # Click or Release
        if action == "Click":
            if button == "left":
                self.mouse.position = (x,y)
                self.mouse.press(Button.left)

            if button == "right":
                self.mouse.position = (x,y)
                self.mouse.press(Button.right)

            if button == "middle":
                self.mouse.position = (x,y)
                self.mouse.press(Button.middle)
        else :
            if button == "left":
                self.mouse.position = (x,y)
                self.mouse.release(Button.left)

            if button == "right":
                self.mouse.position = (x,y)
                self.mouse.release(Button.right)

            if button == "middle":
                self.mouse.position = (x,y)
                self.mouse.release(Button.middle)


    def __key_input(self, now_word_list: list, before_word_list: list):
        """ `-`
        `Type:` Procedure
        `Description:` simulates the action of writing with the keyboard
        :param:`now_word_list:` list of words of the instruction being executed
        :param:`before_word_list:` list of words of the instruction to be executed (useful to know the time between the two actions)
        """

        # waiting time before doing the instructions so as not to go too fast
        if before_word_list != []:
            wait_time = self.__find_wait_time(now_word_list, before_word_list)
            time.sleep(wait_time)

        key_char = now_word_list[1]

        if key_char != "None":
            key = KeyTranslation(key_char).get_key() # translate string to Key or KeyCode

            if key == Key.print_screen:
                Screenshot()
            else:
                self.keyboard.press(key)
                time.sleep(1)
                self.keyboard.release(key)


    def __scroll_input(self, now_word_list: list, before_word_list: list):
        """ `-`
        `Type:` Procedure
        `Description:` simulates the action of scrolling with the mouse
        :param:`now_word_list:` list of words of the instruction being executed
        :param:`before_word_list:` list of words of the instruction to be executed (useful to know the time between the two actions)
        """

        # waiting time before doing the instructions so as not to go too fast
        if before_word_list != []:
            if before_word_list[0] != "Scroll":
                wait_time = self.__find_wait_time(now_word_list, before_word_list)
                time.sleep(wait_time)

        nx = now_word_list[1]
        ny = now_word_list[2]
        dx = now_word_list[3]
        dy = now_word_list[4]

        # x, y depending on screen size
        x = float(nx) * self.screen_width
        y = float(ny) * self.screen_height

        self.mouse.position = (x, y)
        self.mouse.scroll(dx, dy)


    def __move_input(self, now_word_list: list, before_word_list: list):
        """ `-`
        `Type:` Procedure
        `Description:` simulates the action of moving with the mouse
        :param:`now_word_list:` list of words of the instruction being executed
        :param:`before_word_list:` list of words of the instruction to be executed (useful to know the time between the two actions)
        """

        # waiting time before doing the instructions so as not to go too fast
        if before_word_list != []:
            if before_word_list[0] != "Move":
                wait_time = self.__find_wait_time(now_word_list, before_word_list)
                time.sleep(wait_time)

        nx = now_word_list[1]
        ny = now_word_list[2]

        # x, y depending on screen size
        x = float(nx) * self.screen_width
        y = float(ny) * self.screen_height

        self.mouse.move(int(x), int(y))


    def __find_wait_time(self, now_word_list: list, before_word_list: list) -> float:
        """ `-`
        `Type:` Fonction
        `Description:` finds the time it took the user to do two actions which corresponds to the waiting time
        :param:`now_word_list:` list of words of the instruction being executed
        :param:`before_word_list:` list of words of the instruction to be executed (useful to know the time between the two actions)
        `Return:` time in float
        """

        now_time = self.__find_time_position(now_word_list)
        before_time = self.__find_time_position(before_word_list)

        wait_time = now_time - before_time # waiting time calculation

        return wait_time
    

    def __find_time_position(self, word_list: list) -> float:
        """ `-`
        `Type:` Function
        `Description:` finds where the time is positioned in the character string according to the action performed
        :param:`word_list:` list of words of the instruction being executed
        `Return:` time in float
        """

        word = word_list[0]

        # finds the position of the time in the character string according to the action
        if word == "Click" or word == "Release":
            time = word_list[4]
        else:
            if word == "Key":
                time = word_list[2]
            else:
                if word == "Move":
                    time = word_list[3]
                else:
                    time = word_list[5]

        return float(time)