from tkinter import *
import BrotherDriver

class FraternityManager:
    
    def __init__(self):
        
        self.__brothers = {}

        
        self.__window = Tk()
        
        master = Frame(self.__window)
        
        Label(master, text = "Brothers").grid(row = 1, column = 1, columnspan = 3)
        
        self.__listbox = Listbox(master, selectmode = SINGLE)
        self.__listbox.grid(row = 2, column = 1, columnspan = 3)
        
        Button(master, text = "Add").grid(row = 3, column = 1)
        Button(master, text = "Edit").grid(row = 3, column = 2)
        Button(master, text = "Delete").grid(row = 3, column = 3)
        
        master.pack()
        mainloop()
        
    def add(self):
        name, brother = BrotherDriver()
    
    def edit(self):
        pass
    
    def delete(self):
        pass

FraternityManager()