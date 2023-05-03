# Author        : Victor BROSSARD
# Description   : GUI pop-up to request something to the user

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
import tkinter as tk
import tkinter.messagebox
import ctypes

from tkinter import ttk

from UsefulFunction.UsefulFunction import cant_close
from UsefulFunction.UsefulFunction import validate_int

#-----------------------------------------------------------------------------------------------------

class UserEntryPopUp(tk.Tk):
    """ `+`
    :class:`UserEntryPopUp` handles user interaction through a pop-up
    """

    def __init__(self, name: str, label_list: list, int_entry_list: list):
        """ `-`
        `Type:` Constructor
        :param:`name:` pop-up name
        :param:`label_list:` explanations of what is required of the user
        :param:`int_entry_list:` integer list that has a 1 at location i where i is the index of the input that will hold only integers  
        """

        # Check precondition
        if len(label_list) != len(int_entry_list) or not all(isinstance(x, int) for x in int_entry_list):
            tkinter.messagebox.showinfo('Handling ERROR', 'Erreur de manipulation des UserEntryPopUp.')
            return

        # Parent constructor
        super().__init__()
            
        # Interface initialization
        self.title(name)
        self.protocol("WM_DELETE_WINDOW", cant_close)   # Prevents the window from being closed by the red cross
        self.wm_attributes("-topmost", True)            # Prioritize the window

        # Variables that stores the value given by the user
        self.user_entries = []
        self.nb_entries = len(label_list)

        # Configuring the placement of interface objects
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        # Adds interface objects to the interface
        self.__implementation(label_list, int_entry_list)


    def __implementation(self, label_list: list, int_entry_list: list):
        """ `-`
        `Type:` Procedure
        `Description:` adds interface objects to the interface
        :param:`label_list:` explanations of what is required of the user
        :param:`int_entry_list:` integer list that has a 1 at location i where i is the index of the input that will hold only integers 
        """

        # Canvas
        canvas = tk.Canvas(self)

        # Frame
        entry_frame = ttk.Frame(canvas)

        # Label and Entry
        for i in range(0, self.nb_entries):
            # Label
            text_label = ttk.Label(entry_frame, text=label_list[i])   # Creation of the label
            text_label.pack(side=tk.TOP, pady=2)                # Object position

            # Variable that stores the value given by the user
            self.user_entries.append(tk.StringVar())

            # Entry
            if int_entry_list == []: 
                self.__create_text_entry(entry_frame, self.user_entries[i])
            elif int_entry_list[i] == 1:
                self.__create_int_entry(entry_frame, self.user_entries[i])
            else:
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


    def __create_text_entry(self, frame: ttk.Frame, var: tk.StringVar):
        """ `-`
        `Type:` Procedure
        `Description:`
        """

        text_entry = ttk.Entry(frame, textvariable=var, justify='center')   # Creation of the entry
        text_entry.pack(side=tk.TOP, pady=2)                                # Object position


    def __create_int_entry(self, frame: ttk.Frame, var: tk.StringVar):
        """ `-`
        `Type:` Procedure
        `Description:`
        """

        int_entry = ttk.Entry(frame, textvariable=var, justify='center') # Creation of the entry
        int_entry.config(validate='key', validatecommand=(int_entry.register(validate_int), '%P'))
        int_entry.pack(side=tk.TOP, pady=2)  # Object position


    def __close_pop_up(self):
        """ `-`
        `Type:` Porcedure
        `Description:` close the interface
        """

        new_user_entries = []

        # retrieves the values of the StringVar
        for i in range(0, self.nb_entries):
            new_user_entries.append(self.user_entries[i].get())

        self.user_entries = new_user_entries

        self.destroy() # Closing the interface

    
    def get_user_entries(self):
        """ `+`
        `Type:` Function
        `Description:` getter that returns the variable user_entries
        `Return:` user_entries
        """

        return self.user_entries