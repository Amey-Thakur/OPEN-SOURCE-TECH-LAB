#!/usr/bin/python3
# -----------------------------------------------------------------------------
# Script Name: Advanced_Data_Structures.py
# Experiment:  Experiment 1, Program 1.3
# Description: Implementation of Lists, Tuples, Dictionaries, and Arrays in Python.
#              Demonstrates creation, manipulation, and various built-in functions.
#
# Authors:     Amey Thakur
# Repository:  https://github.com/Amey-Thakur/OPEN-SOURCE-TECH-LAB
# License:     MIT License
# -----------------------------------------------------------------------------

from array import array

# -----------------------------------------------------------------------------
# 1. LISTS
# -----------------------------------------------------------------------------
print("--- 1. List Operations ---")

# Creating a list with mixed data types
l = [12, 23, -5, 0.8, 'python', "CO"]

print(f"Original List:            {l}")
print(f"First three elements:     {l[0:3]}")
print(f"Last element:             {l[-1]}")
print(f"First three elements * 2: {l[0:3] * 2}") # Repeats the slice twice
print("-" * 30)

print("\n--- List Functions ---")

# Creating a list from a range
l1 = list(range(1, 8)) # Generates [1, 2, 3, 4, 5, 6, 7]
print(f"List from range(1, 8):    {l1}")

# Append
l1.append(9)
print(f"After append(9):          {l1}")

# Sort (Descending)
l1.sort(reverse=True)
print(f"Descending Sort:          {l1}")

# Sort (Ascending)
l1.sort()
print(f"Ascending Sort:           {l1}")

# Reverse
l1.reverse()
print(f"Reverse:                  {l1}")

# Remove
l1.sort() # Sorting back to cleaner state
if 9 in l1:
    l1.remove(9)
print(f"After remove(9):          {l1}")

# Statistical functions
print(f"Count of 5:               {l1.count(5)}")
print(f"Max value:                {max(l1)}")
print(f"Min value:                {min(l1)}")
if 6 in l1:
    print(f"Index of 6:               {l1.index(6)}")

print("-" * 30)

print("\n--- Matrices using Lists ---")
m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in m1:
    print(row)
print("-" * 30)


# -----------------------------------------------------------------------------
# 2. TUPLES (Read-Only Lists)
# -----------------------------------------------------------------------------
print("\n--- 2. Tuple Operations ---")

tpl = (-5, 0.8, 'python', 'bj')
print(f"Created Tuple:            {tpl}")
print(f"Elements 0 to 2:          {tpl[0:2]}")

print("\n--- Tuple Functions ---")
tpl2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1)
print(f"Second Tuple:             {tpl2}")
print(f"Length:                   {len(tpl2)}")
print(f"Min:                      {min(tpl2)}")
print(f"Max:                      {max(tpl2)}")
print(f"Count of 1s:              {tpl2.count(1)}") # Corrected from 10 to 1 based on actual data
print(f"Reverse Sorted List:      {sorted(tpl2, reverse=True)}") # sorted() returns a list
print("-" * 30)


# -----------------------------------------------------------------------------
# 3. DICTIONARIES (Key:Value Pairs)
# -----------------------------------------------------------------------------
print("\n--- 3. Dictionary Operations ---")

d1 = {'NAME': "CO", 'GENDER': "M", 'age': "19", 'COLLEGE': "AITKTC"}
print(f"Dictionary:               {d1}")

print(f"Keys:                     {list(d1.keys())}")
print(f"Values:                   {list(d1.values())}")
print(f"Items:                    {list(d1.items())}")

d1.update({'Country': "India"})
print(f"Updated Dictionary:       {d1}")
print("-" * 30)


# -----------------------------------------------------------------------------
# 4. ARRAYS
# -----------------------------------------------------------------------------
print("\n--- 4. Array Operations ---")

# Typecode 'i' for signed integer
arr_int = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print(f"Integer Array:            {arr_int}")
print("Elements:")
for i in arr_int:
    print(i, end=" ")
print(f"\nLength:                   {len(arr_int)}")

# Typecode 'u' for Unicode character 
arr_char = array('u', ['a', 'b', 'c', 'd'])
print(f"\nCharacter Array:          {arr_char}")
print("Elements:")
for ch in arr_char:
    print(ch, end=" ")
print("\n" + "-" * 30)
