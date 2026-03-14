"""
Example 2 from Chapter 12: Scaling Up - Modules and Packages
Python Programming Fundamentals by Rajesh Aadi

Math Utils Module
"""

# math_utils.py - A reusable math utility module
"""Utility functions for mathematical operations"""

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

def calculate_tax(amount, rate=0.08):
    """Calculate tax on an amount"""
    return amount * rate

# Module-level variable
TAX_RATE = 0.08

if __name__ == "__main__":
    print(f"Add: {add(10, 5)}")
    print(f"Tax: {calculate_tax(100)}")
    print(f"TAX_RATE: {TAX_RATE}")
