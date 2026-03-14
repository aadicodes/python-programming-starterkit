"""
Example 4 from Chapter 11: Building Systems - Object-Oriented Programming
Python Programming Fundamentals by Rajesh Aadi

Book
"""

class Book:
    def __init__(self, title, price, stock):
        self.title = title
        self.price = price
        self.stock = stock

    def is_available(self):
        """Check if book is in stock"""
        return self.stock > 0

    def sell(self, quantity=1):
        """Sell books and update stock"""
        if quantity > self.stock:
            print(f"Only {self.stock} available")
            return False

        self.stock -= quantity
        print(f"Sold {quantity} of {self.title}")
        return True

    def restock(self, quantity):
        """Add stock"""
        self.stock += quantity
        print(f"Restocked {quantity} of {self.title}")

# Usage
book = Book("Python Programming", 29.99, 25)

print(book.is_available())  # True
book.sell(5)                # Sold 5 of Python Programming
print(book.stock)           # 20
book.restock(10)            # Restocked 10 of Python Programming
print(book.stock)           # 30
