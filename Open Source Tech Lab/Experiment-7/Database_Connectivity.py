#!/usr/bin/python3
# -----------------------------------------------------------------------------
# Script Name: Database_Connectivity.py
# Experiment:  Experiment 7, Program 7.1
# Description: Demonstrates Python connectivity with MySQL database.
#              Includes CRUD (Create, Read, Update, Delete) operations.
#
# Authors:     Amey Thakur
# Repository:  https://github.com/Amey-Thakur/OPEN-SOURCE-TECH-LAB
# License:     CC BY 4.0
# -----------------------------------------------------------------------------

import mysql.connector
from mysql.connector import Error

def insert_record(cursor, conn):
    """
    Function to insert a new student record into the database.
    """
    try:
        print("\n--- Insert New Student Record ---")
        r = int(input('Enter Roll No:     '))
        n = input('Enter Full Name:   ')
        m = input('Enter Mobile No:   ')
        a = input('Enter Address:     ')
        c = input('Enter Courses:     ')
        cr = int(input('Enter Credits:     '))
        sk = input('Enter Skills:      ')
        co = int(input('Enter No. of Courses: '))

        query = "INSERT INTO Student (rollno, name, mob, address, courses, no_of_credits, skills, no_of_courses) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (r, n, m, a, c, cr, sk, co)
        
        cursor.execute(query, values)
        conn.commit()
        print('>> Record inserted successfully!')
    except ValueError:
        print('Error: Invalid numerical input.')
    except Error as e:
        print(f'Error: Database insertion failed: {e}')

def display_records(cursor):
    """
    Function to display all records from the Student table.
    """
    print("\n--- Displaying All Records ---")
    try:
        query = 'SELECT * FROM Student'
        cursor.execute(query)
        records = cursor.fetchall()
        
        if not records:
            print("No records found in the database.")
            return

        for row in records:
            print(row)
    except Error as e:
        print(f'Error: Could not retrieve records: {e}')

def update_record(cursor, conn):
    """
    Function to update an existing record by Roll No.
    """
    print("\n--- Update Existing Record ---")
    try:
        r = int(input('Enter Roll No to update: '))
        n = input('Enter New Name: ')
        
        query = "UPDATE Student SET name = %s WHERE rollno = %s"
        cursor.execute(query, (n, r))
        conn.commit()
        
        if cursor.rowcount > 0:
            print(f'>> Record for Roll No {r} updated successfully!')
        else:
            print(f'>> No record found with Roll No {r}.')
    except Error as e:
        print(f'Error: Update failed: {e}')

def delete_record(cursor, conn):
    """
    Function to delete a student record by Roll No.
    """
    print("\n--- Delete Student Record ---")
    try:
        r = int(input('Enter Roll No to delete: '))
        
        query = "DELETE FROM Student WHERE rollno = %s"
        cursor.execute(query, (r,))
        conn.commit()
        
        if cursor.rowcount > 0:
            print(f'>> Record for Roll No {r} deleted successfully!')
        else:
            print(f'>> No record found with Roll No {r}.')
    except Error as e:
        print(f'Error: Deletion failed: {e}')

def main():
    """
    Main driver for Database Connectivity demo.
    """
    try:
        # Configuration for local MySQL server
        conn = mysql.connector.connect(
            host="localhost",
            user="root",        # Updated to common default
            passwd="",          # Blank by default on many setups
            database="ostldb"   # Assuming ostldb exists
        )
        
        if conn.is_connected():
            cursor = conn.cursor()
            
            while True:
                print("\n" + "=" * 40)
                print("\tDATABASE OPERATIONS MENU")
                print("=" * 40)
                print("1. INSERT RECORD")
                print("2. DISPLAY ALL RECORDS")
                print("3. UPDATE RECORD (NAME)")
                print("4. DELETE RECORD")
                print("5. EXIT")
                print("=" * 40)
                
                try:
                    ch = int(input('Enter your choice: '))
                    if ch == 5:
                        break
                    elif ch == 1:
                        insert_record(cursor, conn)
                    elif ch == 2:
                        display_records(cursor)
                    elif ch == 3:
                        update_record(cursor, conn)
                    elif ch == 4:
                        delete_record(cursor, conn)
                    else:
                        print('Error: Invalid choice.')
                except ValueError:
                    print('Error: Please enter a number.')

            cursor.close()
            conn.close()
            print("\nDatabase connection closed. Goodbye!")
            
    except Error as e:
        print(f"Error: Could not connect to MySQL server: {e}")

if __name__ == '__main__':
    main()