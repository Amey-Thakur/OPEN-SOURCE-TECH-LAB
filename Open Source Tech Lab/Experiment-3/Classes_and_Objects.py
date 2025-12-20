#!/usr/bin/python3
# -----------------------------------------------------------------------------
# Script Name: Classes_and_Objects.py
# Experiment:  Experiment 3, Program 3.1
# Description: Demonstrates implementation of Classes and Objects in Python.
#              Includes Instance Methods, Class Methods, and Static Methods.
#
# Authors:     Amey Thakur
# Repository:  https://github.com/Amey-Thakur/OPEN-SOURCE-TECH-LAB
# License:     CC BY 4.0
# -----------------------------------------------------------------------------

import datetime

# -----------------------------------------------------------------------------
# STUDENT CLASS DEFINITION
# -----------------------------------------------------------------------------
class Student:
    """
    A class to represent a Student.
    Demonstrates class variables, instance variables, and different method types.
    """
    
    # Class Variables (Shared by all instances)
    no_of_courses = 5       
    credits = 25            

    def setval(self, rollno, name, addr, mob):
        """
        Instance Method: Sets the properties of the object (Instance Variables).
        """
        self.rollno = rollno   # Instance Variable
        self.name = name
        self.addr = addr       # Added 'addr' to match method signature logic
        self.mob = mob
    
    def getval(self):
        """
        Instance Method: Returns the properties of the object.
        """
        # id(self) returns the memory address of the current object instance
        print(f'Object Memory Address: {id(self)}')
        return self.rollno, self.name, self.no_of_courses, self.credits, self.mob

    @classmethod
    def setcourses(cls, n):
        """
        Class Method: Modifies the class variable 'no_of_courses'.
        Effects all instances of the class.
        """
        cls.no_of_courses = n
    
    @classmethod
    def setcredits(cls, c):
        """
        Class Method: Modifies the class variable 'credits'.
        """
        cls.credits = c

    @staticmethod
    def is_workday(day):
        """
        Static Method: Utility function checking if a date is a workday.
        Does not depend on class or instance state.
        Returns False if Sunday (weekday() == 6), else True.
        """
        if day.weekday() == 6:
            return False
        return True
    
# -----------------------------------------------------------------------------
# DRIVER CODE
# -----------------------------------------------------------------------------
print("\n--- 1. Creating Student Objects ---")

s1 = Student()
s1.setval('58', 'Mega', 'Mumbai', 9167078027)
print(f"Student 1 Details: {s1.getval()}")
print("-" * 30)

s2 = Student()
# Modifying instance variable specifically for s2 (shadowing class variable if name collided, but here logic is separate)
# Here we just modify s2's view if we were accessing it via instance, but we set class variable below.
# Note: In original code s2.no_of_courses = 6 created an instance variable 'no_of_courses' for s2, shadowing the class var.
s2.no_of_courses = 6 
s2.setval('50', 'Amey', 'Mumbai', 9191919191)
print(f"Student 2 Details: {s2.getval()}")
print("-" * 30)

print("\n--- 2. Inspecting Object Dictionaries (__dict__) ---")
# __dict__ attribute contains all writable instance attributes.
print(f'S1 __dict__: {s1.__dict__}')
print(f'S2 __dict__: {s2.__dict__}') # Will show 'no_of_courses': 6 because it was set on the instance
print("-" * 30)

print("\n--- 3. Class Methods (Modifying Class State) ---")
# Changing credits for ALL students using Class Method
Student.setcredits(30)
print(f"Updated Student 1 (New Credits 30): {s1.getval()}")
print("-" * 30)

print("\n--- 4. Static Methods (Utility) ---")
try:
    print("Check if a specific date is a workday:")
    # Hardcoding example input for demo purposes if not interactive, else taking input
    # Interactive input as per original program
    date = int(input('ENTER DATE (DD): '))
    month = int(input('ENTER MONTH (MM): '))
    year = int(input('ENTER YEAR (YYYY): '))
    
    d = datetime.date(year, month, date)
    is_working = Student.is_workday(d)
    status = "YES" if is_working else "NO"
    
    print(f'IS {d} A WORKDAY? {status}')

except ValueError:
    print("Error: Invalid Date Input.")

print("-" * 30)
