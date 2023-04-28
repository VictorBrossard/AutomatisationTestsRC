# Author        : Victor BROSSARD
# Description   : Graphical interface that allows you to manage the number of loops made on the same test

#-----------------------------------------------------------------------------------------------------
# Import of files useful for code execution 
import tkinter as tk
import ctypes
import os

from tkinter import ttk

from UsefulFunction.UsefulFunction import cant_close
from UsefulFunction.UsefulFunction import str_list_to_int_list

#-----------------------------------------------------------------------------------------------------

class LoopTestInterface(tk.Tk):
    """ `+`
    :class:`LoopTestInterface` allows you to manage the number of loops made on the same test
    """

    def __init__(self, name: str, test_list: list):
        """ `-`
        `Type:` Constructor
        :param:`name:` window name
        :param:`test_list:` list that contains the tests to be performed
        """

        # Parent constructor
        super().__init__()

        # list to handle
        self.old_test_list = test_list 
        self.new_test_list = []

        # Window size and position
        height = 500
        width = 400
        user32 = ctypes.windll.user32                               # User information
        x = int((user32.GetSystemMetrics(0) / 2) - (height / 2))    # int() = any type to int
        y = int((user32.GetSystemMetrics(1) / 2) - (width / 2))     # user32.GetSystemMetrics() = screen size (0 = height and 1 = width)

        # Interface initialization
        self.title(name)
        self.geometry(str(height) + "x" + str(width) + "+" + str(x) + "+" + str(y))     # Set window size and position | str() = type to string
        self.resizable(width=0, height=0)                                               # Prevents any modification of window size
        self.protocol("WM_DELETE_WINDOW", cant_close)                                   # Prevents the window from being closed by the red cross

        self.__implementation(self.old_test_list)

    
    def __implementation(self, test_list: list):
        """ `-`
        `Type:` Procedure
        `Description:` adds interface objects to the interface
        :param:`test_list:` list that contains the tests to be performed
        """  

        # Start Button
        start_button = ttk.Button(self, text="Start", command=lambda: self.__create_new_test_list(test_frame))    
        start_button.pack(side=tk.TOP, padx=10)

        start_button = ttk.Button(self, text="Exit", command=self.__close_interface)    
        start_button.pack(side=tk.TOP, padx=10)

        # Canvas
        canvas = tk.Canvas(self)
        canvas.pack(side=tk.LEFT, fill=tk.Y)

        # Frame
        test_frame = ttk.Frame(self)
        canvas.create_window(0, 0, window=test_frame, anchor='nw')

        # Label and Entry
        for i, test in enumerate(test_list):
            # We separate the name of the file and its path to be able to handle it better later
            test_name = os.path.basename(test)

            # for each test in the list we display them on our interface
            test_name_label = ttk.Label(test_frame, text=test_name)
            test_name_label.grid(column=0, row=i, pady=10)

            var_entry = tk.StringVar(value="1")

            test_entry = ttk.Entry(test_frame, textvariable=var_entry)
            test_entry.config(validate='key', validatecommand=(test_entry.register(self.__validate_int), '%P'))
            test_entry.grid(column=1, row=i, pady=10)

        # Scrollbar
        scrollbar_y = tk.Scrollbar(self, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.config(yscrollcommand=scrollbar_y.set)

        # Configurer le canvas pour agir sur la barre de défilement
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
        canvas.bind('<MouseWheel>', lambda e: canvas.yview_scroll(int(-1*(e.delta/120)), "units"))
        

    def __create_new_test_list(self, frame):
        """ `-`
        `Type:` Procedure
        `Description:` creates the new test list then destroys the interface
        :param:`frame:` interface panel where all entries are placed
        """

        # recovery of all values in the entries
        entry_values = []
        for child in frame.winfo_children():
            if isinstance(child, tk.Entry):
                entry_values.append(child.get())
        
        # transformation into integer list
        entry_values = str_list_to_int_list(entry_values)

        # new test list that has n times the test in the list, where n is the number entered as parameter by the user
        for i, n in enumerate(entry_values):
            if n > 0:
                for j in range(0, n):
                    self.new_test_list.append(self.old_test_list[i])

        self.destroy()


    def __close_interface(self):
        """ `-`
        `Type:` Procedure
        `Description:` close only the interface
        """

        self.destroy()


    def get_new_test_list(self):
        """ `+`
        `Type:` Function
        `Description:` getter that returns the variable new_test_list
        `Return:` new_test_list
        """

        return self.new_test_list
    

    def __validate_int(self, value: str) -> bool:
        """ `-`
        `Type:` Function
        `Description:` checks if the input value is an int
        :param:`value:` string to check
        `Return:` bool
        """

        if value == "":
            return True
        try:
            int(value)
            return True
        except ValueError:
            return False