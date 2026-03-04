"""
Example 22 from Chapter 3: Making Decisions - Conditional Statements
Python Programming Fundamentals by Rajesh Aadi

Instead Of Deep Nesting
"""

# Instead of deep nesting
def process_order(order_total):
    if order_total <= 0:
        print("Invalid order total")
        return

    if order_total >= 100:
        print("Large order processing...")
    else:
        print("Standard order processing...")
