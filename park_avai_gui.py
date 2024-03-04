'''
    Kay (Mengxian) Cai
    CS5001, Fall 2022
    Data Dashboard Final Project - Milestone 2
    park_avai_gui.py -- store the class of GUI for the park availability analysis
'''
from tkinter import *
from tkinter import ttk
from functions_file import make_neighbourhoods_data_frame_and_graph, make_bar_graph_from_dict 

class ParkAvaiGui:
    '''
    class: ParkAvaiGui
        This is the GUI (graphical user interface) for park availability analysis. 
    Attributes: name, master, title, name_list, objects_list, label, choice_combo, confirm_btn,
    bg, frame1, frame2, bg_label, nbh_label, sorting_label, draw_label, nbh_combo, sort_combo, draw_btn
    Methods: show_page1, show_page2, __str__, __eq__
    '''
    def __init__(self, master_window, title, name_list, nbh_objects_list):
        '''
        Constructor -- to create new instances of park availability analysis GUI.
        Parameters:
            self -- the current GUI instance
            master_window -- a Tk root window, which is the master of the current GUI instance
            title -- a string, which is the title of image to be placed in the bg_label
            name_list -- a list of strings, which are names of all Neighbourhoods and which will
            become string value of the nbh_combo drop-down
            nbh_objects_list - a list of Neighbourhood objects
        Raise:
            None
        '''
        self.name = "Park Availability Analysis GUI"
        self.master = master_window
        self.title = title
        self.name_list = name_list
        self.objects_list = nbh_objects_list
        self.show_page1()
        

    def show_page1(self):
        '''
        Method -- to show the first page of this GUI instance, where user choose how to draw the visulization
        of all neighbourhoods.
        Parameters:
            self -- the current GUI instance
        Return:
            None
        Raise:
            None
        '''
        self.label = ttk.Label(self.master, text = f'''Please choose how you would like the analysis to\
 be shown.\n\n Alphabetical: \n\tNeighbourhoods will be shown in alphabetical order according to the first letter of their names.\n \
Ascending-Parks Num: \n\tNeighbourhoods will be ranked ascendingly in terms of total number of parks.\n \
Descending-Parks Num: \n\tNeighbourhoods will be ranked descendingly in terms of total number of parks.\n \
Ascending-PerPerson Area: \n\tNeighbourhoods will be ranked ascendingly in terms of parks area per person.\n \
Descending-PerPerson Area: \n\tNeighbourhoods will be ranked descendingly in terms of parks area per person.\n''', wraplength = 600, justify = LEFT)
        self.label.grid(row = 0, column = 0, sticky = 'nsew', padx = 10, pady = 10)
        order_list = StringVar()
        keepvalue = order_list.get()
        self.choice_combo = ttk.Combobox(self.master, textvariable = keepvalue, values = (["Alphabetical","Ascending-Parks Num", \
                                                                                              "Descending-Parks Num", "Ascending-PerPerson Area",\
                                                                                             "Descending-PerPerson Area"]), state="readonly")
        self.choice_combo.set("Alphabetical")
        self.choice_combo.grid(row = 1, column = 0)
        self.confirm_btn = ttk.Button(self.master, text = "Confirm", command = self.show_page2)
        self.confirm_btn.bind("<Button>", lambda e: make_neighbourhoods_data_frame_and_graph(self.objects_list, self.choice_combo.current(), self.title), add="+")
        self.confirm_btn.grid(row = 2, column = 0, padx = 10, pady = 10)


    def show_page2(self):
        '''
        Method -- to show the second page of this GUI instance, where user choose which neighbourhood to see
        breakdown and the sorting order.
        Parameters:
            self -- the current GUI instance
        Return:
            None
        Raise:
            None
        '''
        for i in self.master.winfo_children():
            i.destroy()
        self.bg = PhotoImage(file = self.title+".png", master = self.master)
        self.frame1 = Frame(self.master, width = 800, height = 600)
        self.frame1.pack()
        self.frame2 = Frame(self.master)
        self.frame2.pack()
        self.bg_label = ttk.Label(self.frame1, image = self.bg)
        self.bg_label.pack()
        self.nbh_label = ttk.Label(self.frame2, text = "Please select a Neighbourhood from the menu to see the \
breakdown of all parks in the chosen Neighbourhood.", wraplength = 240, justify = CENTER)
        self.nbh_label.grid(row = 0, column = 0, sticky = 'nsew', padx = 10, pady = 5)
        self.sorting_label = ttk.Label(self.frame2, text = "Please select the sorting order of parks (\"Ascending\" and\
 \"Descending\" in terms of the area of each park).", wraplength = 240, justify = CENTER)
        self.sorting_label.grid(row = 0, column = 1, sticky = 'nsew', padx = 10, pady = 5)
        self.draw_label = ttk.Label(self.frame2, text = "Confirm and draw a graph for your selected Neighbourhood and \
sorting order by pressing the button below. To re-choose, just select and press the button again.", wraplength = 300, \
                                    justify = CENTER)
        self.draw_label.grid(row = 0, column = 2, sticky = 'nsew', padx = 10, pady = 5)
        nbh_list = StringVar()
        self.nbh_combo = ttk.Combobox(self.frame2, textvariable = nbh_list, values = self.name_list, state="readonly")
        self.nbh_combo.grid(row = 1, column = 0, padx = 10, pady = 5)
        sorting_list = StringVar()
        self.sort_combo = ttk.Combobox(self.frame2, textvariable = sorting_list, values =(["Alphabetical","Ascending", "Descending"]),\
                                       state ="readonly")
        self.sort_combo.grid(row = 1, column = 1, padx = 10, pady = 5)
        self.draw_btn = ttk.Button(self.frame2, text = "Confirm & Draw", command = lambda: make_bar_graph_from_dict(self.objects_list, self.nbh_combo.current(), self.sort_combo.current()))
        self.draw_btn.grid(row = 1, column = 2, padx = 10, pady = 5)

        
    def __str__(self):
        '''
        Method -- to return a string that represents this GUI instance.
        Parameters:
            self -- the current GUI instance
        Return:
            a string that represents this GUI instance
        Raise:
            None
        '''
        printable = f"{self.name}"
        return printable


    def __eq__(self, other):
        '''
        Method -- to compares the current GUI instance to another one.
        Parameters:
            self -- the current GUI instance
            other -- the other GUI instance
        Return:
            Boolean True if the names are equal, otherwise, return Boolen False if
            name are inequal
        Raise:
            TypeError if the other is not a park availability analysis GUI instance
        '''
        if not isinstance(other, ParkAvaiGui):
            raise TypeError("You can only compare two same instances.")
        else:
            return self.name == other.name
