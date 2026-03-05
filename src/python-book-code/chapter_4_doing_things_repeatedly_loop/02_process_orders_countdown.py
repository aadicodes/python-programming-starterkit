"""
Example 2 from Chapter 4: Doing Things Repeatedly - Loops
Python Programming Fundamentals by Rajesh Aadi

Example 02: Using range() with countdown
"""

total_orders = 5

for order_num in range(1, total_orders + 1):
    remaining = total_orders - order_num
    print(f"Processing order {order_num}... ({remaining} remaining)")

print(f"\nAll {total_orders} orders processed!")
