"""
Example 7 from Chapter 5: Organizing Code - Functions
Python Programming Fundamentals by Rajesh Aadi

Calculate Discount
"""

def calculate_discount(subtotal, customer_type, has_coupon):
    discount = 0

    if customer_type == "premium":
        discount = subtotal * 0.15
    elif customer_type == "member":
        discount = subtotal * 0.10

    if has_coupon:
        discount += subtotal * 0.05

    return discount

# Using the function
order_amount = 100.00
discount1 = calculate_discount(order_amount, "premium", False)
discount2 = calculate_discount(order_amount, "member", True)

print(f"Premium customer: ${discount1:.2f} off")
print(f"Member with coupon: ${discount2:.2f} off")
