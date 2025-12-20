#!/usr/bin/python3
# -----------------------------------------------------------------------------
# Script Name: Lambda_Filter_Map_Reduce.py
# Experiment:  Experiment 5, Program 5.2
# Description: Demonstrates functional programming concepts in Python.
#              Uses Lambda functions with Filter, Map, and Reduce.
#
# Authors:     Amey Thakur
# Repository:  https://github.com/Amey-Thakur/OPEN-SOURCE-TECH-LAB
# License:     CC BY 4.0
# -----------------------------------------------------------------------------

from functools import reduce

def get_list_input():
    """
    Helper function to take a list of integers from the user.
    """
    li = list()
    try:
        n = int(input('How many elements do you want in the list? '))
        for i in range(n):
            elem = int(input(f'Enter element {i+1}: '))
            li.append(elem)
        return li
    except ValueError:
        print("Error: Please enter valid integers.")
        return []

def main():
    """
    Main Menu Driver
    """
    while True:
        print("\n" + "=" * 50)
        print("\t\tLAMBDA FUNCTIONS MENU")
        print("=" * 50)
        print("1. FILTER: Filter Odd Numbers from List")
        print("2. MAP:    Square every number in List")
        print("3. REDUCE: Calculate Sum of all numbers in List")
        print("4. QUIT")
        print("=" * 50)

        try:
            ch = int(input('Enter your choice: '))
            
            if ch == 4:
                print("Exiting... Goodbye!")
                break
                
            elif ch == 1:
                # FILTER: Filters elements based on a condition (True/False)
                # Syntax: filter(function, iterable)
                print("\n--- 1. Lambda with Filter (Odd Numbers) ---")
                data_list = get_list_input()
                if data_list:
                    odd_list = list(filter(lambda x: (x % 2 != 0), data_list))
                    print(f'Original List: {data_list}')
                    print(f'Filtered List (Odd): {odd_list}')

            elif ch == 2:
                # MAP: Applies a function to every item in the iterable
                # Syntax: map(function, iterable)
                print("\n--- 2. Lambda with Map (Square Numbers) ---")
                data_list = get_list_input()
                if data_list:
                    sqr_list = list(map(lambda x: x**2, data_list))
                    print(f'Original List: {data_list}')
                    print(f'Mapped List (Squares): {sqr_list}')

            elif ch == 3:
                # REDUCE: Apply a rolling computation to sequential pairs of values in a list
                # Syntax: reduce(function, iterable)
                print("\n--- 3. Lambda with Reduce (Summation) ---")
                data_list = get_list_input()
                if data_list:
                    total_sum = reduce(lambda x, y: x + y, data_list)
                    print(f'Original List: {data_list}')
                    print(f'Reduced Result (Sum): {total_sum}')
            
            else:
                print("Invalid Choice. Please try again.")

        except ValueError:
            print("Error: Invalid Input. Please enter a number.")

if __name__ == '__main__':
    main()
