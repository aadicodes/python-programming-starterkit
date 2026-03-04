"""
Example 15 from Chapter 3: Making Decisions - Conditional Statements
Python Programming Fundamentals by Rajesh Aadi

Traditional If Else
"""

# Traditional if-else
order_total = 80
if order_total >= 75:
    shipping = 0
else:
    shipping = 8.99

# Ternary operator (one line)
shipping = 0 if order_total >= 75 else 8.99

# More examples
status = "Member" if is_member else "Guest"
discount = 0.10 if order_total >= 100 else 0.05
message = "In stock" if quantity > 0 else "Out of stock"
