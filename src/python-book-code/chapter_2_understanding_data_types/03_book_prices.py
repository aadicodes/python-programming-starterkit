"""
Example 3 from Chapter 2: Understanding Data - Types and Operations
Python Programming Fundamentals by Rajesh Aadi

Book Prices
"""

# Book prices
python_book_price = 29.99
javascript_book_price = 34.50
java_book_price = 39.99

# Calculating subtotal
subtotal = (python_book_price * 2 +
            javascript_book_price * 1 +
            java_book_price * 3)

print("Subtotal: $", subtotal)  # 234.45

# Float division always returns float
average_price = subtotal / 6
print("Average price per book: $", average_price)  # 39.075
