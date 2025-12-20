#!/usr/bin/python3
# -----------------------------------------------------------------------------
# Script Name: Data_Structures_And_String_Ops.py
# Experiment:  Experiment 1, Program 1.2
# Description: Demonstrates Python data structures (ByteArray, Range, Set) and
#              common String manipulation functions.
#
# Authors:     Amey Thakur
# Repository:  https://github.com/Amey-Thakur/OPEN-SOURCE-TECH-LAB
# License:     CC BY 4.0
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# 1. BYTEARRAYS
# -----------------------------------------------------------------------------
print("--- 1. ByteArrays ---")

# bytearray() returns a mutable sequence of integers in range 0 <= x <= 255
b = bytearray(3)
print(f"Byte array initialized (size 3): {b[0]}, {b[1]}, {b[2]}")

c = b'Mega'
print(f"Bytes literal: {c}")
print(f"Type: {type(c)}")
print("-" * 30)

# -----------------------------------------------------------------------------
# 2. RANGE
# -----------------------------------------------------------------------------
print("\n--- 2. Illustrating Range ---")

# range() returns an immutable sequence of numbers
r = range(10)
print(f"Range(10) start: {r[0]}, end index: {r[-1]}")

# Converting range to list to visualize contents
r_list = list(range(10, 20))
print(f"List from range(10, 20): {r_list}")
print("-" * 30)

# -----------------------------------------------------------------------------
# 3. SETS
# -----------------------------------------------------------------------------
print("\n--- 3. Illustration of Sets ---")

s1 = {1, 2, 3}
s2 = {3, 4, 5, 6}

print(f"Set 1: {s1}")
print(f"Set 2: {s2}")

# Intersection: Elements common to both sets
intersection = s1.intersection(s2)
print(f"Intersection of s1 and s2: {intersection}")

# Union: All unique elements from both sets
union_set = s1.union(s2)
print(f"Union of s1 and s2: {union_set}")

# Issuperset: Checks if a set contains all elements of another set
is_superset = union_set.issuperset(s1)
print(f"Is Union set superset of s1? {is_superset}")
print("-" * 30)

# -----------------------------------------------------------------------------
# 4. STRING FUNCTIONS
# -----------------------------------------------------------------------------
print("\n--- 4. Illustration of String Functions ---")

try:
    s = input('Enter a string: ')
    sub = input('Enter a substring to find: ')

    # String Reversal using slicing [start:end:step]
    print(f"Reverse of the string: {s[::-1]}")

    # Substring check
    is_substring = sub in s
    print(f"Is '{sub}' a substring of '{s}'? {is_substring}")

    # Uppercase conversion
    print(f"Uppercased: {s.upper()}")

except Exception as e:
    print(f"An error occurred: {e}")

print("-" * 30)
