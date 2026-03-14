"""
Example 3 from Chapter 11: Building Systems - Object-Oriented Programming
Python Programming Fundamentals by Rajesh Aadi

Book
"""

class Book:
    """Represents a book"""

    def __init__(self, title, price, stock):
        """Initialize book with title, price, and stock"""
        self.title = title
        self.price = price
        self.stock = stock

# Create books
book1 = Book("Python Programming", 29.99, 25)
book2 = Book("JavaScript Basics", 24.99, 15)

# Each has its own attributes
print(book1.title)  # Python Programming
print(book2.title)  # JavaScript Basics
print(book1.price)  # 29.99
print(book2.price)  # 24.99
