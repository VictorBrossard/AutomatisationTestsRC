# Author        : Victor BROSSARD
# Description   : Object that transforms the keys given in string into Key or Keycode

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
from pynput.keyboard import Key
from pynput.keyboard import KeyCode

from Useful.UsefulFunction import starts_with

#-----------------------------------------------------------------------------------------------------

class KeyTranslation(object):
    """ `+`
    :class:`KeyTranslation` transforms the keys given in string into Key or Keycode
    """

    def __init__(self):
        """ `-`
        `Type:` Constructor
        """

        pass
    

    def find_correct_key(self, chr: str) -> (Key | KeyCode):
        """ `+`
        `Type:` Function
        `Description:` looks for the translation of in Key or KeyCode of the key in string
        :param:`chr:` key in string
        `Return:` Key or KeyCode
        """

        key_map = {
            "backspace": Key.backspace,
            "caps_lock": Key.caps_lock,
            "delete": Key.delete,
            "down": Key.down,
            "end": Key.end,
            "enter": Key.enter,
            "esc": Key.esc,
            "home": Key.home,
            "insert": Key.insert,
            "left": Key.left,
            "menu": Key.menu,
            "num_lock": Key.num_lock,
            "pause": Key.pause,
            "print_screen": Key.print_screen,
            "right": Key.right,
            "scroll_lock": Key.scroll_lock,
            "space": Key.space,
            "tab": Key.tab,
            "up": Key.up
        }
    
        if chr in key_map:
            return key_map[chr]

        if starts_with(chr, "alt"):
            return self.__alt(chr)

        if starts_with(chr, "cmd"):
            return self.__cmd(chr)

        if starts_with(chr, "ctrl"):
            return self.__ctrl(chr)

        if starts_with(chr, "f"):
            return self.__f(chr)

        if starts_with(chr, "page"):
            return self.__page(chr)

        if starts_with(chr, "shift"):
            return self.__shift(chr)

        if starts_with(chr, "numpad"):
            return self.__numpad(chr)

        return KeyCode(char=chr)

        
    def __alt(self, chr: str) -> Key:
        """ `-`
        `Type:` Function
        `Description:` looks for the translation of in Key or KeyCode of the key in string starting with alt
        :param:`chr:` key in string
        `Return:` Key
        """
        
        keys = {
            "alt": Key.alt,
            "alt_l": Key.alt_l,
            "alt_r": Key.alt_r,
            "alt_gr": Key.alt_gr
        }

        if chr in keys:
            return keys[chr] 
        
    
    def __cmd(self, chr: str) -> Key:
        """ `-`
        `Type:` Function
        `Description:` looks for the translation of in Key or KeyCode of the key in string starting with cmd
        :param:`chr:` key in string
        `Return:` Key
        """
        
        keys = {
            "cmd": Key.cmd,
            "cmd_l": Key.cmd_l,
            "cmd_r": Key.cmd_r
        }

        if chr in keys:
            return keys[chr] 
        

    def __ctrl(self, chr: str) -> Key:
        """ `-`
        `Type:` Function
        `Description:` looks for the translation of in Key or KeyCode of the key in string starting with ctrl
        :param:`chr:` key in string
        `Return:` Key
        """
        
        keys = {
            "ctrl": Key.ctrl,
            "ctrl_l": Key.ctrl_l,
            "ctrl_r": Key.ctrl_r
        }

        if chr in keys:
            return keys[chr] 
        

    def __f(self, chr: str) -> Key:
        """ `-`
        `Type:` Function
        `Description:` looks for the translation of in Key or KeyCode of the key in string starting with f
        :param:`chr:` key in string
        `Return:` Key
        """

        keys = {
            "f1": Key.f1,
            "f2": Key.f2,
            "f3": Key.f3,
            "f4": Key.f4,
            "f5": Key.f5,
            "f6": Key.f6,
            "f7": Key.f7,
            "f8": Key.f8,
            "f9": Key.f9,
            "f10": Key.f10,
            "f11": Key.f11,
            "f12": Key.f12
        }

        if chr in keys:
            return keys[chr]
        

    def __page(self, chr: str) -> Key:
        """ `-`
        `Type:` Function
        `Description:` looks for the translation of in Key or KeyCode of the key in string starting with page
        :param:`chr:` key in string
        `Return:` Key
        """
        
        keys = {
            "page_down": Key.page_down,
            "page_up": Key.page_up
        }

        if chr in keys:
            return keys[chr] 
        
        
    def __shift(self, chr: str) -> Key: 
        """ `-`
        `Type:` Function
        `Description:` looks for the translation of in Key or KeyCode of the key in string starting with shift
        :param:`chr:` key in string
        `Return:` Key
        """

        keys = {
            "shift": Key.shift,
            "shift_l": Key.shift_l,
            "shift_r": Key.shift_r
        }

        if chr in keys:
            return keys[chr]
        

    def find_combination(self, chr: str) -> KeyCode:
        """ `+`
        `Type:` Function
        `Description:` find the correct letter for the key combination with ctrl at the beginning
        :param:`chr:` key in string
        `Return:` the correct string
        """

        # use of a dictionary because the values returned by pynput, for key combinations like ctrl+... , are in the form x..
        key_map = {
            "x01'": 'a',
            "x03'": 'c',
            "x16'": 'v',
            "x18'": 'x',
            "x1a'": 'z',
            "x19'": 'y',
            "x0e'": 'n',
            "x0f'": 'o',
            "x13'": 's',
            "x06'": 'f',
            "x14'": 't',
            "x17'": 'w',
            "x10'": 'p',
            "x11'": 'q'
        }
    
        if chr in key_map:
            return key_map[chr]
        else:
            return chr
        

    def find_numpad(self, chr: str) -> str:
        """ `+`
        `Type:` Function
        `Description:` find the correct translation for numpad keys when in num_lock
        :param:`chr:` key in string
        `Return:` the correct string
        """

        key_map = {
            "<96>": '0',
            "<97>": '1',
            "<98>": '2',
            "<99>": '3',
            "<100>": '4',
            "<101>": '5',
            "<102>": '6',
            "<103>": '7',
            "<104>": '8',
            "<105>": '9',
            "<110>": '.'
        }
    
        if chr in key_map:
            return key_map[chr]