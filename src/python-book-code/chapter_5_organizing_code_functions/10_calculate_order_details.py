"""
Example 10 from Chapter 5: Organizing Code - Functions
Python Programming Fundamentals by Rajesh Aadi

Calculate Order Details
"""

def calculate_order_details(subtotal, is_member):
    # Calculate discount
    discount = subtotal * 0.10 if is_member else 0

    # Calculate tax
    tax_rate = 0.08
    amount_after_discount = subtotal - discount
    tax = amount_after_discount * tax_rate

    # Calculate total
    total = amount_after_discount + tax

    # Return multiple values as a tuple
    return discount, tax, total

# Unpack the returned values
discount_amt, tax_amt, total_amt = calculate_order_details(100, True)

print(f"Discount: ${discount_amt:.2f}")
print(f"Tax: ${tax_amt:.2f}")
print(f"Total: ${total_amt:.2f}")
