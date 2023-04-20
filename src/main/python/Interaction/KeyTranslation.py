# Author        : Victor BROSSARD
# Description   : 

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution
from pynput.keyboard import Key
from pynput.keyboard import KeyCode
from UsefulFunction.UsefulFunction import starts_with

#-----------------------------------------------------------------------------------------------------

class KeyTranslation(object):

    def __init__(self, chr):
        """
        Constructor
        """
        self.key = self.__find_correct_key(chr)


    def get_key(self):
        return self.key
    

    def __find_correct_key(self, chr):

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

        
    def __alt(self, chr):
        """
        Map a string to a corresponding Key object.
        """
        
        keys = {
            "alt": Key.alt,
            "alt_l": Key.alt_l,
            "alt_r": Key.alt_r,
            "alt_gr": Key.alt_gr
        }

        if chr in keys:
            return keys[chr] 
        
    
    def __cmd(self, chr):
        """
        Map a string to a corresponding Key object.
        """
        
        keys = {
            "cmd": Key.cmd,
            "cmd_l": Key.cmd_l,
            "cmd_r": Key.cmd_r
        }

        if chr in keys:
            return keys[chr] 
        

    def __ctrl(self, chr):
        """
        Map a string to a corresponding Key object.
        """
        
        keys = {
            "ctrl": Key.ctrl,
            "ctrl_l": Key.ctrl_l,
            "ctrl_r": Key.ctrl_r
        }

        if chr in keys:
            return keys[chr] 
        

    def __f(self, chr):
        """
        Map a string to a corresponding Key object.
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
        

    def __page(self, chr):
        """
        Map a string to a corresponding Key object.
        """
        
        keys = {
            "page_down": Key.page_down,
            "page_up": Key.page_up
        }

        if chr in keys:
            return keys[chr] 
        
        
    def __shift(self, chr):
        """
        Map a string to a corresponding Key object.
        """

        keys = {
            "shift": Key.shift,
            "shift_l": Key.shift_l,
            "shift_r": Key.shift_r
        }

        if chr in keys:
            return keys[chr] 