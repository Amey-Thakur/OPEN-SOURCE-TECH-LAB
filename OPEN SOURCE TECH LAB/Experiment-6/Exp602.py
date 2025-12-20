from tkinter import *
import mysql.connector
class App:
    def __init__(self):
        self.root=Tk()
        self.root.title('GUI App')
        self.root.geometry('500x350')
        self.root.configure(background='light blue')
        self.rollno = Label(self.root, text="Roll No.", bg="light blue")
        self.name = Label(self.root, text="Name", bg="light blue")
        self.address = Label(self.root, text="Address", bg="light blue")
        self.mob = Label(self.root, text="Mobile", bg="light blue")
        self.no_of_courses = Label(self.root, text="No. of Courses", bg="light blue")
        self.no_of_credits = Label(self.root, text="Credits", bg="light blue")
        self.courses = Label(self.root, text="Courses", bg="light blue")
        self.skills = Label(self.root, text="Skills", bg="light blue")
        self.rollno.grid(row=0,column=0)
        self.name.grid(row=1,column=0)
        self.address.grid(row=2,column=0)
        self.mob.grid(row=3,column=0)
        self.no_of_courses.grid(row=4,column=0)
        self.no_of_credits.grid(row=5,column=0)
        self.courses.grid(row=6,column=0)
        self.skills.grid(row=7,column=0)
        self.rollnof = Entry(self.root)
        self.namef = Entry(self.root)
        self.addressf = Entry(self.root)
        self.mobf = Entry(self.root)
        self.no_of_coursesf = Entry(self.root)
        self.no_of_creditsf = Entry(self.root)
        self.coursesf = Entry(self.root)
        self.skillsf = Entry(self.root)
        self.rollnof.grid(row=0,column=1,ipadx='100')
        self.namef.grid(row=1,column=1,ipadx='100')
        self.addressf.grid(row=2,column=1,ipadx='100')
        self.mobf.grid(row=3,column=1,ipadx='100')
        self.no_of_coursesf.grid(row=4,column=1,ipadx='100')
        self.no_of_creditsf.grid(row=5,column=1,ipadx='100')
        self.coursesf.grid(row=6,column=1,ipadx='100')
        self.skillsf.grid(row=7,column=1,ipadx='100')

        self.submit = Button(self.root, text="Submit", fg="Black", bg="light green", command=self.insert) 
        self.submit.grid(row=8, column=1,sticky=W+E)
        self.clear = Button(self.root, text="Clear",fg="Black", bg="light green", command=self.clearAll) 
        self.clear.grid(row=8, column=0,sticky=W+E)  
        self.root.mainloop()
    def clearAll(self):
        self.rollnof.delete(0,'end')
        self.namef.delete(0,'end')
        self.addressf.delete(0,'end')
    def insert(self):
        #print(self.rollnof.get())
        mydb = mysql.connector.connect(host='localhost',user='ostl',passwd='ostluser')
        mycursor=mydb.cursor()
        #print(rollnof.get())
        mycursor.execute('use ostldb')
        query="insert into Student values("+self.rollnof.get()+",'"+self.namef.get()+"','"+self.mobf.get()+"','"+self.addressf.get()+"','"+self.coursesf.get()+"',"+self.no_of_creditsf.get()+",'"+self.skillsf.get()+"',"+self.no_of_coursesf.get()+")"
        print(query)
        try:
            mycursor.execute(query)
            mycursor.execute('commit')
            #self.popup('Data Inserted successfully..')
            print('Data Inserted successfully..')
        except Exception:
            print('Data Insertion failed..')
            #self.popup('Data Insertion failed..')
        
            
def main():
    app=App()

if __name__=='__main__':
    main()
