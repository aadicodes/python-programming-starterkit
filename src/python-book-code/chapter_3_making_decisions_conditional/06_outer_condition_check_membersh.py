"""
Example 6 from Chapter 3: Making Decisions - Conditional Statements
Python Programming Fundamentals by Rajesh Aadi

Outer Condition Check Membersh
"""

is_member = True
order_total = 120.00
discount_rate = 0

# Outer condition: Check membership
if is_member:
    print("Member verified")

    # Inner condition: Check order amount
    if order_total >= 100:
        discount_rate = 0.15
        print("Large order bonus: 15% discount")
    else:
        discount_rate = 0.10
        print("Standard member discount: 10%")
else:
    print("Regular customer")
    if order_total >= 150:
        discount_rate = 0.05
        print("Large order discount: 5%")
    else:
        discount_rate = 0
        print("No discount available")

discount = order_total * discount_rate
final_total = order_total - discount

print(f"\nOrder total: ${order_total:.2f}")
print(f"Discount: ${discount:.2f}")
print(f"Final total: ${final_total:.2f}")
