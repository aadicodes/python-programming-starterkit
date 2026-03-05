"""
Example 14 from Chapter 2: Understanding Data - Types and Operations
Python Programming Fundamentals by Rajesh Aadi

And Operator Both Conditions M
"""

# AND operator - both conditions must be True
order_total = 150
is_member = True

free_shipping = (order_total >= 100) and is_member
print(free_shipping)  # True

# OR operator - at least one condition must be True
has_discount_code = False
is_premium_customer = True

gets_discount = has_discount_code or is_premium_customer
print(gets_discount)  # True

# NOT operator - inverts the boolean value
is_guest = not is_member
print(is_guest)  # False

# Combining logical operators
order_total = 75
is_member = True
has_coupon = True

eligible = (order_total >= 100 or is_member) and has_coupon
print(eligible)  # True

# Use parentheses for clarity
eligible = ((order_total >= 100) or is_member) and has_coupon
