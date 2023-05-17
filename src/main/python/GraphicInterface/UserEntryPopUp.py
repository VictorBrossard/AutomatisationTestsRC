# Author        : Victor BROSSARD
# Description   : GUI pop-up to request something to the user

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
import tkinter as tk
import ctypes

from tkinter import ttk

from GraphicInterface.MessageBox import MessageBox

from Useful.UsefulFunction import cant_close
from Useful.UsefulFunction import validate_int

#-----------------------------------------------------------------------------------------------------

class UserEntryPopUp(tk.Tk):
    """ `+`
    :class:`UserEntryPopUp` handles user interaction through a pop-up
    """

    def __init__(self, name: str, label_list: list[str], widget_list: list[int], combobox_list: list[list[str]] | None = None):
        """ `-`
        `Type:` Constructor
        :param:`name:` pop-up name
        :param:`label_list:` explanations of what is required of the user
        :param:`widget_list:` list of integers with a number between 0 and 3 at index i where i is the index of the label associated with the future widget to create
                        - "0" = text entry
                        - "1" = integer entry
                        - "2" = comboboxs
                        - "3" = limited text entry
        :param:`combobox_list:` list of combobox values
        """

        # Parent constructor
        super().__init__()
            
        # Interface initialization
        self.title(name)
        self.protocol("WM_DELETE_WINDOW", cant_close)   # Prevents the window from being closed by the red cross
        self.wm_attributes("-topmost", True)            # Prioritize the window

        # Variables that stores the value given by the user
        self.user_entries = []
        self.nb_entries = len(label_list)
        self.nb_combobox = 0

        # Configuring the placement of interface objects
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        # Adds interface objects to the interface
        self.__implementation(label_list, widget_list, combobox_list)


    def __implementation(self, label_list: list[str], widget_list: list[int], combobox_list: list[list[str]]):
        """ `-`
        `Type:` Procedure
        `Description:` adds interface objects to the interface
        :param:`label_list:` explanations of what is required of the user
        :param:`widget_list:` list of integers with a number between 0 and 3 at index i where i is the index of the label associated with the future widget to create
                        - "0" = text entry
                        - "1" = integer entry
                        - "2" = comboboxs
                        - "3" = limited text entry
        :param:`combobox_list:` list of combobox values
        """

        # Canvas
        canvas = tk.Canvas(self)

        # Frame
        entry_frame = ttk.Frame(canvas)

        # Label and Entry
        for i in range(0, self.nb_entries):
            # Label
            text_label = ttk.Label(entry_frame, text=label_list[i]) # Creation of the label
            text_label.pack(side=tk.TOP, pady=2)                    # Object position

            # Entry
            if widget_list[i] == 1:
                self.user_entries.append(tk.StringVar()) # Variable that stores the value given by the user
                self.__create_int_entry(entry_frame, self.user_entries[i])
            elif widget_list[i] == 2:
                self.__create_combobox(entry_frame, combobox_list[self.nb_combobox])
                self.nb_combobox = self.nb_combobox + 1
            elif widget_list[i] == 3:
                self.user_entries.append(tk.StringVar()) # Variable that stores the value given by the user
                self.__create_limited_entry(entry_frame, self.user_entries[i])
            else:
                self.user_entries.append(tk.StringVar()) # Variable that stores the value given by the user
                self.__create_text_entry(entry_frame, self.user_entries[i])

        # Button
        ok_button = ttk.Button(entry_frame, text='OK', command=self.__close_pop_up) # Creation of the button
        ok_button.pack(side=tk.TOP, pady=10)                                        # Object position

        # Scrollbar
        scrollbar_x = tk.Scrollbar(self, orient=tk.HORIZONTAL, command=canvas.xview)
        scrollbar_x.pack(side=tk.TOP, fill=tk.X)
        canvas.config(xscrollcommand=scrollbar_x.set)

        canvas.create_window(0, 0, window=entry_frame, anchor='nw')
        canvas.pack(side=tk.TOP)
        entry_frame.pack(side=tk.TOP)

        # Configurer le canvas pour agir sur la barre de défilement
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
        canvas.bind('<MouseWheel>', lambda e: canvas.yview_scroll(int(-1*(e.delta/120)), "units"))

        self.__init_size()


    def __init_size(self):
        """ `-`
        `Type:` Procedure
        `Description:` manages the size of the interface according to the number of entries
        """

        # Window size and position
        height = 500
        width = self.nb_entries * 60 + 75
        user32 = ctypes.windll.user32                               # User information
        x = int((user32.GetSystemMetrics(0) / 2) - (height / 2))    # int() = any type to int
        y = int((user32.GetSystemMetrics(1) / 2) - (width / 2))     # user32.GetSystemMetrics() = screen size (0 = height and 1 = width)

        self.geometry(str(height) + "x" + str(width) + "+" + str(x) + "+" + str(y))     # Set window size and position | str() = type to string
        self.resizable(width=0, height=0)                                               # Prevents any modification of window size


    def __create_text_entry(self, frame: ttk.Frame, val: tk.StringVar):
        """ `-`
        `Type:` Procedure
        `Description:` creates a text entry for the user
        :param:`frame:` frame of the interface where the entry is displayed
        :param:`val:` input value
        """

        text_entry = ttk.Entry(frame, textvariable=val, justify='center')   # Creation of the entry
        text_entry.pack(side=tk.TOP, pady=2)                                # Object position


    def __create_int_entry(self, frame: ttk.Frame, val: tk.StringVar):
        """ `-`
        `Type:` Procedure
        `Description:` creates a text entry that takes only integers for the user
        :param:`frame:` frame of the interface where the entry is displayed
        :param:`val:` input value
        """

        int_entry = ttk.Entry(frame, textvariable=val, justify='center') # Creation of the entry
        int_entry.config(validate='key', validatecommand=(int_entry.register(validate_int), '%P'))
        int_entry.pack(side=tk.TOP, pady=2)  # Object position


    def __create_combobox(self, frame: ttk.Frame, val: list[str]):
        """ `-`
        `Type:` Procedure
        `Definition:` creates a combobox for the user
        :param:`frame:` frame of the interface where the combobox is displayed
        :param:`val:` combobox values
        """

        combobox = ttk.Combobox(frame, values=val, justify='center', state="readonly")  # Creation of the combobox
        combobox.pack(side=tk.TOP, pady=2)                                              # Object position

        self.user_entries.append(combobox) # Add a combobox instead of a StringVar in the list to retrieve more easily this value later


    def __create_limited_entry(self, frame: ttk.Frame, val: tk.StringVar):
        """ `-`
        `Type:` Procedure
        `Description:` creates a limited text entry
        :param:`frame:` frame of the interface where the entry is displayed
        :param:`val:` input value
        """

        val.trace('w', lambda *args, var=val: self.__validate_input(var))   # limitation of the number of characters

        entry = ttk.Entry(frame, textvariable=val, justify='center')        # Creation of the entry
        entry.pack(side=tk.TOP, pady=2)                                     # Object position


    def __validate_input(self, var: tk.StringVar):
        """ `-`
        `Type:` Procedure
        `Description:` checks that a certain number of characters cannot be exceeded
        :param:`var:` stringvar associated with the entry
        """

        max_char = 11
        current_text = var.get()
        if len(current_text) > max_char:
            var.set(current_text[:max_char])


    def __close_pop_up(self):
        """ `-`
        `Type:` Porcedure
        `Description:` close the interface and check that all input fields are not empty
        """

        new_user_entries = []
        was_break = False

        # retrieves the values of the StringVar
        for i in range(0, self.nb_entries):
            value = self.user_entries[i].get()
            if value == "":
                was_break = True
                break

            new_user_entries.append(value)
        
        self.user_entries = new_user_entries

        self.destroy() # Closing the interface

        # information to the user that he has not filled in all the boxes
        if was_break:
            MessageBox("ERREUR Manque d'information", "[ERREUR] Vous n'avez pas remplis toutes les cases.").mainloop()
            self.user_entries = []

    
    def get_user_entries(self) -> list[str]:
        """ `+`
        `Type:` Function
        `Description:` getter that returns the variable user_entries
        `Return:` user entries in string
        """

        return self.user_entries