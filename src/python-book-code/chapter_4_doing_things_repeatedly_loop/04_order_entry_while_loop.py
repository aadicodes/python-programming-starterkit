"""
Example 4 from Chapter 4: Doing Things Repeatedly - Loops
Python Programming Fundamentals by Rajesh Aadi

Example 04: While loop with user input and break statement
"""

print("Bookish Corner - Order Entry")
print("Enter 'done' when finished\n")

total_books = 0
order_count = 0

while True:
    response = input("Enter quantity (or 'done'): ").strip().lower()
    
    if response == 'done':
        break
    
    try:
        quantity = int(response)
        order_count += 1
        total_books += quantity
        print(f"Added {quantity} books to order #{order_count}")
    except ValueError:
        print("Invalid input. Please enter a number or 'done'")

print(f"\nOrder complete! Total: {total_books} books across {order_count} items")
