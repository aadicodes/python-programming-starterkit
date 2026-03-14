"""
Example 3 from Chapter 10: Handling Problems - Error Handling and Exceptions
Python Programming Fundamentals by Rajesh Aadi

Without Error Handling Crashes
"""

# Without error handling - crashes
quantity = int(input("Enter quantity: "))  # Crashes if user enters 'abc'

# With error handling - recovers
try:
    quantity = int(input("Enter quantity: "))
    print(f"You ordered {quantity} items")
except ValueError:
    print("Invalid input. Please enter a number.")
    quantity = 0
