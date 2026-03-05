"""
Example 14 from Chapter 5: Organizing Code - Functions
Python Programming Fundamentals by Rajesh Aadi

Global Counter
"""

# Global counter
orders_processed = 0

def process_order():
    global orders_processed  # Declare we're modifying global
    orders_processed += 1
    print(f"Order processed. Total: {orders_processed}")

process_order()
process_order()
process_order()
