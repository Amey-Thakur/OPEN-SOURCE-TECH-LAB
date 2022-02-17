from tkinter import *
from tkinter import ttk
import mysql.connector
class App:
    def __init__(self):
        self.root=Tk()
        self.root.title('GUI App')
        #self.root.geometry('500x350')
        #self.root.configure(background='light blue')
        self.menu=Menu(self.root) 
        self.root.config(menu=self.menu)
        self.crud_menu=Menu(self.menu)
        self.menu.add_cascade(label='CRUD',menu=self.crud_menu)
        self.crud_menu.add_command(label='Create',command=self.create)
        self.crud_menu.add_separator()
        self.crud_menu.add_command(label='Read',command=self.read)
        self.crud_menu.add_separator()
        self.crud_menu.add_command(label='Update',command=self.update)
        self.crud_menu.add_separator()
        self.crud_menu.add_command(label='Delete',command=self.delete)
        self.crud_menu.add_separator()
        self.crud_menu.add_command(label='Exit',command=self.root.quit)
        self.cn=Canvas(self.root,height=700,width=700,bg='#263D42')
        self.cn.grid()
        self.frame=Frame(self.root,bg='white')#light blue')
        self.frame.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)
        self.rollno = ttk.Label(self.frame, text="Roll No.")#, bg="light blue")
        self.name = Label(self.frame, text="Name", bg="light blue")
        self.address = Label(self.frame, text="Address", bg="light blue")
        self.mob = Label(self.frame, text="Mobile", bg="light blue")
        self.no_of_courses = Label(self.frame, text="No. of Courses", bg="light blue")
        self.no_of_credits = Label(self.frame, text="Credits", bg="light blue")
        self.courses = Label(self.frame, text="Courses", bg="light blue")
        self.skills = Label(self.frame, text="Skills", bg="light blue")
        self.rollno.grid(row=0,column=0)
        self.name.grid(row=1,column=0)
        self.address.grid(row=2,column=0)
        self.mob.grid(row=3,column=0)
        self.no_of_courses.grid(row=4,column=0)
        self.no_of_credits.grid(row=5,column=0)
        self.courses.grid(row=6,column=0)
        self.skills.grid(row=7,column=0)
        self.rollnof = ttk.Entry(self.frame)
        self.namef = Entry(self.frame)
        self.addressf = Entry(self.frame)
        self.mobf = Entry(self.frame)
        self.no_of_coursesf = Entry(self.frame)
        self.no_of_creditsf = Entry(self.frame)
        self.coursesf = Entry(self.frame)
        self.skillsf = Entry(self.frame)
        self.rollnof.grid(row=0,column=1,ipadx='100')
        self.namef.grid(row=1,column=1,ipadx='100')
        self.addressf.grid(row=2,column=1,ipadx='100')
        self.mobf.grid(row=3,column=1,ipadx='100')
        self.no_of_coursesf.grid(row=4,column=1,ipadx='100')
        self.no_of_creditsf.grid(row=5,column=1,ipadx='100')
        self.coursesf.grid(row=6,column=1,ipadx='100')
        self.skillsf.grid(row=7,column=1,ipadx='100')

        self.submit = ttk.Button(self.frame, text="Submit",command=self.insert)# fg="Black", bg="light green", command=self.insert) 
        self.submit.grid(row=8, column=1)#,sticky=W+E)
        self.clear = ttk.Button(self.frame, text="Clear",command=self.clearAll)#fg="Black", bg="light green", command=self.clearAll) 
        self.clear.grid(row=8, column=0)#,sticky=W+E)  
        self.root.mainloop()
    def create(self):
        pass
    def read(self):
        pass
    def update(self):
        pass
    def delete(self):
        pass
    def clearAll(self):
        self.rollnof.delete(0,'end')
        self.namef.delete(0,'end')
        self.addressf.delete(0,'end')
        self.popupmsg('Fields Cleared...')
        
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

    def popupmsg(self, msg):
        popup = Tk()
        popup.wm_title("!")
        label = ttk.Label(popup, text=msg)#, font=NORM_FONT)
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
        B1.pack()
        popup.mainloop()
        
            
def main():
    app=App()

if __name__=='__main__':
    main()
