# Author        : Victor BROSSARD
# Description   : GUI pop-up to request something to the user

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
import tkinter as tk
import ctypes

from tkinter import ttk

from UsefulFunction.UsefulFunction import cant_close

#-----------------------------------------------------------------------------------------------------

class UserEntryPopUp(tk.Tk):
    """ `+`
    :class:`UserEntryPopUp` handles user interaction through a pop-up
    """

    def __init__(self, name: str, desc: list):
        """ `-`
        `Type:` Constructor
        :param:`name:` pop-up name
        :param:`desc:` explanation of what is required of the user
        """

        # Parent constructor
        super().__init__()

        # Interface initialization
        self.title(name)
        self.protocol("WM_DELETE_WINDOW", cant_close)   # Prevents the window from being closed by the red cross
        self.wm_attributes("-topmost", True)            # Prioritize the window

        # Variables that stores the value given by the user
        self.user_entries = []
        self.nb_entries = len(desc)

        # Configuring the placement of interface objects
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        # Adds interface objects to the interface
        self.__implementation(desc)


    def __implementation(self, desc: list):
        """ `-`
        `Type:` Procedure
        `Description:` adds interface objects to the interface
        :param:`desc:` explanation of what is required of the user
        """

        # Canvas
        canvas = tk.Canvas(self)

        # Frame
        entry_frame = ttk.Frame(canvas)

        # Label and Entry
        for i in range(0, self.nb_entries):
            # Label
            text_label = ttk.Label(entry_frame, text=desc[i])   # Creation of the label
            text_label.pack(side=tk.TOP, pady=2)                # Object position

            # Variable that stores the value given by the user
            self.user_entries.append(tk.StringVar())

            # Entry 
            text_entry = ttk.Entry(entry_frame, textvariable=self.user_entries[i])  # Creation of the entry
            text_entry.pack(side=tk.TOP, pady=2)                                    # Object position

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