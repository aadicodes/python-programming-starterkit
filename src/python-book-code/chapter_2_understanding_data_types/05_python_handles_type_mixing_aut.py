"""
Example 5 from Chapter 2: Understanding Data - Types and Operations
Python Programming Fundamentals by Rajesh Aadi

Python Handles Type Mixing Aut
"""

# Python handles type mixing automatically
books = 5           # int
price = 29.99       # float
total = books * price  # Result is float: 149.95

print(type(total))     # <class 'float'>

# Integer + Float = Float
result = 10 + 5.5      # 15.5 (float)

# Integer / Integer = Float
result = 10 / 2        # 5.0 (float, not 5!)
