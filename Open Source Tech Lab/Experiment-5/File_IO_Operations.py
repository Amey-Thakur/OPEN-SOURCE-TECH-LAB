#!/usr/bin/python3
# -----------------------------------------------------------------------------
# Script Name: File_IO_Operations.py
# Experiment:  Experiment 5, Program 5.1
# Description: Demonstrates File Input/Output operations in Python.
#              Includes Reading, Writing, and Appending to files.
#
# Authors:     Amey Thakur
# Repository:  https://github.com/Amey-Thakur/OPEN-SOURCE-TECH-LAB
# License:     CC BY 4.0
# -----------------------------------------------------------------------------

import os

def readf():
    """
    Function to read data from a file line by line.
    Handles FileNotFoundError and other OS errors.
    """
    fname = input('Enter filename to read: ')
    try:
        with open(fname, 'r') as f:
            print(f"\n--- Content of '{fname}' ---")
            for line in f:
                print(line, end='')
            print("\n" + "-" * 30)
            
    except FileNotFoundError:
        print(f"Error: The file '{fname}' does not exist.")
    except OSError as e:
        print(f"System Error: {e}")

def writef():
    """
    Function to write data to a file (Overwrites existing content).
    Creates the file if it doesn't exist.
    """
    fname = input('Enter filename to write: ')
    try:
        with open(fname, 'w') as f:
            print(f"Writing to '{fname}'... (Type 'exit' to stop)")
            while True:
                data = input('Enter Data: ')
                if data.lower() == 'exit':
                    break
                f.write(data + '\n')
        print(f"Successfully wrote to '{fname}'.")
        
    except OSError as e:
        print(f"System Error: {e}")

def appendf():
    """
    Function to append data to an existing file.
    Creates the file if it doesn't exist.
    """
    fname = input('Enter filename to append to: ')
    try:
        with open(fname, 'a') as f:
            print(f"Appending to '{fname}'... (Type 'exit' to stop)")
            while True:
                data = input('Enter Data: ')
                if data.lower() == 'exit':
                    break
                f.write(data + '\n')
        print(f"Successfully appended to '{fname}'.")
        
    except OSError as e:
        print(f"System Error: {e}")

def main():
    """
    Main Menu Driver
    """
    while True:
        print("\n" + "=" * 40)
        print("\t\tFILE OPERATIONS MENU")
        print("=" * 40)
        print("1. DISPLAY FILE CONTENT")
        print("2. WRITE TO FILE")
        print("3. APPEND TO FILE")
        print("4. QUIT")
        print("=" * 40)

        try:
            choice = int(input('Enter your choice: '))
            
            if choice == 1:
                readf()
            elif choice == 2:
                writef()
            elif choice == 3:
                appendf()
            elif choice == 4:
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid Choice. Please try again.")
                
        except ValueError:
            print("Error: Invalid Input. Please enter a number.")

if __name__ == '__main__':
    main()
