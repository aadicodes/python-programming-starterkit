"""
Example 20 from Chapter 2: Understanding Data - Types and Operations
Python Programming Fundamentals by Rajesh Aadi

Number Operations
"""

# Number Operations
result = 10 + 5         # Addition
result = 10 - 5         # Subtraction
result = 10 * 5         # Multiplication
result = 10 / 5         # Division (float)
result = 10 // 3        # Floor division (int)
result = 10 % 3         # Modulo (remainder)
result = 2 ** 3         # Exponent

# String Formatting
name = "Alice"
age = 25
# F-strings (preferred)
print(f"Name: {name}, Age: {age}")
print(f"Price: ${price:.2f}")  # 2 decimals

# String Methods
text = "  Hello World  "
text.upper()            # HELLO WORLD
text.lower()            # hello world
text.strip()            # Hello World (no spaces)
text.split()            # ['Hello', 'World']

# Boolean Operators
result = x > 5 and y < 10   # AND
result = x > 5 or y < 10    # OR
result = not is_member      # NOT

# Comparison
a == b                  # Equal
a != b                  # Not equal
a > b                   # Greater than
a >= b                  # Greater or equal

# Type Conversion
int("25")               # String to int
float("25.5")           # String to float
str(25)                 # Number to string
int(25.8)               # Float to int (truncates)
round(25.8)             # Round float (26)
round(25.123, 2)        # Round to 2 decimals
