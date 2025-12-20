#!/usr/bin/python3
# -----------------------------------------------------------------------------
# Script Name: GUI_Class_Implementation.py
# Experiment:  Experiment 6, Program 6.2
# Description: Demonstrates a Class-based GUI implementation using Python Tkinter.
#              Encapsulates GUI components and database logic within a Class.
#
# Authors:     Amey Thakur
# Repository:  https://github.com/Amey-Thakur/OPEN-SOURCE-TECH-LAB
# License:     CC BY 4.0
# -----------------------------------------------------------------------------

import tkinter as tk
from tkinter import messagebox
import mysql.connector

class StudentApp:
    """
    Class to manage the Student Information GUI application.
    """
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('OSTL Experiment 6.2 - Class-based GUI')
        self.root.geometry('550x450')
        self.root.configure(background='light blue')

        # UI Initialization
        self.create_widgets()
        self.prefill_data()
        
        self.root.mainloop()

    def create_widgets(self):
        """
        Creates and grids all UI components.
        """
        # Grid Configuration
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=2)

        # Labels
        labels_text = [
            "Roll No.", "Name", "Address", "Mobile", 
            "No. of Courses", "Credits", "Courses", "Skills"
        ]
        
        for i, text in enumerate(labels_text):
            tk.Label(
                self.root, text=text, bg="light blue", 
                font=('Arial', 10, 'bold')
            ).grid(row=i, column=0, padx=20, pady=8, sticky='w')

        # Entry Fields
        self.entry_roll = tk.Entry(self.root)
        self.entry_name = tk.Entry(self.root)
        self.entry_addr = tk.Entry(self.root)
        self.entry_mob = tk.Entry(self.root)
        self.entry_no_courses = tk.Entry(self.root)
        self.entry_credits = tk.Entry(self.root)
        self.entry_courses = tk.Entry(self.root)
        self.entry_skills = tk.Entry(self.root)

        # Gridding Entry Fields
        entries = [
            self.entry_roll, self.entry_name, self.entry_addr, self.entry_mob,
            self.entry_no_courses, self.entry_credits, self.entry_courses, self.entry_skills
        ]
        for i, entry in enumerate(entries):
            entry.grid(row=i, column=1, padx=20, pady=8, sticky='ew')

        # Buttons Frame
        btn_frame = tk.Frame(self.root, bg='light blue')
        btn_frame.grid(row=8, column=0, columnspan=2, pady=20, sticky='ew')
        btn_frame.columnconfigure(0, weight=1)
        btn_frame.columnconfigure(1, weight=1)

        # Submit Button
        self.submit_btn = tk.Button(
            btn_frame, text="Submit", fg="Black", bg="light green", 
            font=('Arial', 11, 'bold'), command=self.insert_to_db
        )
        self.submit_btn.grid(row=0, column=1, padx=10, sticky='ew')

        # Clear Button
        self.clear_btn = tk.Button(
            btn_frame, text="Clear Fields", fg="Black", bg="#ff9999", 
            font=('Arial', 11, 'bold'), command=self.clear_all
        )
        self.clear_btn.grid(row=0, column=0, padx=10, sticky='ew')

    def prefill_data(self):
        """
        Pre-fills the form with sample data for demonstration.
        """
        self.entry_roll.insert(0, "58")
        self.entry_name.insert(0, "Mega")
        self.entry_addr.insert(0, "Mumbai")
        self.entry_mob.insert(0, "9167078027")
        self.entry_no_courses.insert(0, "5")
        self.entry_credits.insert(0, "25")
        self.entry_courses.insert(0, "Python Programming")
        self.entry_skills.insert(0, "Logic, Design")

    def clear_all(self):
        """
        Clears all entry fields.
        """
        self.entry_roll.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)
        self.entry_addr.delete(0, tk.END)
        self.entry_mob.delete(0, tk.END)
        self.entry_no_courses.delete(0, tk.END)
        self.entry_credits.delete(0, tk.END)
        self.entry_courses.delete(0, tk.END)
        self.entry_skills.delete(0, tk.END)
        print("Fields Cleared.")

    def insert_to_db(self):
        """
        Extracts data from UI and inserts into the MySQL database.
        """
        # Fetching data
        roll = self.entry_roll.get()
        name = self.entry_name.get()
        addr = self.entry_addr.get()
        mob = self.entry_mob.get()
        courses = self.entry_courses.get()
        credits = self.entry_credits.get()
        skills = self.entry_skills.get()
        no_courses = self.entry_no_courses.get()

        try:
            mydb = mysql.connector.connect(
                host='localhost',
                user='root',
                passwd='',
                database='ostldb'
            )
            mycursor = mydb.cursor()
            
            # Parametric query to avoid SQL injection
            query = "INSERT INTO Student (rollno, name, mob, address, courses, no_of_credits, skills, no_of_courses) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            values = (roll, name, mob, addr, courses, credits, skills, no_courses)
            
            print(f"Attempting to insert: {values}")
            mycursor.execute(query, values)
            mydb.commit()
            
            messagebox.showinfo("Success", f"Data for {name} inserted successfully!")
            
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        except Exception as e:
            messagebox.showerror("Error", f"Unexpected error: {e}")

def main():
    StudentApp()

if __name__ == '__main__':
    main()
