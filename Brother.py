import re

class Brother:
    
    def __init__(self, gpas = None, pledged_semester = None, matriculated_semester = None, graduated = None, major = None):
        self.__gpas = None
        self.__pladged_semester = None
        self.__matriculated_semester = None
        self.__graduated = None
        self.__major = None
        self.setGPAs(gpas)
        self.setPledgedSemester(pledged_semester)
        self.setMatriculatedSemester(matriculated_semester)
        self.setGraduated(graduated)
        self.setMajor(major)
    
    def setGPAs(self, gpas):
        if not isinstance(gpas, list) and gpas != None:
            raise TypeError("GPAs need to be in a list or None")
        if gpas == None:
            self.__gpas = []
        else:
            self.__gpas = self.__convertGPAs(gpas)
    
    def getGPAs(self):
        return self.__gpas
    
    def __getIndex(self, term, year):
        return (1 if term == self.__matriculated_semester[0] else 0) + (year - self.__matriculated_semester[1]) * 2
    
    def attending(self, term, year):
        index = self.__getIndex(term, year)
        return index > 0 and index <= len(self.__gpas)
    
    def getGPA(self, term, year):
        if not self.attending(term, year):
            return None
        return self.__gpas[self.__getIndex(term,year)]
    
    def addGPA(self, gpa):
        gpa = self.__convertedGPAs([gpa])
        self.__gpas = self.__gpas + gpa
    
    def __isNumber(self, num):
        try:
            float(num)
            return True
        except ValueError:
            return False

    def __convertGPAs(self, gpas):
        lst = []
        for gpa in gpas:
            if not self.__isNumber(gpa) and gpa != None:
                raise TypeError("GPA must be a number between 0 and 4 or None")
            if gpa == "None":
                lst.append(None)
            elif re.match(r'[0-3]\.\d\d|4.00', gpa) != None:
                lst.append(float(gpa))
            else:
                raise ValueError("GPA must be between 0 and 4")
        return lst
    
    def __validSemester(self, semester):
        result = re.match(r'[fF][aA][lL]{2} \d{4}|[sS][pP][rR][iI][nN][gG] \d{4}', semester)
        return False if result == None else True

    def setPledgedSemester(self, pledged_semester):
        if not self.__validSemester(pledged_semester) and pledged_semester != None:
            if not isinstance(pledged_semester, str):
                raise TypeError("Semester must be a string in Fall/Spring YYYY format or None")
            raise ValueError("Semester doesn't match Fall/Spring YYYY format")
        if pledged_semester == None:
            self.__pledged_semester = None
        else:
            self.__pledged_semester = [pledged_semester[0:4].lower(), int(pledged_semester[4:])]
    
    
    def setMatriculatedSemester(self, matriculated_semester):
        if not self.__validSemester(matriculated_semester) and matriculated_semester != None:
            if not isinstance(matriculated_semester, str):
                raise TypeError("Semester must be a string in Fall/Spring YYYY format or None")
            raise ValueError("Semester doesn't match Fall/Spring YYYY format")
        if matriculated_semester == None:
            self.__matriculated_semester = None
        else:
            self.__matriculated_semester = [matriculated_semester[0:4].lower(), int(matriculated_semester[4:])]
    
    def setGraduated(self, graduated):
        if not isinstance(graduated, bool) and graduated != None:
            raise TypeError("Graduated must be a boolean value or None")
        self.__graduated = graduated
    
    def setMajor(self, major):
        if not isinstance(major, str):
            raise TypeError("Major must be a string")
        if major.lower() in ['accounting', 'animal behavior', 'biochemistry', 'biology', 'business economics', 'chemistry', 'communication and media', 'computer science', 'construction managment', 'criminal justice', 'cybersecurity', 'economics', 'english', 'foreign language', 'fraud and financial crime investigation', 'geoscience', 'government and politics', 'health studies', 'health studies - management', 'mathematics', 'neuroscience', 'nursing', 'occupational therapy', 'philosophy', 'physical therapy', 'physics', 'psychobiology', 'psychology', 'psychology - child life', 'public relations', 'risk management and insurance', 'sociology and anthropology', 'sports management', 'therapeutic recreation', 'wellness and adventure education']:
            self.__major = major
        else:
            raise ValueError("Invalid Major")
    
Brother()