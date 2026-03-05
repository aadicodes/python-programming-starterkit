"""
Example 3 from Chapter 4: Doing Things Repeatedly - Loops
Python Programming Fundamentals by Rajesh Aadi

Customer Order Entry System
"""

# Customer order entry system
print("Bookish Corner - Order Entry")
print("Enter 'done' when finished\n")

total_books = 0
order_count = 0

while True:
    response = input("Enter quantity (or 'done'): ")

    if response.lower() == 'done':
        break  # Exit the loop

    if response.isdigit():
        quantity = int(response)
        total_books += quantity
        order_count += 1
        print(f"Added {quantity} books to order #{order_count}")
    else:
        print("Invalid input. Please enter a number.")

print(f"\nOrder complete! Total: {total_books} books across {order_count} items")
