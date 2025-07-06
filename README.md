# 📚 Student Management & Palindrome Checker System

This repository contains two Python programs:

1. **Student Management System** – Collects student data, calculates average grades, and displays results.
2. **Palindrome Checker** – Checks if a given string is a palindrome (case-insensitive, ignoring spaces).

These scripts are contains
- Input/output
- String and list manipulation
- Functions and modular code
- Conditional statements
- Dictionaries and loops in Python.

## ✨ Features

- Modular functions (`input`, `process`, `display`) where applicable
- User interaction via `input()`
- Clean console output
- Easy to modify and expand

---

## 1. Student Management System

### 🧠 Description

Collects student details including name, age, and course marks. Calculates average grade and prints structured output.

### 📦 Functions

| Function | Purpose |
|---------|---------|
| `input_student_data()` | Gathers student info from user |
| `calculate_average(marks)` | Computes average of course marks |
| `display_student_data(student_data)` | Displays formatted student data |
| `student_management()` | Main function to run the system |

###  Codes
```python
def input_student_data():
    name = input("Enter student name: ")
    age = int(input(f"Enter age for {name}: "))
    marks = []
    num_courses = int(input(f"How many courses for {name} (2 or 3)? "))
    for i in range(num_courses):
        mark = float(input(f"Enter mark for course {i+1}: "))
        marks.append(mark)
    return name, age, marks

def calculate_average(marks):
    return sum(marks) / len(marks)

def display_student_data(student_data):
    print("\n--- Student Grades ---")
    for name, info in student_data.items():
        print(f"Student: {name}")
        print(f"  Age: {info['age']}")
        print(f"  Marks: {info['marks']}")
        print(f"  Average Grade: {info['average']:.2f}")
        print("-" * 30)

def student_management():
    student_data = {}
    num_students = int(input("Enter the number of students: "))
    for _ in range(num_students):
        name, age, marks = input_student_data()
        avg = calculate_average(marks)
        student_data[name] = {
            'age': age,
            'marks': marks,
            'average': avg
        }
    display_student_data(student_data)
```

### Sample Output
```
Enter the number of students: 1
Enter student name: Sam
Enter age for Sam: 20
How many courses for Sam (2 or 3)? 3
Enter mark for course 1: 75
Enter mark for course 2: 80
Enter mark for course 3: 85

--- Student Grades ---
Student: Sam
  Age: 20
  Marks: [75.0, 80.0, 85.0]
  Average Grade: 80.00
-------------------------------
```
## 2. Palindrome Checker

### 🧠 Description

Checks if a user-entered string is a palindrome by removing spaces and ignoring case sensitivity.

### 📦 Function

| Function | Purpose |
|---------|---------|
| `check_palindrome()` | Prompts for a string and checks palindrome status |

###  Codes
```python
def check_palindrome():
    user_input = input("Enter a string to check if it's a palindrome: ")
    cleaned_input = user_input.replace(" ", "").lower()
    if cleaned_input == cleaned_input[::-1]:
        print("Yes, it is a palindrome.")
    else:
        print("No, it is not a palindrome.")
check_palindrome()
```
### Sample Output

```
1. Enter a string to check if it's a palindrome: Nurses run
Yes, it is a palindrome.
2.Enter a string to check if it's a palindrome: Hello
No, it is not a palindrome.
```

### Tean Members

| Student ID | Names |
|---------|---------|
| 26851 | Samillah Mutoni |
| 24768 | Ndacyayisenga Herve |
| 26627 | Ruhanika Alex |
| 26509 | Munezero Eugene |
| 25915 | Shema Hubert |
| 26240 | Nziza Benjamin |


