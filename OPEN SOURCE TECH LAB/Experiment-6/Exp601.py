from tkinter import *
from Exp301Copy import *
import mysql.connector
def insert(r,n,a,m,cr,co,sk,c):
    mydb = mysql.connector.connect(host='localhost',user='ostl',passwd='ostluser')
    mycursor=mydb.cursor()
    #print(rollnof.get())
    mycursor.execute('use ostldb')
    query="insert into Student values("+str(r)+",'"+n+"','"+m+"','"+a+"','"+c+"',"+str(cr)+",'"+sk+"',"+str(co)+")"
    print(query)
    try:
        mycursor.execute(query)
        mycursor.execute('commit')
        return True
    except Exception:
        return False
def main():
    root=Tk()
    root.title('GUI App')
    root.geometry('500x350')
    root.configure(background='light blue')
    rollno = Label(root, text="Roll No.", bg="light blue")
    name = Label(root, text="Name", bg="light blue")
    address = Label(root, text="Address", bg="light blue")
    mob = Label(root, text="Mobile", bg="light blue")
    no_of_courses = Label(root, text="No. of Courses", bg="light blue")
    no_of_credits = Label(root, text="Credits", bg="light blue")
    courses = Label(root, text="Courses", bg="light blue")
    skills = Label(root, text="Skills", bg="light blue")
    rollno.grid(row=0,column=0)
    name.grid(row=1,column=0)
    address.grid(row=2,column=0)
    mob.grid(row=3,column=0)
    no_of_courses.grid(row=4,column=0)
    no_of_credits.grid(row=5,column=0)
    courses.grid(row=6,column=0)
    skills.grid(row=7,column=0)
    rollnof = Entry(root)
    namef = Entry(root)
    addressf = Entry(root)
    mobf = Entry(root)
    no_of_coursesf = Entry(root)
    no_of_creditsf = Entry(root)
    coursesf = Entry(root)
    skillsf = Entry(root)
    rollnof.grid(row=0,column=1,ipadx='100')
    namef.grid(row=1,column=1,ipadx='100')
    addressf.grid(row=2,column=1,ipadx='100')
    mobf.grid(row=3,column=1,ipadx='100')
    no_of_coursesf.grid(row=4,column=1,ipadx='100')
    no_of_creditsf.grid(row=5,column=1,ipadx='100')
    coursesf.grid(row=6,column=1,ipadx='100')
    skillsf.grid(row=7,column=1,ipadx='100')
    
    submit = Button(root, text="Submit", fg="Black", bg="light green", command=insert(rollnof.get(),namef.get(),addressf.get(),mobf.get(),no_of_creditsf.get(),no_of_coursesf.get(),skillsf.get(),coursesf.get())) 
    submit.grid(row=8, column=1) 

    root.mainloop()
    s=Student()



if __name__=='__main__':
    main()