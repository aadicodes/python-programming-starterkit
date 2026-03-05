"""
Example 23 from Chapter 4: Doing Things Repeatedly - Loops
Python Programming Fundamentals by Rajesh Aadi

Find Specific Order
"""

# Find specific order
order_numbers = [1001, 1002, 1003, 1004, 1005]
target_order = 1003

found = False
for order_num in order_numbers:
    if order_num == target_order:
        print(f"Order {target_order} found!")
        found = True
        break

if not found:
    print(f"Order {target_order} not found.")
