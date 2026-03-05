"""
Example 11 from Chapter 3: Making Decisions - Conditional Statements
Python Programming Fundamentals by Rajesh Aadi

Complex Condition With And And
"""

is_member = True
order_total = 85
location = "remote"

# Complex condition with AND and OR
if (is_member and order_total >= 50) or order_total >= 100:
    shipping_cost = 0
    print("Free shipping!")
else:
    shipping_cost = 12.99
    print(f"Shipping: ${shipping_cost}")

# Using NOT with AND
if is_member and not location == "remote":
    print("Eligible for same-day delivery!")
