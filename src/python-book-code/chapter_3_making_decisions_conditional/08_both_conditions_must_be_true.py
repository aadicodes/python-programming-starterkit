"""
Example 8 from Chapter 3: Making Decisions - Conditional Statements
Python Programming Fundamentals by Rajesh Aadi

Both Conditions Must Be True
"""

is_member = True
order_total = 120
has_coupon = True

# Both conditions must be True
if is_member and order_total >= 100:
    print("Eligible for premium discount!")

# Multiple AND conditions
if is_member and order_total >= 100 and has_coupon:
    print("Maximum discount applied!")
