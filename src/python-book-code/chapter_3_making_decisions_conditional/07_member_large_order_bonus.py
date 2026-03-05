"""
Example 7 from Chapter 3: Making Decisions - Conditional Statements
Python Programming Fundamentals by Rajesh Aadi

Example 07: Nested conditionals and multiple conditions
"""

is_member = True
order_total = 120.00

if is_member:
    print("Member verified")
    
    if order_total >= 100:
        discount_rate = 0.15
        print(f"Large order bonus: {discount_rate * 100}% discount")
        
        discount = order_total * discount_rate
        final_total = order_total - discount
        
        print(f"\nOrder total: ${order_total:.2f}")
        print(f"Discount: ${discount:.2f}")
        print(f"Final total: ${final_total:.2f}")
else:
    print("Please become a member to access special offers")
