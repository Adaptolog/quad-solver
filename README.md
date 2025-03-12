 ---

# Quadratic Equation Solver

This is a simple console application that solves quadratic equations of the form:

```
ax^2 + bx + c = 0
```

where `a`, `b`, and `c` are real numbers, and `a ≠ 0`.

## Features
- Supports **interactive mode** (user enters coefficients manually).
- Supports **file-based mode** (coefficients are read from a file).
- Handles invalid input gracefully.
- Provides meaningful error messages.

---

## Installation and Usage

### **1. Running in Interactive Mode**
If no arguments are provided, the program runs in interactive mode.  
Run the program and input coefficients when prompted:

```sh
python main.py
```

**Example:**
```
$ python main.py
a = 2
b = 4
c = 2
Equation is: (2.0) x^2 + (4.0) x + (2.0) = 0
There are 1 roots
x1 = -1.0
```

---

### **2. Running in File-Based Mode**
Provide the path to a file containing three numbers (`a b c`) separated by spaces:

```sh
python main.py coefficients.txt
```

#### **File format example (`coefficients.txt`):**
```
1 0 0
```
_(Note: The file must end with a newline character.)_

**Example Output:**
```
$ python main.py coefficients.txt
Equation is: (1.0) x^2 + (0.0) x + (0.0) = 0
There are 1 roots
x1 = 0.0
```

---

## Error Handling
The program detects and handles the following errors:
- **Invalid input in interactive mode:**
  ```
  a = invalid
  Error. Expected a valid real number, got 'invalid' instead
  ```
- **File does not exist:**
  ```
  $ python main.py non_existing.txt
  file non_existing.txt does not exist
  ```
- **Invalid file format:**
  ```
  $ python main.py wrong_format.txt
  invalid file format
  ```
- **`a` cannot be 0 (not a quadratic equation):**
  ```
  $ python main.py zero_a.txt
  Error. a cannot be 0
  ```

---

## **Revert Commit**
A revert commit was made as part of this assignment.  
You can check the commit history to find the revert operation.

---

## **License**
This project is open-source and free to use.
