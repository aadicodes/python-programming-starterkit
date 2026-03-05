"""
Example 1 from Chapter 5: Organizing Code - Functions
Python Programming Fundamentals by Rajesh Aadi

Define The Function
"""

# Define the function
def calculate_tax(amount):
    tax_rate = 0.08
    tax = amount * tax_rate
    return tax

# Use the function
order_total = 100.00
tax_amount = calculate_tax(order_total)
print(f"Tax on ${order_total:.2f} is ${tax_amount:.2f}")
