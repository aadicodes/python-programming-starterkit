"""
Example 12 from Chapter 4: Doing Things Repeatedly - Loops
Python Programming Fundamentals by Rajesh Aadi

Example 12: Accumulating values in a loop (running total)
"""

orders = [45.99, 89.50, 120.00, 67.80, 95.25]

print("Bookish Corner - Daily Revenue Calculator\n")

running_total = 0

for idx, amount in enumerate(orders, 1):
    running_total += amount
    print(f"Order #{idx} amount: ${amount:.2f}")
    print(f"  Running total: ${running_total:.2f}\n")

average_order = running_total / len(orders)

print("=" * 40)
print(f"Total Revenue: ${running_total:.2f}")
print(f"Average Order: ${average_order:.2f}")
print("=" * 40)
