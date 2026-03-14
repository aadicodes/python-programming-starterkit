"""
Example 12 from Chapter 10: Handling Problems - Error Handling and Exceptions
Python Programming Fundamentals by Rajesh Aadi

Set Discount
"""

def set_discount(amount):
    """Set discount with validation"""
    if amount < 0:
        raise ValueError("Discount cannot be negative")

    if amount > 100:
        raise ValueError("Discount cannot exceed 100%")

    return amount

# Usage
try:
    discount = set_discount(-10)
except ValueError as e:
    print(f"Invalid discount: {e}")
