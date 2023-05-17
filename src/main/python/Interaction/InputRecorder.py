# Author        : Victor BROSSARD
# Description   : Object that saves all actions that the user does in a file

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
import time
import pyautogui

from pynput import keyboard
from pynput import mouse
from pynput.mouse import Button

from Interaction.KeyTranslation import KeyTranslation

from FilesManagement.Files.ManipulationSettingsFile import ManipulationSettingsFile
from FilesManagement.Files.ManageAnyFile import ManageAnyFile

from Useful.AllConstant import CONSTANT_KEYBOARD_SHORTCUTS

#-----------------------------------------------------------------------------------------------------

class InputRecorder(object):
    """ `+`
    :class:`InputRecorder` saves all actions that the user does in a file
    """

    def __init__(self, name: str, path: str):
        """ `-`
        `Type:` Constructor
        :param:`name:` name of the file to be saved
        :param:`path:` path where we save it
        """

        self.running = False # lets you know if you are recording or not
        self.name_file = f"{name}.txt"
        self.was_file_created = False
        self.file_path = f"{path}\\{self.name_file}"

        self.current_hotkey = []
        self.translate = KeyTranslation()

        self.screen_width, self.screen_height = pyautogui.size() # useful screen size so that all tests are feasible on any type of screen
        
        # Create the file
        ManageAnyFile().create_file(path, self.name_file, [])
        self.was_file_created = True

        # Open the file to write to
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
            # Loop that prevents the code from stopping until you stop
            time.sleep(1)

        

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

            
    def __on_keyboard_press(self, key):
        """ `-`
        `Type:` Procedure
        `Description:` recording of the key press
        :param:`key:` keyboard key
        """

        try:
            key_name = key.char
        except AttributeError:
            key_name = key.name

        # if we keep pressing alt or ctrl or cmd, we are in a key combination
        # so we first register one of these keys in our list of current keys then we register the other keys
        # otherwise we do nothing here
        if key_name in CONSTANT_KEYBOARD_SHORTCUTS and self.current_hotkey == []:
            self.current_hotkey.append(key_name)

        if self.current_hotkey != [] and key_name not in self.current_hotkey and key_name not in CONSTANT_KEYBOARD_SHORTCUTS:
            if self.current_hotkey[0] == 'ctrl' or self.current_hotkey[0] == 'ctrl_l' or self.current_hotkey[0] == 'ctrl_r':
                # case where the key combination returns a key in the form '\x..' because of pynput which has problems when you do ctrl+...
                # so we save the key as a string to better handle it after
                self.current_hotkey.append(str(key))
            else:
                self.current_hotkey.append(key_name)


    def __on_keyboard_release(self, key):
        """ `-`
        `Type:` Procedure
        `Description:` recording of the key release
        :param:`key:` keyboard key  
        """

        try:
            key_name = key.char
        except AttributeError:
            key_name = key.name

        if self.current_hotkey != []:
            # case we are in a key combination
            self.__write_hotkey()
        else:
            if key_name not in CONSTANT_KEYBOARD_SHORTCUTS:             # we prevent to simply write the ctrl, alt or cmd keys because they are just used to make keyboard shortcuts
                if key_name == ManipulationSettingsFile().get_line(5):  # key that stops recording
                    self.__write_in_file(f"Key;{key_name}")
                    self.__stop_recording() 
                else:
                    if key_name == None: # numpad key when in num_lock
                        new_key_name = KeyTranslation().find_numpad(str(key))
                        self.__write_in_file(f"Key;{new_key_name}")
                    else:
                        self.__write_in_file(f"Key;{key_name}")
        
        self.current_hotkey = []


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

        self.__write_in_file(f"Move;{norm_x};{norm_y}")
        

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
    

    def __write_hotkey(self):
        """ `-`
        `Type:` Procedure
        `Description:` write the action to the file in case we are in a key combination
        """

        str_list = []

        # traversal of all the keys present in the combination
        for k in self.current_hotkey:
            if k in CONSTANT_KEYBOARD_SHORTCUTS:
                str_list.append(k)
            else:
                if self.current_hotkey[0] == 'ctrl' or self.current_hotkey[0] == 'ctrl_l' or self.current_hotkey[0] == 'ctrl_r':
                    # the value to save is normally of the form '\x..' but since we put it in string, it is now of the form "'\x..'"
                    # so we remove the first two characters to avoid any problems later
                    # this only happens for ctrl+... type shortcuts
                    str_list.append(k[2:]) 
                else:
                    str_list.append(k)

        # check in case we just press ctrl or cmd or alt
        if len(str_list) > 1:
            action = self.__translate_hotkey(str_list) # put the combination in the form <alt>+... which is accepted by pynput
            self.__write_in_file(f"Key;{action}")
    

    def __translate_hotkey(self, combinations_list: list) -> str:
        """ `-`
        `Type:` Function
        `Description:` transforms a list of key combinations into a string respecting the form <ctrl>+<alt>+'c'
        :param:`combinations_list:` string key list
        `Return:` string respecting the form <ctrl>+<alt>+'c'
        """

        final_str = ''
        action_len = len(combinations_list)

        # go through the list of keys
        for i in range(0, action_len):
            if combinations_list[i] in CONSTANT_KEYBOARD_SHORTCUTS: # when the key is ctrl, alt or cmd
                if i == action_len-1: # last item in the list
                    final_str += f'<{combinations_list[i]}>'
                else:
                    final_str += f'<{combinations_list[i]}>+'
            else:
                # will look for the translation of the key combination if we start with ctrl then the form will be x.. otherwise the form will be the normal key
                key_char = self.translate.find_combination(combinations_list[i])

                if i == action_len-1: # last item in the list
                    final_str += f'{key_char}'
                else:
                    final_str += f'{key_char}+'

        return final_str