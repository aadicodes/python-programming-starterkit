"""
Example 11 from Chapter 5: Organizing Code - Functions
Python Programming Fundamentals by Rajesh Aadi

Process Order
"""

def process_order(quantity, stock_available):
    # Validate input
    if quantity <= 0:
        return "Error: Quantity must be positive"

    if quantity > stock_available:
        return "Error: Insufficient stock"

    # Process order
    return f"Success: {quantity} items ordered"

result1 = process_order(5, 10)
result2 = process_order(-1, 10)
result3 = process_order(20, 10)

print(result1)
print(result2)
print(result3)
