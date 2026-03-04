"""
Example 4 from Chapter 3: Making Decisions - Conditional Statements
Python Programming Fundamentals by Rajesh Aadi

Example 04
"""

customer_type = "premium"
subtotal = 100.00
discount = 0

if customer_type == "regular":
    discount = 0
    print("No discount applied")
elif customer_type == "member":
    discount = subtotal * 0.10
    print("Member discount: 10%")
elif customer_type == "premium":
    discount = subtotal * 0.15
    print("Premium discount: 15%")
else:
    print("Unknown customer type")
    discount = 0

total = subtotal - discount
print(f"Discount amount: ${discount:.2f}")
print(f"Total after discount: ${total:.2f}")
