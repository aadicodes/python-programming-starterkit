"""
Example 5 from Chapter 3: Making Decisions - Conditional Statements
Python Programming Fundamentals by Rajesh Aadi

Example 05: Compound Conditional - Multiple conditions with AND operator
"""

customer_type = "premium"
order_amount = 100.00

if customer_type == "premium" and order_amount > 0:
    discount_rate = 0.15
    discount_amount = order_amount * discount_rate
    total = order_amount - discount_amount
    
    print(f"Premium discount: {discount_rate * 100}%")
    print(f"Discount amount: ${discount_amount:.2f}")
    print(f"Total after discount: ${total:.2f}")
