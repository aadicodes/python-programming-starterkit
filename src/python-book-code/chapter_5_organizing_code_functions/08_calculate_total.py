"""
Example 8 from Chapter 5: Organizing Code - Functions
Python Programming Fundamentals by Rajesh Aadi

Calculate Total
"""

def calculate_total(subtotal, tax_rate=0.08, shipping=0):
    tax = subtotal * tax_rate
    total = subtotal + tax + shipping
    return total

# Different ways to call it
total1 = calculate_total(100)                    # Uses defaults
total2 = calculate_total(100, 0.10)              # Custom tax rate
total3 = calculate_total(100, 0.08, 8.99)        # All parameters
total4 = calculate_total(100, shipping=8.99)     # Named parameter

print(f"Default: ${total1:.2f}")
print(f"10% tax: ${total2:.2f}")
print(f"With shipping: ${total3:.2f}")
print(f"Named param: ${total4:.2f}")
