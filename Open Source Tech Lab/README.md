<!-- =========================================================================================
                                     HEADER SECTION
     ========================================================================================= -->
<div align="center">

  <!-- Title -->
  # Open Source Tech Laboratory

  <!-- Subtitle -->
  ### CSL405 · Semester IV · Computer Engineering

  <!-- Badges -->
  [![Curated by](https://img.shields.io/badge/Curated%20by-Amey%20Thakur-blue.svg)](https://github.com/Amey-Thakur)
  [![Programs](https://img.shields.io/badge/Programs-15-yellowgreen.svg)](#laboratory-experiments)
  [![Language](https://img.shields.io/badge/Language-Python-blueviolet.svg)](./)
  [![Lab Manual](https://img.shields.io/badge/Lab%20Manual-Available-brightgreen.svg)](PRACTICAL%20LAB.pdf)

  <!-- Short Description -->
  **A comprehensive collection of 15 programs across 7 experiments covering the core implementation of Python-based Open Source technologies, including OOP, GUI, and Database systems.**

  ---

  <!-- Navigation Links -->
  **[Experiment 1](#experiment-1-python-basics-3-programs)** &nbsp;·&nbsp; **[Experiment 2](#experiment-2-control-flow-3-programs)** &nbsp;·&nbsp; **[Experiment 3](#experiment-3-intro-to-oop-2-programs)** &nbsp;·&nbsp; **[Experiment 4](#experiment-4-advanced-oop-1-program)** &nbsp;·&nbsp; **[Experiment 5](#experiment-5-functional-python-2-programs)** &nbsp;·&nbsp; **[Experiment 6](#experiment-6-gui-programming-3-programs)** &nbsp;·&nbsp; **[Experiment 7](#experiment-7-database-connectivity-1-program)** &nbsp;·&nbsp; **[How to Use](#how-to-use)** &nbsp;·&nbsp; **[Learning Path](#learning-path)**

</div>

---

> [!TIP]
> **Pythonic Thinking**: Always start by understanding the problem, then write clean, readable code with meaningful variable names. Use list comprehensions, generators, and built-in functions to write efficient Python. Practice the DRY (Don't Repeat Yourself) principle and leverage Python's extensive standard library for common tasks.

> [!WARNING]
> **Environment Requirements**: Python 3.x is required for all experiments. For Experiments 6 and 7, ensure **MySQL Server** is installed and configured, along with the **mysql-connector-python** library (`pip install mysql-connector-python`).

---

<!-- =========================================================================================
                                     EXPERIMENT 1
     ========================================================================================= -->
## Experiment 1: Python Basics (3 Programs)

| # | Program | Description |
|:-:|:---|:---|
| 1 | [Basic_Datatypes_And_IO.py](Experiment-1/Basic_Datatypes_And_IO.py) | Input/Output, Casting, and basic Datatypes |
| 2 | [Data_Structures_And_String_Ops.py](Experiment-1/Data_Structures_And_String_Ops.py) | Sets, ByteArrays, and String manipulation |
| 3 | [Advanced_Data_Structures.py](Experiment-1/Advanced_Data_Structures.py) | Mixed Lists, Tuples, Dictionaries, and Arrays |

---

<!-- =========================================================================================
                                     EXPERIMENT 2
     ========================================================================================= -->
## Experiment 2: Control Flow (3 Programs)

| # | Program | Algorithm | Description |
|:---|:---|:---|:---|
| 1 | [If_Else_Logic.py](Experiment-2/If_Else_Logic.py) | Identity Check | Memory address and string comparison logic |
| 2 | [Loops_Factorial_Fibonacci.py](Experiment-2/Loops_Factorial_Fibonacci.py) | For / While | Calculating factorial and Fibonacci series |
| 3 | [Functions_Menu_Driven.py](Experiment-2/Functions_Menu_Driven.py) | Menu-driven | Modular functions for mathematical operations |

---

<!-- =========================================================================================
                                     EXPERIMENT 3
     ========================================================================================= -->
## Experiment 3: Intro to OOP (2 Programs)

| # | Program | Core Concept | Description |
|:---|:---|:---|:---|
| 1 | [Classes_and_Objects.py](Experiment-3/Classes_and_Objects.py) | Instance/Class Methods | Managing student data states |
| 2 | [Constructors_Implementation.py](Experiment-3/Constructors_Implementation.py) | `__init__` method | Initializing objects with default/custom args |

---

<!-- =========================================================================================
                                     EXPERIMENT 4
     ========================================================================================= -->
## Experiment 4: Advanced OOP (1 Program)

| # | Program | Core Concept | Description |
|:---|:---|:---|:---|
| 1 | [Inheritance_Implementation.py](Experiment-4/Inheritance_Implementation.py) | Single Inheritance | Extending parent classes and method overriding |

---

<!-- =========================================================================================
                                     EXPERIMENT 5
     ========================================================================================= -->
## Experiment 5: Functional Python (2 Programs)

| # | Program | Concepts | Description |
|:---|:---|:---|:---|
| 1 | [File_IO_Operations.py](Experiment-5/File_IO_Operations.py) | File Handling | Read, Write, and Append with Error Handling |
| 2 | [Lambda_Filter_Map_Reduce.py](Experiment-5/Lambda_Filter_Map_Reduce.py) | Higher-order Functions | Advanced functional computations |

---

<!-- =========================================================================================
                                     EXPERIMENT 6
     ========================================================================================= -->
## Experiment 6: GUI Programming (3 Programs)

| # | Program | Complexity | Focus Area |
|:---|:---|:---|:---|
| 1 | [GUI_Basic_Implementation.py](Experiment-6/GUI_Basic_Implementation.py) | Basic | Grid positioning and Entry fields |
| 2 | [GUI_Class_Implementation.py](Experiment-6/GUI_Class_Implementation.py) | Intermediate | Class-based UI encapsulation |
| 3 | [GUI_CRUD_Implementation.py](Experiment-6/GUI_CRUD_Implementation.py) | Advanced | Modern UI with Menus and ttk themes |

---

<!-- =========================================================================================
                                     EXPERIMENT 7
     ========================================================================================= -->
## Experiment 7: Database Connectivity (1 Program)

| # | Program | Technology | Description |
|:---|:---|:---|:---|
| 1 | [Database_Connectivity.py](Experiment-7/Database_Connectivity.py) | MySQL + Python | Robust CRUD system with parameterized queries |

---

<!-- =========================================================================================
                                     HOW TO USE
     ========================================================================================= -->
## How to Use

### Requirements

- **Python 3.x**
- **MySQL Server** (for Experiment 6 and 7)
- **mysql-connector-python** library:
  ```bash
  pip install mysql-connector-python
  ```

### Running Programs

1. **Navigate** to the specific experiment folder
2. **Execute** using the Python interpreter:
   ```bash
   python filename.py
   ```

> [!TIP]
> **Database Setup**: For Experiments 6 and 7, ensure you have a database named `ostldb` and a table `Student` configured with the appropriate schema (RollNo, Name, etc.) on your local MySQL server.

---

<!-- =========================================================================================
                                     LEARNING PATH
     ========================================================================================= -->
## 📖 Learning Path

This section documents the structured learning schedule followed during the academic semester to master Python and Open Source technologies.

| Dates | Focus Area | Key Topics Covered |
|:---|:---|:---|
| **December 2-3, 2019** | Python Documentation Basics | Control Flow, Functions, Data Structures, Modules, File I/O, Exceptions, OOP (Classes & Inheritance) |
| **December 4, 2019** | Data Science Foundational Basics | Pandas and NumPy basics for data manipulation |
| **December 5, 2019** | Web & API Basics | JSON data handling and Postman for API testing |
| **December 6, 2019** | Network Programming | Reading and writing emails using **SMTP** and **IMAP** protocols |
| **December 9-10, 2019** | Advanced Automation | Detecting and Replying to Threads using SMTP and IMAP |
| **December 11, 2019** | Systems Programming | Multithreading and Multiprocessing basics |

---

<!-- =========================================================================================
                                     LAB MANUAL
     ========================================================================================= -->
## Lab Manual

| # | Resource | Description |
|:-:|:---|:---|
| 1 | [PRACTICAL LAB.pdf](PRACTICAL%20LAB.pdf) | Complete laboratory manual with theory and analysis |

---

<!-- =========================================================================================
                                     FOOTER SECTION
     ========================================================================================= -->
<div align="center">

  <!-- Footer Navigation -->
  **[↑ Back to Top](#open-source-tech-laboratory)**

  **[Experiment 1](#experiment-1-python-basics-3-programs)** &nbsp;·&nbsp; **[Experiment 2](#experiment-2-control-flow-3-programs)** &nbsp;·&nbsp; **[Experiment 3](#experiment-3-intro-to-oop-2-programs)** &nbsp;·&nbsp; **[Experiment 4](#experiment-4-advanced-oop-1-program)** &nbsp;·&nbsp; **[Experiment 5](#experiment-5-functional-python-2-programs)** &nbsp;·&nbsp; **[Experiment 6](#experiment-6-gui-programming-3-programs)** &nbsp;·&nbsp; **[Experiment 7](#experiment-7-database-connectivity-1-program)** &nbsp;·&nbsp; **[How to Use](#how-to-use)** &nbsp;·&nbsp; **[Learning Path](#learning-path)**

  <br>

  **[🏠 Back to Main Repository](../)**

</div>

---

<div align="center">

  ### [Open Source Tech Lab](https://github.com/Amey-Thakur/OPEN-SOURCE-TECH-LAB)

  **CSL405 · Semester IV · Computer Engineering**

  *University of Mumbai · Curated by [Amey Thakur](https://github.com/Amey-Thakur)*

</div>
