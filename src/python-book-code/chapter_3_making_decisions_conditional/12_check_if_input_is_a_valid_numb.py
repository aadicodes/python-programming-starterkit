"""
Example 12 from Chapter 3: Making Decisions - Conditional Statements
Python Programming Fundamentals by Rajesh Aadi

Check If Input Is A Valid Numb
"""

print("Enter quantity to order:")
quantity_str = input("> ")

# Check if input is a valid number
if quantity_str.isdigit():
    quantity = int(quantity_str)

    if quantity > 0:
        print(f"Ordering {quantity} books")
    else:
        print("Quantity must be positive")
else:
    print("Invalid input. Please enter a number.")
