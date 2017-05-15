from tkinter import *
import re

class Semester(Frame):
    
    def __init__(self, window, label, var = None):
        super().__init__(window)
        
        self.__term = StringVar()
        self.__year = StringVar()
        self.__year.set("YYYY")
        
        if var == None:
            self.__var = StringVar()
        elif isinstance(var, StringVar):
            self.__var = var
        else:
            raise TypeError("var must be a StringVar")
        self.__term.trace("w", self.__update)
        self.__year.trace("w", self.__update)
        
        Label(self, text = label).grid(row = 1, column = 1)
        OptionMenu(self, self.__term, "Fall", "Spring").grid(row = 1, column = 2)
        Entry(self, textvariable = self.__year, width = 5).grid(row = 1, column = 3)
        
    def get(self):
        return self.__var.get()
    
    def __update(self, *args):
        self.__var.set(self.__term.get() + " " + self.__year.get())

class SemesterGPA(Frame):
    
    def __init__(self, master, term = None, year = None):
        super().__init__(master)
        
        self.term = StringVar()
        self.term.set(term)
        
        self.year = StringVar()
        self.year.set(year)
        
        self.__entry = StringVar()
        self.__entry.set("0.00")
        
        Label(self, textvariable = self.term).grid(row = 1, column = 1)
        Label(self, textvariable = self.year).grid(row = 1, column = 2)
        
        Entry(self, textvariable = self.__entry, width = 4).grid(row = 1, column = 3)
    
    def get(self):
        return self._entry.get()

class SemesterMatrix(Frame):
    
    def __init__(self, master, startterm, startyear):
        super().__init__(master)
        self.__frame = Frame(self)
        self.__frame.grid(row = 1, column = 1, columnspan = 2)
        
        self.__semesters = [SemesterGPA(self.__frame) for i in range(8)]

        Label(self, text = "Extra semesters:").grid(row = 2, column = 1)
        self.__extrasemester = StringVar()
        menu = OptionMenu(self, self.__extrasemester, "0", "1","2","3","4","5","6")
        menu.grid(row = 2, column = 2)
        self.__extrasemester.trace("w",self.__changeSemesters)
        
        for i in range(1, 5):
            for j in range(1,3):
                widget = self.__semesters[(i-1)*2 + j-1]
                widget.grid(row = i, column = j)
                
        self.update(startterm, startyear)
    
    def __changeSemesters(self, *args):
        try:
            1-int(self.__extrasemester.get())
        except:
            return
        difference = len(self.__semesters) - 8 - int(self.__extrasemester.get())
        if difference == 0:
            return
        elif difference > 0:
            while difference > 0:
                self.__semesters[-1].destroy()
                self.__semesters.pop()
                difference -= 1
        else:
            while difference < 0:
                temp = SemesterGPA(self.__frame)
                self.__semesters.append(temp)
                temp.grid(row = (len(self.__semesters)-1) // 2 + 1, column = (len(self.__semesters)-1) % 2 + 1)
                difference += 1
            self.update(self.__semesters[0].term.get(), self.__semesters[0].year.get())
    
    def update(self, startterm, startyear):
        year = int(startyear)
        terms = [startterm, "Spring"]
        if startterm == "Spring":
            terms[1] = "Fall"
            year -= 1

        for i in range(1, 1 + len(self.__semesters)//2 if len(self.__semesters)%2 == 0 else 2 + len(self.__semesters)//2):
            for j in range(1, 3):
                try:
                    widget = self.__semesters[(i-1)*2 + j-1]
            
                    widget.term.set(terms[j -1])
                    
                    if terms[j-1] == "Spring":
                        year += 1
                    widget.year.set(year)
                except:
                    pass
    def get(self):
        lst = []
        

class BrotherDriver:
    
    def __init__(self, brother = None):
        window = Tk()
        
        master = Frame(window)
        
        Label(master, text = "Name:").grid(row = 1, column = 1)
        self.__name = StringVar()
        Entry(master, textvariable = self.__name).grid(row = 1, column = 2)
        
        Label(master, text = "Major:").grid(row = 1, column = 3)
        self.__major = StringVar()
        OptionMenu(master, self.__major, "Accounting", "Animal Behavior", "Biochemistry", "Biology", "Business Economics", "Chemistry", "Communication and Media", "Computer Science", "Construction Managment", "Criminal Justice", "Cybersecurity", "Economics", "English", "Foreign Language", "Fraud and Financial Crime Investigation", "Geoscience", "Government and Politics", "Health Studies", "Health Studies - Management", "Mathematics", "Neuroscience", "Nursing", "Occupational Therapy", "Philosophy", "Physical Therapy", "Physics", "Psychobiology", "Psychology", "Psychology - Child Life", "Public Relations", "Risk Management and Insurance", "Sociology and Anthropology", "Sports Management", "Therapeutic Recreation", "Wellness and Adventure Education").grid(row = 1, column = 4)
        
        self.__matriculated = StringVar()
        self.__matriculated.trace("w", self.__updateMatrix)
        self.__startingsemester = Semester(master, "Semester Matriculated:", var = self.__matriculated)
        self.__startingsemester.grid(row = 2, column = 1, columnspan = 4, sticky = W)
        
        self.__joiningsemester = Semester(master, "Semester Recruited:")
        self.__joiningsemester.grid(row = 3, column = 1, columnspan = 4, sticky = W)
        
        self.__gpas = SemesterMatrix(master, "Fall", "2016")
        self.__gpas.grid(row = 4, column = 1, columnspan = 4)

        Label(master, text = "Did he graduate?").grid(row = 5, column = 1)
        self.__graduated = StringVar()
        OptionMenu(master, self.__graduated, "Yes", "No", "N/A").grid(row = 5, column = 2)

        Button(master, text = "Save", command = self.__save).grid(row = 6, column = 4)
        
        master.grid()
        mainloop()

    def __updateMatrix(self, *args):
        start = self.__startingsemester.get()
        term = start.split(" ")
        if not term[0] in ["Fall","Spring"] or re.match(r'\d{4}', term[1]) == None:
            pass
        else:
            self.__gpas.update(term[0], term[1])
        
    def __save(self):
        gpas = self.__gpas.get()
        matriculated = self.__matriculated.get()
        pledged = self.__joining_semester.get()
        major = self.__major.get()
        graduated =  self.__graduated.get()
        if graduated == "N/A":
            graduated = None

BrotherDriver()