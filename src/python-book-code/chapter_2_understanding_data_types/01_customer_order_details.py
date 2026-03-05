"""
Example 1 from Chapter 2: Understanding Data - Types and Operations
Python Programming Fundamentals by Rajesh Aadi

Customer Order Details
"""

# Customer order details
python_book_qty = 2
javascript_book_qty = 1
java_book_qty = 3

# Total books ordered
total_books = python_book_qty + javascript_book_qty + java_book_qty
print("Total books in order:", total_books)  # 6

# Integer division (for packaging)
books_per_box = 4
boxes_needed = total_books // books_per_box  # Floor division
print("Boxes needed:", boxes_needed)  # 1

# Remainder (for partial boxes)
books_in_partial_box = total_books % books_per_box  # Modulo
print("Books in partial box:", books_in_partial_box)  # 2
