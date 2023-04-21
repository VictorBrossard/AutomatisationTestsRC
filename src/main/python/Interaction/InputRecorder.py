# Author        : Victor BROSSARD
# Description   : Object that saves all actions that the user does in a file

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import os
import time
import subprocess

from pynput import keyboard
from pynput import mouse
from pynput.mouse import Button
from pynput.keyboard import Key
from pynput.keyboard import KeyCode
from FilesManagement.InitFolders import CONSTANT_TESTS_FOLDER_PATH

#-----------------------------------------------------------------------------------------------------
#
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

        # Create the file
        os.chdir(CONSTANT_TESTS_FOLDER_PATH) # Change the current working directory by giving the path
        subprocess.run(['type', 'nul', '>', self.name_file], shell=True)

        # Open the file to write to
        self.file_path = CONSTANT_TESTS_FOLDER_PATH + "\\" + self.name_file
        self.file = open(self.file_path, "w")
        
        # Initialization of objects that let you know what the user is doing
        self.mouse_listener = mouse.Listener(on_click=self.__on_mouse_click, on_scroll=self.__on_scroll)
        self.keyboard_listener = keyboard.Listener(on_press=self.__on_keyboard_press)


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

        # Checking if it is pressed and not maintained
        if pressed:
            self.__write_in_file(f"Click;{button_name};{x};{y}")

        if button == mouse.Button.middle:
            self.__write_in_file(f"Click;middle;{x};{y}")

        ##################action = "Click" if pressed else "Release"
        

    def __on_keyboard_press(self, key: (Key | KeyCode | None)):
        """ `-`
        `Type:` Procedure
        `Description:` recording of the key pressed
        :param:`key:` keyboard key pressed
        """

        if key_name == 'tab': # key that stops recording
            self.__stop_recording() 
        else:
            try:
                key_name = key.char
            except AttributeError:
                key_name = key.name
        
            self.__write_in_file(f"Key;{key_name}")


    def __on_scroll(self, x: int, y: int, dx: int, dy: int):
        """ `-`
        `Type:` Procedure
        `Description:` scroll record
        :param:`x:` x-coordinate
        :param:`y:` y-coordinate
        :param:`dx:` dx-coordinate
        :param:`dy:` dy-coordinate
        """

        self.__write_in_file(f"Scroll;{x};{y};{dx};{dy}")
        

    def __write_in_file(self, message: str):
        """ `-`
        `Type:` Procedure
        `Description:` writes in the file the action done by adding the time in seconds of when it was done
        :param:`message:` instruction made by the user
        """

        now = time.time()
        self.file.write(f"{message};{now}\n")
        self.file.flush() # force writing the entire contents of the file's buffer to the hard disk

