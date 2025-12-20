#!/usr/bin/python3
# -----------------------------------------------------------------------------
# Script Name: Functions_Menu_Driven.py
# Experiment:  Experiment 2, Program 2.3
# Description: Demonstrates the implementation of Functions in Python.
#              Includes Menu-Driven logic for Factorial, Fibonacci, Summation, and Primality.
#
# Authors:     Amey Thakur
# Repository:  https://github.com/Amey-Thakur/OPEN-SOURCE-TECH-LAB
# License:     CC BY 4.0
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# FUNCTION DEFINITIONS
# -----------------------------------------------------------------------------

def fact(n):
    """
    Function to return the factorial value of a given integer.
    Recursive or iterative approach can be used; iterative is used here.
    """
    if not isinstance(n, int):
        return 'Error: Input must be an integer.'
    
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f

def fibo(n):
    """
    Function to return a list of the Fibonacci series up to a given integer n.
    """
    l = list()
    l.append(0)
    l.append(1)
    
    # Generate series while next term is <= n
    while (l[-1] + l[-2] <= n):
        l.append(l[-1] + l[-2])
    return l

def chkprime(n):
    """
    Function to check the primality of a given integer.
    Returns True if prime, False otherwise.
    """
    if n <= 1:
        return False
    # Check divisibility from 2 up to n/2
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True  

def sumfibo(n):
    """
    Function to return the summation of the Fibonacci series terms up to n.
    """
    l = fibo(n)
    total_sum = 0
    for i in l:
        total_sum += i
    return total_sum

# -----------------------------------------------------------------------------
# MAIN PROGRAM LOOP
# -----------------------------------------------------------------------------
while True:
    print("\n" + "=" * 40)
    print("\t\tMENU")
    print("=" * 40)
    print("1. FACTORIAL OF A GIVEN NUMBER")
    print("2. FIBONACCI SERIES OF GIVEN NUMBER")
    print("3. SUMMATION OF FIBONACCI SERIES")
    print("4. CHECK PRIMALITY")
    print("0. EXIT")
    print("=" * 40)

    try:
        ch = int(input('ENTER YOUR CHOICE: '))
        
        if ch == 0:
            print("Exiting... Goodbye!")
            break
            
        elif ch in range(1, 5):
            n = int(input('ENTER THE NUMBER: '))
            
            if ch == 1:
                print(f'FACTORIAL OF {n} IS: {fact(n)}')
            elif ch == 2:
                print(f'FIBONACCI SERIES TILL {n} IS: {fibo(n)}')
            elif ch == 3:
                print(f'SUMMATION OF FIBONACCI SERIES TILL {n} IS: {sumfibo(n)}')
            elif ch == 4:
                status = "PRIME" if chkprime(n) else "NOT PRIME"
                print(f'THE NUMBER {n} IS {status}')
        else:
            print('Error: Invalid Choice. Please enter a number between 0 and 4.')

    except ValueError:
        print("Error: Invalid Input. Please enter a valid integer.")