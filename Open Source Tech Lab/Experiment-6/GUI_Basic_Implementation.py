#!/usr/bin/python3
# -----------------------------------------------------------------------------
# Script Name: GUI_Basic_Implementation.py
# Experiment:  Experiment 6, Program 6.1
# Description: Demonstrates basic GUI implementation using Python Tkinter.
#              Creating Labels, Entry fields, and Buttons.
#
# Authors:     Amey Thakur
# Repository:  https://github.com/Amey-Thakur/OPEN-SOURCE-TECH-LAB
# License:     CC BY 4.0
# -----------------------------------------------------------------------------

import tkinter as tk
from tkinter import messagebox
import mysql.connector

# -----------------------------------------------------------------------------
# DATABASE HANDLER
# -----------------------------------------------------------------------------
def insert_data(roll, name, addr, mob, courses, credits, skills, no_courses):
    """
    Function to insert data into MySQL database.
    Note: Requires a running MySQL server with 'ostldb' database.
    """
    try:
        # Placeholder connection details - configured for local setup
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',       # Changed from hardcoded 'ostl' for general compatibility
            passwd='',         
            database='ostldb'
        )
        mycursor = mydb.cursor()
        
        query = f"INSERT INTO Student VALUES ({roll}, '{name}', '{mob}', '{addr}', '{courses}', {credits}, '{skills}', {no_courses})"
        print(f"Executing Query: {query}")
        
        mycursor.execute(query)
        mydb.commit()
        messagebox.showinfo("Success", "Data Inserted Successfully!")
        return True
        
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
        messagebox.showerror("Database Error", f"Could not insert data.\nError: {err}")
        return False
    except Exception as e:
        print(f"Error: {e}")
        messagebox.showerror("Error", f"An error occurred: {e}")
        return False

# -----------------------------------------------------------------------------
# MAIN GUI APPLICATION
# -----------------------------------------------------------------------------
def main():
    root = tk.Tk()
    root.title('OSTL Experiment 6.1 - Basic GUI')
    root.geometry('500x400')
    root.configure(background='light blue')

    # Grid Configuration
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=2)

    # --- Labels ---
    labels = ["Roll No.", "Name", "Address", "Mobile", "No. of Courses", "Credits", "Courses", "Skills"]
    row_count = 0
    
    for lbl_text in labels:
        tk.Label(root, text=lbl_text, bg="light blue", font=('Arial', 10, 'bold')).grid(row=row_count, column=0, padx=10, pady=5, sticky='w')
        row_count += 1

    # --- Entry Fields ---
    # We keep references to entry fields to fetch data later
    entry_roll = tk.Entry(root)
    entry_name = tk.Entry(root)
    entry_addr = tk.Entry(root)
    entry_mob = tk.Entry(root)
    entry_no_courses = tk.Entry(root)
    entry_credits = tk.Entry(root)
    entry_courses = tk.Entry(root)
    entry_skills = tk.Entry(root)

    # Placing Entry Fields
    entry_roll.grid(row=0, column=1, padx=10, pady=5, sticky='ew')
    entry_name.grid(row=1, column=1, padx=10, pady=5, sticky='ew')
    entry_addr.grid(row=2, column=1, padx=10, pady=5, sticky='ew')
    entry_mob.grid(row=3, column=1, padx=10, pady=5, sticky='ew')
    entry_no_courses.grid(row=4, column=1, padx=10, pady=5, sticky='ew')
    entry_credits.grid(row=5, column=1, padx=10, pady=5, sticky='ew')
    entry_courses.grid(row=6, column=1, padx=10, pady=5, sticky='ew')
    entry_skills.grid(row=7, column=1, padx=10, pady=5, sticky='ew')

    # --- Pre-filling with Sample Data (Standardized) ---
    entry_roll.insert(0, "58")
    entry_name.insert(0, "Mega")
    entry_addr.insert(0, "Mumbai")
    entry_mob.insert(0, "9167078027")
    entry_no_courses.insert(0, "5")
    entry_credits.insert(0, "25")
    entry_courses.insert(0, "OSTL, AOA, CG")
    entry_skills.insert(0, "Python, SQL")

    # --- Submit Handler ---
    def on_submit():
        insert_data(
            entry_roll.get(),
            entry_name.get(),
            entry_addr.get(),
            entry_mob.get(),
            entry_courses.get(),
            entry_credits.get(),
            entry_skills.get(),
            entry_no_courses.get()
        )

    # --- Submit Button ---
    submit_btn = tk.Button(root, text="Submit", fg="Black", bg="light green", font=('Arial', 12, 'bold'), command=on_submit)
    submit_btn.grid(row=8, column=1, pady=20, sticky='ew', padx=10)

    root.mainloop()

if __name__ == '__main__':
    main()