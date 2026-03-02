"""
Example 6 from Chapter 1: The Beginning - Variables and Your First Program
Python Programming Fundamentals by Rajesh Aadi

Exercise 3: Inventory Update & Exercise 4: Multi-Book Store
"""

# Exercise 3: Inventory Update
print("=== Exercise 3: Inventory Update ===")
books_in_stock = 50
books_sold = 12
books_received = 30

new_inventory = books_in_stock - books_sold + books_received
print(f"Starting inventory: {books_in_stock}")
print(f"Books sold: {books_sold}")
print(f"Books received: {books_received}")
print(f"New inventory level: {new_inventory}")

print()

# Exercise 4: Multi-Book Store
print("=== Exercise 4: Multi-Book Store ===")
book1_title = "Python Basics"
book1_qty = 25

book2_title = "Data Science 101"
book2_qty = 18

book3_title = "Web Development"
book3_qty = 32

total_books = book1_qty + book2_qty + book3_qty

print(f"  {book1_title}: {book1_qty} copies")
print(f"  {book2_title}: {book2_qty} copies")
print(f"  {book3_title}: {book3_qty} copies")
print(f"  Total books in store: {total_books}")
