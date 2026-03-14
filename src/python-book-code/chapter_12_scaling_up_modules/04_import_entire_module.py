"""
Example 4 from Chapter 12: Scaling Up - Modules and Packages
Python Programming Fundamentals by Rajesh Aadi

Import Entire Module - Different Import Styles
"""

# Define math_utils functions inline for demonstration
def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

# Style 1: Import entire module
# import math_utils
# result = math_utils.add(10, 5)  # 15
result = add(10, 5)
print(f"Style 1 - add(10, 5) = {result}")

# Style 2: Import specific items
# from math_utils import add, subtract
result = add(10, 5)  # No need for math_utils.
print(f"Style 2 - add(10, 5) = {result}")

# Style 3: Import with alias
# import math_utils as mu
# result = mu.add(10, 5)
result = add(10, 5)
print(f"Style 3 - add(10, 5) = {result}")

# Style 4: Import everything (NOT RECOMMENDED - creates namespace pollution)
# from math_utils import *
# result = add(10, 5)
result = add(10, 5)
print(f"Style 4 - add(10, 5) = {result}")

# Best practice examples
print("\nBest Practice Examples:")
print(f"add(15, 3) = {add(15, 3)}")
print(f"subtract(15, 3) = {subtract(15, 3)}")
print(f"multiply(15, 3) = {multiply(15, 3)}")
