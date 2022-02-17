#Experiment 4, Program 4.1
#Program to implement Inheritance

class Student:
    no_of_courses=5
    credits=25
    def __init__(self,*args):
        if args.__len__()==0:
            self.rollno=self.name=self.addr=None
            self.mob=None
        elif isinstance(args[0],Student):
            self.rollno=args[0].rollno
            self.name=args[0].name
            self.addr=args[0].addr
            self.mob=args[0].mob
        else:
            self.setval(args[0],args[1],args[2],args[3])
    def setval(self,rollno,name,addr,mob):
        self.rollno=rollno
        self.name=name
        self.addr=addr
        self.mob=mob
    def getval(self):
        print('RollNo:',self.rollno,'\nName:',self.name,'\nNo. of Courses:',self.no_of_courses)
        print('Credits:',self.credits,'\nMobile:',self.mob)    
       

class SECO(Student):
    courses=list()
    skills=list()
    def __init__(self):
        #Student.__init__(self)
        try:
            Student.__init__(self)
            #name=myname
        except NameError:
            print('This is Name Error')
        except Exception as e:
            print('Error:',e)
        else:
            pass
        finally:
            pass
    def setprop(self,c,s):
        self.courses.append(c)
        self.skills.append(s)
    def getprop(self):
        self.getval()
        print('Courses:',self.courses,'\nSkills:',self.skills)

s=SECO()
#print(s.getval())
#s1=SECO('18DCO01','Almas','Mumbai',9898989898)
#print(s1.getval())
s.setval('18CO01','Ahmed','Mumbai',9898)
s.setprop('OSTL','Python')
s.setprop('AOA','Design Algos')
s.setprop('CG','C Programming')
s.getprop()


