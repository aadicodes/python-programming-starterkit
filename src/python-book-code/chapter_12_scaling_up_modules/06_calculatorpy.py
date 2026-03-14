"""
Example 6 from Chapter 12: Scaling Up - Modules and Packages
Python Programming Fundamentals by Rajesh Aadi

Calculatorpy
"""

# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# This only runs when file is executed directly
if __name__ == "__main__":
    print("Calculator module test")
    print(f"10 + 5 = {add(10, 5)}")
    print(f"10 - 5 = {subtract(10, 5)}")
