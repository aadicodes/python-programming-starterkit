"""
Example 7 from Chapter 10: Handling Problems - Error Handling and Exceptions
Python Programming Fundamentals by Rajesh Aadi

Example 07
"""

try:
    price = float(input("Enter price: $"))
except ValueError:
    print("Invalid price")
else:
    # Only runs if no exception
    print(f"Price accepted: ${price:.2f}")
    tax = price * 0.08
    print(f"Tax: ${tax:.2f}")
