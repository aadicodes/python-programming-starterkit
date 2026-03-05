"""
Example 9 from Chapter 3: Making Decisions - Conditional Statements
Python Programming Fundamentals by Rajesh Aadi

Either Condition Can Be True
"""

order_total = 80
is_member = False
is_first_time_customer = True

# Either condition can be True
if order_total >= 75 or is_member:
    print("Free shipping!")

# Checking multiple possibilities
if is_first_time_customer or order_total >= 100 or is_member:
    print("Special offer available!")
