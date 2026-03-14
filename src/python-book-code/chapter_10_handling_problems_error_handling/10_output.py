"""
Example 10 from Chapter 10: Handling Problems - Error Handling and Exceptions
Python Programming Fundamentals by Rajesh Aadi

Output
"""

try:
    value = int("abc")
except ValueError as error:
    print(f"Error type: {type(error).__name__}")
    print(f"Error message: {str(error)}")
    print(f"Error details: {repr(error)}")

# Output:
# Error type: ValueError
# Error message: invalid literal for int() with base 10: 'abc'
# Error details: ValueError("invalid literal for int() with base 10: 'abc'")
