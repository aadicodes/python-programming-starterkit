"""
Example 19 from Chapter 5: Organizing Code - Functions
Python Programming Fundamentals by Rajesh Aadi

Apply Operation
"""

def apply_operation(amount, operation):
    """Apply a given operation function to an amount"""
    return operation(amount)

def add_tax(amount):
    return amount * 1.08

def add_shipping(amount):
    return amount + 8.99

# Pass functions as arguments
total1 = apply_operation(100, add_tax)
total2 = apply_operation(100, add_shipping)

print(f"With tax: ${total1:.2f}")
print(f"With shipping: ${total2:.2f}")
