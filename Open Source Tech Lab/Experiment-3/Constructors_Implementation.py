#!/usr/bin/python3
# -----------------------------------------------------------------------------
# Script Name: Constructors_Implementation.py
# Experiment:  Experiment 3, Program 3.2
# Description: Demonstrates implementation of Constructors (__init__) in Python.
#              Shows object initialization with default and custom arguments.
#
# Authors:     Amey Thakur
# Repository:  https://github.com/Amey-Thakur/OPEN-SOURCE-TECH-LAB
# License:     CC BY 4.0
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# STUDENT CLASS DEFINITION
# -----------------------------------------------------------------------------
class Student:
    """
    Student class with a Constructor and basic variable management.
    """
    # Class Variables
    no_of_courses = 5
    credits = 25

    def __init__(self, r=0, n='', a='', m=0):
        """
        Constructor (__init__): Initializes the object state.
        Arguments with default values allow flexible object creation.
        """
        self.rollno = r
        self.name = n
        self.addr = a
        self.mob = m
        print(f">> Student Object Created: {self.name if self.name else 'Unknown'}")
        
    def setval(self, rollno, name, addr, mob):
        """
        Method to update object properties after creation.
        """
        self.rollno = rollno
        self.name = name
        self.addr = addr
        self.mob = mob

    def getval(self):
        """
        Returns a tuple of student details.
        """
        return self.rollno, self.name, self.no_of_courses, self.credits, self.mob

    @classmethod
    def setcourses(cls, n):
        cls.no_of_courses = n

    @classmethod
    def setcredits(cls, c):
        cls.credits = c

    @staticmethod
    def is_workday(day):
        if day.weekday() == 6:
            return False
        return True

# -----------------------------------------------------------------------------
# DRIVER CODE
# -----------------------------------------------------------------------------
print("\n--- 1. Constructor Usage ---")

# 1. Object creation with arguments provided to Constructor
# Note: '1' passed as Number, '9822' passed as Number.
s1 = Student(58, 'Mega', 'Mumbai', 9167078027) 
print(f"Details s1: {s1.getval()}")

# 2. Object creation with Default Constructor Arguments
s2 = Student()
print(f"Details s2 (Default): {s2.getval()}")

# Modifying s2 values using setval
print("\n--- 2. Updating Object Data ---")
s2.setval('50', 'Amey', 'Mumbai', 9898998989)
print(f"Details s2 (Updated): {s2.getval()}")

# 3. Another Object creation demonstrating flexibility
print("\n--- 3. Multiple Instances ---")
s3 = Student()
s3.setval('17CO35', 'SS', 'M', 9898)
print(f"Details s3: {s3.getval()}")
print(f"Memory Address s3: {id(s3)}")

s4 = Student()
s4.setval('17CO35', 'SS', 'M', 9898) # Same data as s3
print(f"Details s4: {s4.getval()}")
print(f"Memory Address s4: {id(s4)}")

if id(s3) != id(s4):
    print(">> s3 and s4 have different memory addresses (distinct objects).")

print("-" * 30)
