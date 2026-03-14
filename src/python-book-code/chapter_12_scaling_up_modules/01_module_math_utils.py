"""
Example 1 from Chapter 12: Scaling Up - Modules and Packages
Python Programming Fundamentals by Rajesh Aadi

Example 01: Module Basics
"""

# This example demonstrates how modules organize code
# A module is simply a Python file with .py extension

# math_utils.py module (conceptual - demonstrates module structure)
def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# When this module is imported:
if __name__ == "__main__":
    # Test the functions
    print(add(10, 5))           # 15
    print(subtract(10, 5))      # 5
    print(multiply(10, 5))      # 50
    print(divide(10, 5))        # 2.0
