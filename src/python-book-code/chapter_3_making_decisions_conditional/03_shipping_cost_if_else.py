"""
Example 3 from Chapter 3: Making Decisions - Conditional Statements
Python Programming Fundamentals by Rajesh Aadi

Example 03
"""

order_total = 45.99
shipping_cost = 0

if order_total >= 75:
    shipping_cost = 0
    print("Free shipping!")
else:
    shipping_cost = 8.99
    print(f"Shipping cost: ${shipping_cost}")

final_total = order_total + shipping_cost
print(f"Final total: ${final_total:.2f}")
