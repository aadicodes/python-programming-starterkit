"""
Example 5 from Chapter 11: Building Systems - Object-Oriented Programming
Python Programming Fundamentals by Rajesh Aadi

Book
"""

class Book:
    # Class attribute - shared by all books
    tax_rate = 0.08

    def __init__(self, title, price):
        self.title = title
        self.price = price

    def price_with_tax(self):
        """Calculate price including tax"""
        return self.price * (1 + Book.tax_rate)

# All books share the same tax_rate
book1 = Book("Python", 29.99)
book2 = Book("Java", 34.99)

print(book1.price_with_tax())  # 32.39
print(book2.price_with_tax())  # 37.79

# Change tax rate for all books
Book.tax_rate = 0.10
print(book1.price_with_tax())  # 32.99
