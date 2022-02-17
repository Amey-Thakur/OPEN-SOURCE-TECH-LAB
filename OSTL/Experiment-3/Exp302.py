#Experiment 3, Program 3.2
#Program to implement Constructors

class Student:
    no_of_courses=5
    credits=25
    '''
    def __init__(self):
        self.rollno=0   #instance var
        self.name=''
        self.addr=''
        self.mob=0
        '''
    def __init__(self,r=0,n='',a='',m=0):
        self.rollno=r
        self.name=n
        self.addr=a
        self.mob=m
        
    def setval(self,rollno,name,addr,mob):
        self.rollno=rollno
        self.name=name
        self.addr=addr
        self.mob=mob
    def getval(self):
        #print('Self is at',id(self))
        return self.rollno, self.name, self.no_of_courses, self.credits, self.mob
    @classmethod
    def setcourses(cls,n):
        cls.no_of_courses=n
    @classmethod
    def setcredits(cls,c):
        cls.credits=c
    @staticmethod
    def is_workday(day):
        if day.weekday()==6:
            return False
        return True



#s1=Student('1','Name','NM',876875)
s1=Student(1,'Ahmed','Mum',9822)
#s1.setval('17CO01','Ansari Heena','Mumbai',9898998989)
#print('s1 is at',id(s1))
print(s1.getval())
s2=Student()
Student.setcourses(6)
Student.setcredits(30)
s2.setval('17CO02','Iqra','Mumbai',9898998989)
#print('s2 is at',id(s2))
print(s2.getval())
s3=Student()
s3.setval('17CO35','SS','M',9898)
print(s3.getval())
#type(s3)
print('s3 is at',id(s3))
s4=Student()
s4.setval('17CO35','SS','M',9898)
print(s4.getval())
print('s4 is at',id(s4))
#import datetime
#d=datetime.date(2019,1,28)
#print('Is workday ?',Student.is_workday(d))
