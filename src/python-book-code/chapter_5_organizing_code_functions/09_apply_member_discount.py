"""
Example 9 from Chapter 5: Organizing Code - Functions
Python Programming Fundamentals by Rajesh Aadi

Apply Member Discount
"""

def apply_member_discount(amount):
    discount = amount * 0.10
    discounted_price = amount - discount
    return discounted_price

original = 100.00
final = apply_member_discount(original)
print(f"Original: ${original:.2f}, Final: ${final:.2f}")
