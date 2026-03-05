"""
Example 13 from Chapter 5: Organizing Code - Functions
Python Programming Fundamentals by Rajesh Aadi

Global Variable
"""

# Global variable
store_name = "Bookish Corner"
tax_rate = 0.08

def calculate_with_tax(amount):
    # Can read global variables
    tax = amount * tax_rate
    return amount + tax

def print_receipt(total):
    # Can read global variables
    print(f"Store: {store_name}")
    print(f"Total: ${total:.2f}")

total = calculate_with_tax(100)
print_receipt(total)
