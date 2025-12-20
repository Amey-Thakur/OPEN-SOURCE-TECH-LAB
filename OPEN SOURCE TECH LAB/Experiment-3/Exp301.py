'''
EXPERIMENT No. : 3
Name : AMEY THAKUR

Aim : Program to implement Classes in Python.
'''

import datetime

class Student:
    '''
    A STUDENT CLASS TO MANAGE STUDENTS.
    '''
    no_of_courses = 5       #class variable
    credits = 25            #class variable

    def setval(self,rollno,name,addr,mob):
        '''
        METHOD TO SET THE PROPERTIES OF THE OBJECT.
        '''
        self.rollno = rollno   #instance variable
        self.name = name
        self.mob = mob
    
    def getval(self):
        print('SELF IS AT: ',id(self))
        return self.rollno, self.name, self. no_of_courses, self.credits, self.mob

    @classmethod
    def setcourses(cls,n):
        cls.no_of_courses = n
    
    @classmethod
    def setcredits(cls,c):
        cls.credits = c

    @staticmethod
    def is_workday(day):
        if(day.weekday()==6):
            return False
        return True
    
s1 = Student()
s1.setval('18CO63', 'TAUSEEF MUSHTAQUE ALI SHAIKH', 'MUMBAI', 9898989898)
print('S1 IS AT: ', id(s1))
print(s1.getval())
print()

s2 = Student()
s2.no_of_courses = 6
print('S2 IS AT: ',id(s2))
s2.setval('18CO55', 'RAUF YOOSAF SHAIKH', 'MUMBAI', 9191919191)
print(s2.getval())
print()

print(s1.getval())
print()
print('S1 = ', s1.__dict__)
print()
print('S2 = ', s2.__dict__)
print()

Student.setcredits(30)
print(s1.getval())
print()

date = int(input('ENTER DATE (DD): '))
month = int(input('ENTER MONTH (MM): '))
year = int(input('ENTER YEAR (YYYY): '))
d = datetime.date(year,month,date)
print('IS WORKING?', Student.is_workday(d))
