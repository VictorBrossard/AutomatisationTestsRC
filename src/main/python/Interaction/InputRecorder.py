# Author        : Victor BROSSARD
# Description   : Object that saves all actions that the user does in a file

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import os
import time
import subprocess
import tkinter.messagebox
import pyautogui

from pynput import keyboard
from pynput import mouse
from pynput.mouse import Button
from pynput.keyboard import Key
from pynput.keyboard import KeyCode
from FilesManagement.ManipulationSettingsFile import ManipulationSettingsFile

from FilesManagement.InitFolders import CONSTANT_TESTS_FOLDER_PATH

#-----------------------------------------------------------------------------------------------------

class InputRecorder(object):
    """ `+`
    :class:`InputRecorder` saves all actions that the user does in a file
    """

    def __init__(self, name: str):
        """ `-`
        `Type:` Constructor
        """

        self.running = False # lets you know if you are recording or not
        self.name_file = name + ".txt"
        self.was_file_created = False
        self.current_combination = []

        self.screen_width, self.screen_height = pyautogui.size() # useful screen size so that all tests are feasible on any type of screen

        # Check if the file exists
        if os.path.exists(CONSTANT_TESTS_FOLDER_PATH + '\\' + self.name_file):
            tkinter.messagebox.showinfo('ERROR file name','The file already exists')    # Displaying the error message for the user
            return
        
        # Create the file
        os.chdir(CONSTANT_TESTS_FOLDER_PATH)
        subprocess.run(['type', 'nul', '>', self.name_file], shell=True)
        self.was_file_created = True

        # Open the file to write to
        self.file_path = CONSTANT_TESTS_FOLDER_PATH + "\\" + self.name_file
        self.file = open(self.file_path, "w")
        
        # Initialization of objects that let you know what the user is doing
        self.mouse_listener = mouse.Listener(on_move=self.__on_move, on_click=self.__on_mouse_click, on_scroll=self.__on_scroll)
        self.keyboard_listener = keyboard.Listener(on_press=self.__on_keyboard_press, on_release=self.__on_keyboard_release)


    def start_recording(self):
        """ `+`
        `Type:` Procedure
        `Description:` starts recording user actions
        """
        
        self.running = True
        self.mouse_listener.start()
        self.keyboard_listener.start()

        while self.running:
            pass # Loop that prevents the code from stopping until you stop
        

    def __stop_recording(self):
        """ `-`
        `Type:` Procedure
        `Description:` stop recording user actions
        """

        self.mouse_listener.stop()
        self.keyboard_listener.stop()
        self.file.close()
        self.running = False
        

    def __on_mouse_click(self, x: int, y: int, button: Button, pressed: bool):
        """ `-`
        `Type:` Procedure
        `Description:` at each click we save the coordinates of the click, the button used and if it is pressed or held
        :param:`x:` x-coordinate
        :param:`y:` y-coordinate
        :param:`button:` mouse button pressed
        :param:`pressed:` pressed or held
        """

        button_name = button.name
        norm_x = x / self.screen_width
        norm_y = y / self.screen_height

        # Checking if it is pressed and not maintained
        if pressed:
            if button == mouse.Button.middle:
                self.__write_in_file(f"Click;middle;{norm_x};{norm_y}")
            else:
                self.__write_in_file(f"Click;{button_name};{norm_x};{norm_y}")
        else:
            self.__write_in_file(f"Release;{button_name};{norm_x};{norm_y}")
        

    def __on_keyboard_press(self, key: (Key | KeyCode | None)):
        """ `-`
        `Type:` Procedure
        `Description:` recording of the key pressed
        :param:`key:` keyboard key pressed
        """

        try:
            key_name = key.char
        except AttributeError:
            key_name = key.name

        try:
            if self.current_combination == [] and key_name in self.key_combinations:
                self.current_combination.append(key_name)
                print(self.current_combination)
                return 
        except KeyError:
            pass

        if self.current_combination != []:
            try:
                print(key_name)
                print(self.key_combinations[self.current_combination[0]][key_name])
                combination = self.key_combinations[self.current_combination[0]][key_name]
                self.current_combination.append(key)
                print(self.current_combination)
            except KeyError:
                pass

        
    def __on_keyboard_release(self, key: (Key | KeyCode | None)):
        """ `-`
        `Type:` Procedure
        `Description:` recording of the key release
        :param:`key:` keyboard key released
        """

        try:
            key_name = key.char
        except AttributeError:
            key_name = key.name

        if key_name == ManipulationSettingsFile().get_test_stop_key(): # key that stops recording
            self.__stop_recording() 
        else:
            self.__write_in_file(f"Key;{key_name}")

        self.current_combination = []


    def __on_scroll(self, x: int, y: int, dx: int, dy: int):
        """ `-`
        `Type:` Procedure
        `Description:` scroll record
        :param:`x:` x-coordinate
        :param:`y:` y-coordinate
        :param:`dx:` dx-coordinate
        :param:`dy:` dy-coordinate
        """

        norm_x = x / self.screen_width
        norm_y = y / self.screen_height

        self.__write_in_file(f"Scroll;{norm_x};{norm_y};{dx};{dy}")


    def __on_move(self, x: int, y: int):
        """ `-`
        `Type:` Procedure
        `Description:` Move record
        :param:`x:` x-coordinate
        :param:`y:` y-coordinate
        """

        norm_x = x / self.screen_width
        norm_y = y / self.screen_height

        #self.__write_in_file(f"Move;{norm_x};{norm_y}")
        

    def __write_in_file(self, message: str):
        """ `-`
        `Type:` Procedure
        `Description:` writes in the file the action done by adding the time in seconds of when it was done
        :param:`message:` instruction made by the user
        """

        now = time.time()
        self.file.write(f"{message};{now}\n")
        self.file.flush() # force writing the entire contents of the file's buffer to the hard disk


    def get_was_file_created(self):
        """ `+`
        `Type:` Function
        `Description:` Getter that returns the variable file_was_created 
        `Return:` True or False
        """
        return self.was_file_created
    

    key_combinations = {
        'ctrl_l': {
            'a': 'ctrl+a',
            'c': 'ctrl+c',
            'v': 'ctrl+v',
            'x': 'ctrl+x',
            'z': 'ctrl+z',
            'y': 'ctrl+y',
            'n': 'ctrl+n',
            'o': 'ctrl+o',
            's': 'ctrl+s',
            'f': 'ctrl+f',
            't': 'ctrl+t',
            'w': 'ctrl+w',
            'p': 'ctrl+p',
            'q': 'ctrl+q'
        },
        'ctrl_r': {
            'a': 'ctrl+a',
            'c': 'ctrl+c',
            'v': 'ctrl+v',
            'x': 'ctrl+x',
            'z': 'ctrl+z',
            'y': 'ctrl+y',
            'n': 'ctrl+n',
            'o': 'ctrl+o',
            's': 'ctrl+s',
            'f': 'ctrl+f',
            't': 'ctrl+t',
            'w': 'ctrl+w',
            'p': 'ctrl+p',
            'q': 'ctrl+q'
        },
        'alt_l': {
            'f4': 'alt+f4',
            'tab': 'alt+tab',
            'space': 'alt+space',
            'left': 'alt+left',
            'right': 'alt+right',
            'up': 'alt+up',
            'down': 'alt+down',
            'enter': 'alt+enter',
            'f': 'alt+f',
            'e': 'alt+e',
            'd': 'alt+d',
            'p': 'alt+p',
            'q': 'alt+q',
            'r': 'alt+r',
            's': 'alt+s'
        },
        'alt_r': {
            'f4': 'alt+f4',
            'tab': 'alt+tab',
            'space': 'alt+space',
            'left': 'alt+left',
            'right': 'alt+right',
            'up': 'alt+up',
            'down': 'alt+down',
            'enter': 'alt+enter',
            'f': 'alt+f',
            'e': 'alt+e',
            'd': 'alt+d',
            'p': 'alt+p',
            'q': 'alt+q',
            'r': 'alt+r',
            's': 'alt+s'
        },
        'cmd': {
            'c': 'cmd+c',
            'v': 'cmd+v',
            'x': 'cmd+x',
            'z': 'cmd+z',
            'y': 'cmd+y',
            'n': 'cmd+n',
            'o': 'cmd+o',
            's': 'cmd+s',
            'f': 'cmd+f',
            't': 'cmd+t',
            'w': 'cmd+w',
            'p': 'cmd+p',
            'q': 'cmd+q'
        }
    }