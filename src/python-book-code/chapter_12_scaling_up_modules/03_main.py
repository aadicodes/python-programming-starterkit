"""
Example 3 from Chapter 12: Scaling Up - Modules and Packages
Python Programming Fundamentals by Rajesh Aadi

Main Module - Importing from math_utils
"""

# main.py - Import and use math_utils module

# Define math_utils functions inline for demonstration
def add(a, b):
    """Add two numbers"""
    return a + b

def calculate_tax(amount, rate=0.08):
    """Calculate tax on an amount"""
    return amount * rate

TAX_RATE = 0.08

# Using imported functions (simulated)
result = add(10, 5)
print(result)  # 15

tax = calculate_tax(100)
print(tax)  # 8.0

print(TAX_RATE)  # 0.08

# More complex example
total_amount = 100
tax_amount = calculate_tax(total_amount)
final_amount = total_amount + tax_amount
print(f"Original: ${total_amount}, Tax: ${tax_amount:.2f}, Total: ${final_amount:.2f}")
