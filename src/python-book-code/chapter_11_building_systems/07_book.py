"""
Example 7 from Chapter 11: Building Systems - Object-Oriented Programming
Python Programming Fundamentals by Rajesh Aadi

Book
"""

class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __eq__(self, other):
        """Check equality"""
        return self.price == other.price

    def __lt__(self, other):
        """Less than comparison"""
        return self.price < other.price

    def __le__(self, other):
        """Less than or equal"""
        return self.price <= other.price

# Usage
book1 = Book("Python", 29.99)
book2 = Book("Java", 34.99)
book3 = Book("Ruby", 29.99)

print(book1 == book3)  # True (same price)
print(book1 < book2)   # True (29.99 < 34.99)
print(book1 <= book3)  # True

# Can now sort books!
books = [book2, book1, book3]
books.sort()  # Sorts by price using __lt__
