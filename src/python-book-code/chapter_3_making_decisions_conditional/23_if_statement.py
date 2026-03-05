"""
Example 23 from Chapter 3: Making Decisions - Conditional Statements
Python Programming Fundamentals by Rajesh Aadi

If Statement
"""

# If Statement
if condition:
    # code block

# If-Else
if condition:
    # code if True
else:
    # code if False

# If-Elif-Else
if condition1:
    # code
elif condition2:
    # code
elif condition3:
    # code
else:
    # default code

# Logical Operators
if a > 5 and b < 10:        # Both must be True
if a > 5 or b < 10:         # At least one must be True
if not is_member:           # Inverts boolean

# Comparison Operators
a == b      # Equal
a != b      # Not equal
a > b       # Greater than
a >= b      # Greater or equal
a < b       # Less than
a <= b      # Less or equal

# Membership Testing
if item in [1, 2, 3]:       # Check if in list
if key in dictionary:       # Check if key exists
if char in "string":        # Check if in string

# Ternary Operator
result = value_if_true if condition else value_if_false

# Input Validation
if text.isdigit():          # Check if all digits
if text.isalpha():          # Check if all letters
if text.lower() in ["yes", "y"]:  # Multiple options
