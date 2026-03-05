"""
Example 14 from Chapter 4: Doing Things Repeatedly - Loops
Python Programming Fundamentals by Rajesh Aadi

Process Orders Skip Invalid On
"""

# Process orders, skip invalid ones
print("Order Processing - Skipping Invalid Orders\n")

for order_id in range(1001, 1006):
    # Simulate checking order validity
    order_amount = float(input(f"Amount for order #{order_id}: $"))

    if order_amount <= 0:
        print(f"⚠️  Invalid amount. Skipping order #{order_id}\n")
        continue

    # This code only runs for valid orders
    tax = order_amount * 0.08
    total = order_amount + tax
    print(f"✓ Order #{order_id} processed: ${total:.2f}\n")

print("Order processing complete!")
