"""
Example 4 from Chapter 10: Handling Problems - Error Handling and Exceptions
Python Programming Fundamentals by Rajesh Aadi

Program Continues Normally
"""

try:
    # Code that might raise an exception
    result = 10 / 0
    print("This won't execute")
except ZeroDivisionError:
    # This executes if ZeroDivisionError occurs
    print("Cannot divide by zero")
    result = 0

# Program continues normally
print("Program continues...")
