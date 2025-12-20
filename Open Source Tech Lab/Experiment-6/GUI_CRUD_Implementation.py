#!/usr/bin/python3
# -----------------------------------------------------------------------------
# Script Name: GUI_CRUD_Implementation.py
# Experiment:  Experiment 6, Program 6.3
# Description: Advanced GUI implementation with Menus and CRUD Operation stubs.
#              Uses ttk themed widgets for a modern look.
#
# Authors:     Amey Thakur
# Repository:  https://github.com/Amey-Thakur/OPEN-SOURCE-TECH-LAB
# License:     CC BY 4.0
# -----------------------------------------------------------------------------

import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

class AdvancedApp:
    """
    Advanced Student Management GUI with Menu navigation.
    """
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('OSTL Experiment 6.3 - Advanced CRUD GUI')
        self.root.geometry('700x600')
        
        # Theme/Style
        self.style = ttk.Style()
        self.style.configure("TLabel", font=('Arial', 10))
        self.style.configure("TButton", font=('Arial', 10, 'bold'))

        self.setup_menu()
        self.setup_ui()
        self.prefill_data()
        
        self.root.mainloop()

    def setup_menu(self):
        """
        Configures the top menu bar.
        """
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # CRUD Menu
        crud_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='Operations', menu=crud_menu)
        crud_menu.add_command(label='Create / Insert', command=self.insert_to_db)
        crud_menu.add_command(label='Read / Search', command=lambda: messagebox.showinfo("Info", "Search functionality stub"))
        crud_menu.add_command(label='Update Record', command=lambda: messagebox.showinfo("Info", "Update functionality stub"))
        crud_menu.add_command(label='Delete Record', command=lambda: messagebox.showinfo("Info", "Delete functionality stub"))
        crud_menu.add_separator()
        crud_menu.add_command(label='Exit', command=self.root.quit)

        # Help Menu
        help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='Help', menu=help_menu)
        help_menu.add_command(label='About', command=lambda: messagebox.showinfo("About", "OSTL Advanced GUI Demo\nCreated for academic purposes."))

    def setup_ui(self):
        """
        Builds the main container and widgets.
        """
        # Background Canvas
        self.canvas = tk.Canvas(self.root, height=600, width=700, bg='#2c3e50')
        self.canvas.pack(fill="both", expand=True)

        # Central Frame
        self.main_frame = tk.Frame(self.root, bg='white', padx=20, pady=20)
        self.main_frame.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.8, relheight=0.8)

        # Title
        tk.Label(
            self.main_frame, text="STUDENT REGISTRATION FORM", 
            bg='white', font=('Arial', 14, 'bold'), fg='#2c3e50'
        ).grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Form Fields
        labels = [
            "Roll No.", "Full Name", "Address", "Mobile Number", 
            "No. of Courses", "Total Credits", "Specific Courses", "Technical Skills"
        ]
        
        self.entries = {}
        vars = [
            "roll", "name", "addr", "mob", 
            "no_courses", "credits", "courses", "skills"
        ]

        for i, (lbl, var_name) in enumerate(zip(labels, vars)):
            ttk.Label(self.main_frame, text=lbl, background='white').grid(row=i+1, column=0, sticky='w', pady=5)
            ent = ttk.Entry(self.main_frame, width=40)
            ent.grid(row=i+1, column=1, sticky='ew', pady=5, padx=(10, 0))
            self.entries[var_name] = ent

        # Button Group
        btn_frame = tk.Frame(self.main_frame, bg='white')
        btn_frame.grid(row=9, column=0, columnspan=2, pady=30)

        self.btn_submit = ttk.Button(btn_frame, text="SUBMIT DATA", command=self.insert_to_db)
        self.btn_submit.pack(side='right', padx=10)

        self.btn_clear = ttk.Button(btn_frame, text="CLEAR FIELDS", command=self.clear_all)
        self.btn_clear.pack(side='left', padx=10)

    def prefill_data(self):
        """
        Pre-fills with 'Mega' data for demo.
        """
        self.entries["roll"].insert(0, "58")
        self.entries["name"].insert(0, "Mega")
        self.entries["addr"].insert(0, "Mumbai")
        self.entries["mob"].insert(0, "9167078027")
        self.entries["no_courses"].insert(0, "5")
        self.entries["credits"].insert(0, "25")
        self.entries["courses"].insert(0, "Open Source Technologies")
        self.entries["skills"].insert(0, "Python, Git, UI/UX")

    def clear_all(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        messagebox.showinfo("Status", "All fields cleared.")

    def insert_to_db(self):
        """
        Database Insertion Logic.
        """
        data = {k: v.get() for k, v in self.entries.items()}
        
        try:
            mydb = mysql.connector.connect(
                host='localhost', user='root', passwd='', database='ostldb'
            )
            mycursor = mydb.cursor()
            
            query = (
                "INSERT INTO Student (rollno, name, mob, address, courses, no_of_credits, skills, no_of_courses) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            )
            values = (
                data["roll"], data["name"], data["mob"], data["addr"], 
                data["courses"], data["credits"], data["skills"], data["no_courses"]
            )
            
            mycursor.execute(query, values)
            mydb.commit()
            messagebox.showinfo("Success", f"Registration for {data['name']} completed!")
            
        except mysql.connector.Error as err:
            messagebox.showerror("DB Error", f"Registration Failed: {err}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

def main():
    AdvancedApp()

if __name__ == '__main__':
    main()
