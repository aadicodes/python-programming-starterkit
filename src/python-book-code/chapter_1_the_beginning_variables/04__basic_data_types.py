"""
Example 4 from Chapter 1: The Beginning - Variables and Your First Program
Python Programming Fundamentals by Rajesh Aadi
Basic Data Types
"""

# 1. Integers (Whole Numbers)
books_in_stock = 25
chapters = 12
print("=== Integers ===")
print(f"books_in_stock = {books_in_stock} (type: {type(books_in_stock).__name__})")
print(f"chapters = {chapters} (type: {type(chapters).__name__})")

# 2. Floats (Decimal Numbers)
book_price = 29.99
tax_rate = 0.08
print("\n=== Floats ===")
print(f"book_price = {book_price} (type: {type(book_price).__name__})")
print(f"tax_rate = {tax_rate} (type: {type(tax_rate).__name__})")

# 3. Strings (Text)
store_name = "Bookish Corner"
greeting = 'Welcome to our store!'
print("\n=== Strings ===")
print(f"store_name = {store_name} (type: {type(store_name).__name__})")
print(f"greeting = {greeting} (type: {type(greeting).__name__})")

# Using different types together
total = books_in_stock * book_price
print(f"\n=== Calculation ===")
print(f"{books_in_stock} books x ${book_price} = ${total:.2f}")
