#!/usr/bin/python3
# -----------------------------------------------------------------------------
# Script Name: Loops_Factorial_Fibonacci.py
# Experiment:  Experiment 2, Program 2.2
# Description: Demonstrates the implementation of FOR and WHILE loops in Python.
#              Calculates Factorial (For Loop) and Fibonacci Series (While Loop).
#
# Authors:     Amey Thakur
# Repository:  https://github.com/Amey-Thakur/OPEN-SOURCE-TECH-LAB
# License:     CC BY 4.0
# -----------------------------------------------------------------------------

try:
    n = int(input('ENTER A NUMBER: '))
except ValueError:
    print("Error: Please enter a valid integer.")
    exit()

# -----------------------------------------------------------------------------
# 1. FOR LOOP (FACTORIAL CALCULATION)
# -----------------------------------------------------------------------------
# FOR loop is used to iterate over a sequence (list, tuple, string) or other iterable objects.
# Syntax:
#   for val in sequence:
#       Body of for

print("\n--- 1. Loop: Factorial Calculation (FOR Loop) ---")

f = 1
# Range is inclusive of start, exclusive of stop. So range(1, n+1) goes from 1 to n.
for i in range(1, n + 1):
    f = f * i

print(f'FACTORIAL OF {n} IS: {f}')
print("-" * 30)

# -----------------------------------------------------------------------------
# 2. WHILE LOOP (FIBONACCI SERIES)
# -----------------------------------------------------------------------------
# WHILE loop repeats a block of code as long as the test condition is true.
# Syntax:
#   while test_expression:
#       Body of while

print("\n--- 2. Loop: Fibonacci Series (WHILE Loop) ---")

a, b = 0, 1
c = a + b

# Using 'end=" "' to print on the same line separated by space
print(f'FIBONACCI SERIES TILL {n} IS: {a} {b}', end=' ')

while c <= n:
    print(c, end=' ')
    # Swap variables for next iteration
    a, b = b, c
    c = a + b

print('\n' + "-" * 30)