"""
Example 10 from Chapter 3: Making Decisions - Conditional Statements
Python Programming Fundamentals by Rajesh Aadi

Equivalent To
"""

in_stock = False

if not in_stock:
    print("Sorry, this item is out of stock")

# Equivalent to:
if in_stock == False:
    print("Sorry, this item is out of stock")

# NOT with other operators
is_guest = True
if not is_guest:
    print("Welcome back, member!")
