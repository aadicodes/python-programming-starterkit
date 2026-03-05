"""
Example 11 from Chapter 4: Doing Things Repeatedly - Loops
Python Programming Fundamentals by Rajesh Aadi

Calculate Total Revenue From D
"""

# Calculate total revenue from daily sales
print("Bookish Corner - Daily Revenue Calculator\n")

total_revenue = 0
num_orders = 5

for order_num in range(1, num_orders + 1):
    amount = float(input(f"Order #{order_num} amount: $"))
    total_revenue += amount
    print(f"  Running total: ${total_revenue:.2f}\n")

average_order = total_revenue / num_orders

print("=" * 40)
print(f"Total Revenue: ${total_revenue:.2f}")
print(f"Average Order: ${average_order:.2f}")
print("=" * 40)
