#!/usr/bin/python3
# -----------------------------------------------------------------------------
# Script Name: If_Else_Logic.py
# Experiment:  Experiment 2, Program 2.1
# Description: Demonstrates decision making using IF-ELSE statements in Python.
#              Includes integer comparison, string comparison, and memory address checks.
#
# Authors:     Amey Thakur
# Repository:  https://github.com/Amey-Thakur/OPEN-SOURCE-TECH-LAB
# License:     CC BY 4.0
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# 1. IF-ELSE CONDITION (NUMBER COMPARISON)
# -----------------------------------------------------------------------------
# Decision making is required when we want to execute code only if a condition is satisfied.
# Syntax:
#   if test expression:
#       Body of if
#   else:
#       Body of else

print("\n--- 1. Condition: Number Comparison ---")

try:
    f = int(input("ENTER FIRST NO.:  "))
    s = int(input("ENTER SECOND NO.: "))
    t = int(input("ENTER THIRD NO.:  "))

    print("\nResult:")
    if f > s:
        if f > t:
            print(f"{f} IS THE LARGEST NUMBER!")
        else:
            print(f"{t} IS THE LARGEST NUMBER!")
    elif s > t:
        print(f"{s} IS THE LARGEST NUMBER!")
    else:
        print(f"{t} IS THE LARGEST NUMBER!")

except ValueError:
    print("Error: Please enter valid integers.")

print("-" * 30)

# -----------------------------------------------------------------------------
# 2. STRING COMPARISON
# -----------------------------------------------------------------------------
print("\n--- 2. Condition: String Comparison ---")

s1 = input("ENTER FIRST STRING:  ")
s2 = input("ENTER SECOND STRING: ")

print(f"\nTHE COMPARED STRINGS ARE '{s1}' & '{s2}'")

# Convert to uppercase for case-insensitive comparison
s1_upper = s1.upper()
s2_upper = s2.upper()

if s1_upper == s2_upper:
    print("Result: STRINGS ARE SIMILAR!")
else:
    print("Result: STRINGS ARE DIFFERENT!")

print("-" * 30)

# -----------------------------------------------------------------------------
# 3. IDENTITY OPERATORS (is / id())
# -----------------------------------------------------------------------------
print("\n--- 3. Memory Address Check (Identity) ---")

st1 = "MEGA"
print(f"Address of st1 ('MEGA'): {id(st1)}")

print("")

st1 = "AMEY"
st2 = "AMEY"

# Python optimizes memory by assigning the same address to identical string literals (interning)
print(f"Address of st1 ('AMEY'): {id(st1)}")
print(f"Address of st2 ('AMEY'): {id(st2)}")

if id(st1) == id(st2):
    print("Result: Both variables point to the same memory location.")
else:
    print("Result: Variables point to different memory locations.")

print("-" * 30)
