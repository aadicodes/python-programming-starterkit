"""
Example 2 from Chapter 10: Handling Problems - Error Handling and Exceptions
Python Programming Fundamentals by Rajesh Aadi

Valueerror Invalid Value
"""

# ValueError - Invalid value
int("abc")  # ValueError: invalid literal for int()

# TypeError - Wrong type
"hello" + 5  # TypeError: can only concatenate str to str

# ZeroDivisionError - Division by zero
10 / 0  # ZeroDivisionError: division by zero

# KeyError - Dictionary key doesn't exist
d = {"name": "Alice"}
print(d["age"])  # KeyError: 'age'

# IndexError - List index out of range
lst = [1, 2, 3]
print(lst[10])  # IndexError: list index out of range

# FileNotFoundError - File doesn't exist
open("nonexistent.txt")  # FileNotFoundError

# AttributeError - Attribute doesn't exist
x = 5
x.append(10)  # AttributeError: 'int' object has no attribute 'append'
