#!/usr/bin/python3
# -----------------------------------------------------------------------------
# Script Name: Inheritance_Implementation.py
# Experiment:  Experiment 4, Program 4.1
# Description: Demonstrates Inheritance in Python (Single Inheritance).
#              The SECO class inherits properties and methods from the Student class.
#
# Authors:     Amey Thakur
# Repository:  https://github.com/Amey-Thakur/OPEN-SOURCE-TECH-LAB
# License:     CC BY 4.0
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# PARENT CLASS (BASE CLASS)
# -----------------------------------------------------------------------------
class Student:
    """
    Base Class representing a generic Student.
    """
    no_of_courses = 5
    credits = 25

    def __init__(self, *args):
        """
        Constructor with variable arguments (*args) to simulate Method Overloading.
        Can initialize empty, from another object, or with specific values.
        """
        if len(args) == 0:
            # Default initialization
            self.rollno = None
            self.name = None
            self.addr = None
            self.mob = None
        elif isinstance(args[0], Student):
            # Copy Constructor logic (initializing from another Student object)
            self.rollno = args[0].rollno
            self.name = args[0].name
            self.addr = args[0].addr
            self.mob = args[0].mob
        elif len(args) == 4:
            # Detailed initialization
            self.setval(args[0], args[1], args[2], args[3])
        else:
            print("Error: Invalid arguments passed to Student Constructor.")

    def setval(self, rollno, name, addr, mob):
        """
        Method to set student details.
        """
        self.rollno = rollno
        self.name = name
        self.addr = addr
        self.mob = mob

    def getval(self):
        """
        Method to print student details.
        """
        print(f'RollNo:        {self.rollno}')
        print(f'Name:          {self.name}')
        print(f'No. of Courses:{self.no_of_courses}')
        print(f'Credits:       {self.credits}')
        print(f'Mobile:        {self.mob}')


# -----------------------------------------------------------------------------
# CHILD CLASS (DERIVED CLASS)
# -----------------------------------------------------------------------------
class SECO(Student):
    """
    Derived Class inherited from Student.
    Represents a specific category of student (e.g., SE Computer Engineering).
    """
    courses = list()
    skills = list()

    def __init__(self):
        """
        Constructor for Child Class.
        Invokes Parent Class Constructor.
        Includes basic Error Handling demonstration.
        """
        try:
            # Invoking Parent Class Constructor
            super().__init__() 
        except Exception as e:
            print(f'Initialization Error: {e}')

    def setprop(self, course, skill):
        """
        Method to add courses and desired skills.
        Specific to SECO students.
        """
        self.courses.append(course)
        self.skills.append(skill)

    def getprop(self):
        """
        Method to retrieve all properties.
        Calls parent method getval() to print basic details, then prints specific details.
        """
        print("\n--- Student Details (Inherited) ---")
        self.getval() # Calling method from Parent Class
        
        print("--- Additional Properties (Child Class) ---")
        print(f'Courses:       {self.courses}')
        print(f'Skills:        {self.skills}')


# -----------------------------------------------------------------------------
# DRIVER CODE
# -----------------------------------------------------------------------------
print("\n--- Inheritance Demonstration ---")

# Creating an object of the Child Class (SECO)
s = SECO()

# Using Parent Class method to set values
s.setval('58', 'Mega', 'Mumbai', 9167078027)

# Using Child Class method to set specific properties
s.setprop('OSTL', 'Python')
s.setprop('AOA', 'Design Algos')
s.setprop('CG', 'C Programming')

# Displaying all properties (Child + Parent)
s.getprop()

print("-" * 30)
