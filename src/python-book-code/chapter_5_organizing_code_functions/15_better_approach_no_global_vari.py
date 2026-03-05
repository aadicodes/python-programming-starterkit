"""
Example 15 from Chapter 5: Organizing Code - Functions
Python Programming Fundamentals by Rajesh Aadi

Better Approach No Global Vari
"""

# Better approach - no global variables
def process_order(current_count):
    new_count = current_count + 1
    print(f"Order processed. Total: {new_count}")
    return new_count

orders = 0
orders = process_order(orders)
orders = process_order(orders)
orders = process_order(orders)
