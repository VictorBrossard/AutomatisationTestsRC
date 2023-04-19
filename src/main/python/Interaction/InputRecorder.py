# Author        : Victor BROSSARD
# Description   : 

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import os
import time
import subprocess

from pynput import keyboard
from pynput import mouse
from FilesManagement.InitFolders import CONSTANT_TESTS_FOLDER_PATH

#-----------------------------------------------------------------------------------------------------
#
class InputRecorder:

    # Constructor
    def __init__(self, name, folder_path):
        #
        self.folder_path = folder_path
        self.name_file = name + ".txt"

        # Create file
        os.chdir(CONSTANT_TESTS_FOLDER_PATH) # Change the current working directory by giving the path
        subprocess.run(['type', 'nul', '>', self.name_file], shell=True)

        #
        self.file_path = self.folder_path + "\\" + self.name_file
        self.file = open(self.file_path, "w")
        
        #
        self.mouse_listener = mouse.Listener(on_click=self.on_mouse_click)
        self.keyboard_listener = keyboard.Listener(on_press=self.on_keyboard_press)

    # 
    def start_record(self):
        self.mouse_listener.start()
        self.keyboard_listener.start()
        
    #
    def stop_record(self):
        self.mouse_listener.stop()
        self.keyboard_listener.stop()
        self.file.close()
        
    #
    def on_mouse_click(self, x, y, button, pressed):
        button_name = button.name
        if pressed:
            self.write_in_file(f"Click;{button_name};{x};{y}")

        #action = "Click" if pressed else "Release"
        #self.write_in_file(f"{action};{button_name};{x};{y}")
        
    #
    def on_keyboard_press(self, key):
        try:
            key_name = key.char
        except AttributeError:
            key_name = key.name
        
        self.write_in_file(f"Key;{key_name}")

        if key_name == 'a': self.stop_record() 
        
    #
    def write_in_file(self, message):
        self.file.write(f"{message}\n")

