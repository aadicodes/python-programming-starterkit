"""
Example 12 from Chapter 5: Organizing Code - Functions
Python Programming Fundamentals by Rajesh Aadi

Calculate Price
"""

def calculate_price():
    price = 29.99  # Local variable
    tax = price * 0.08  # Local variable
    return price + tax

total = calculate_price()
print(f"Total: ${total:.2f}")
# print(price)  # Error! price doesn't exist outside the function
