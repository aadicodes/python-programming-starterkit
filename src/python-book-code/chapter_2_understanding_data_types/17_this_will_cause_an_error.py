"""
Example 17 from Chapter 2: Understanding Data - Types and Operations
Python Programming Fundamentals by Rajesh Aadi

This Will Cause An Error
"""

# This will cause an error:
# bad_number = int("29.99")  # ValueError!

# Correct approach:
float_number = float("29.99")  # First to float
int_number = int(float_number)  # Then to int: 29

# Or chain them:
result = int(float("29.99"))  # 29
