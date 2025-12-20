#!/usr/bin/python3
# -----------------------------------------------------------------------------
# Script Name: Basic_Datatypes_And_IO.py
# Experiment:  Experiment 1, Program 1.1
# Description: Demonstrates basic Python concepts including Comments, Datatypes, 
#              Expressions, and Input/Output functions.
#
# Authors:     Amey Thakur
# Repository:  https://github.com/Amey-Thakur/OPEN-SOURCE-TECH-LAB
# License:     CC BY 4.0
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# 1. COMMENTS
# -----------------------------------------------------------------------------
# Single line comment: Begins with a hash (#) character.
# Terminated automatically at the end of the line.

"""
Multi-line comment (Docstring):
Used to explain code in more detail.
Created by adding a delimiter (''') or ( \"\"\" ) on each end.
"""

print("--- 1. Comments ---")
print("hello")
print("-" * 30)

# -----------------------------------------------------------------------------
# 2. DATATYPES
# -----------------------------------------------------------------------------
print("\n--- 2. Illustration of Data Types ---")

i = 10              # Integer
f = 24.5            # Float
s = 'Hello user'    # String
c = 2 + 3j          # Complex number

print(f"Integer value: {i}")
print(f"Float value:   {f}")
print(f"String value:  {s}")
print(f"Complex value: {c}")
print("-" * 30)

# -----------------------------------------------------------------------------
# 3. EXPRESSIONS
# -----------------------------------------------------------------------------
print("\n--- 3. Illustration of Expressions ---")

# Division (/) returns float
print(f"Division (21/i):      {21 / i}")

# Floor Division (//) returns integer quotient
print(f"Quotient (21//i):     {21 // i}")

# Modulus (%) returns remainder
print(f"Remainder (21%i):     {21 % i}")

# Exponentiation (**) or pow()
print(f"Power of 2 to 3:      {2 ** 3}")

# divmod(x, y) returns a tuple (quotient, remainder)
print(f"Divmod of 5/2:        {divmod(5, 2)}")

x, y = divmod(5, 2)
print(f"Unpacked Divmod:      Quotient={x}, Remainder={y}")
print("-" * 30)

# -----------------------------------------------------------------------------
# 4. INPUT AND OUTPUT FUNCTIONS
# -----------------------------------------------------------------------------
print("\n--- 4. Illustration of Input and Output Functions ---")
print("(User Input Required)")

# Taking user input and explicitly casting to target datatypes
try:
    i_input = int(input('Enter an Integer: '))
    f_input = float(input('Enter a Float:    '))
    s_input = input('Enter a String:   ')
    # Complex input can be '1+2j'
    c_input = complex(input('Enter a Complex:  '))

    print("\n--- User Input Results ---")
    print(f"Integer value: {i_input}")
    print(f"Float value:   {f_input}")
    print(f"String value:  {s_input}")
    print(f"Complex value: {c_input}")

except ValueError as e:
    print(f"\nError: Invalid input format. {e}")

print("-" * 30)
