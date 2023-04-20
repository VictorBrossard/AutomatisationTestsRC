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
    def __init__(self, name):
        #
        self.running = False
        self.name_file = name + ".txt"

        # Create file
        os.chdir(CONSTANT_TESTS_FOLDER_PATH) # Change the current working directory by giving the path
        subprocess.run(['type', 'nul', '>', self.name_file], shell=True)

        #
        self.file_path = CONSTANT_TESTS_FOLDER_PATH + "\\" + self.name_file
        self.file = open(self.file_path, "w")
        
        #
        self.mouse_listener = mouse.Listener(on_click=self.__on_mouse_click, on_scroll=self.__on_scroll)
        self.keyboard_listener = keyboard.Listener(on_press=self.__on_keyboard_press)

    # 
    def start_record(self):
        self.running = True
        self.mouse_listener.start()
        self.keyboard_listener.start()

        while self.running:
            pass ##### Boucle qui empêche le code de s'arrêter tant qu'on a pas fait stop
        
    #
    def __stop_record(self):
        self.mouse_listener.stop()
        self.keyboard_listener.stop()
        self.file.close()
        self.running = False
        
    #
    def __on_mouse_click(self, x, y, button, pressed):
        button_name = button.name
        if pressed:
            self.__write_in_file(f"Click;{button_name};{x};{y}")
        if button == mouse.Button.middle:
            self.__write_in_file(f"Click;middle;{x};{y}")

        ##################action = "Click" if pressed else "Release"
        
    #
    def __on_keyboard_press(self, key):
        try:
            key_name = key.char
        except AttributeError:
            key_name = key.name
        
        self.__write_in_file(f"Key;{key_name}")

        if key_name == 'a': self.__stop_record()

    def __on_scroll(self, x, y, dx, dy):
        self.__write_in_file(f"Scroll;{x};{y};{dx};{dy}")
        
    #
    def __write_in_file(self, message):
        now = time.time()
        self.file.write(f"{message};{now}\n")
        self.file.flush() #  forcer l'écriture de tout le contenu du tampon du fichier sur le disque dur.

