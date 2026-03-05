"""
Example 1 from Chapter 4: Doing Things Repeatedly - Loops
Python Programming Fundamentals by Rajesh Aadi

Process Orders One By One
"""

# Process orders one by one
orders_remaining = 5
orders_processed = 0

while orders_remaining > 0:
    orders_processed += 1
    orders_remaining -= 1
    print(f"Processing order {orders_processed}... ({orders_remaining} remaining)")

print(f"\nAll {orders_processed} orders processed!")
