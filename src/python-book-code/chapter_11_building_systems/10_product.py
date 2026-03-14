"""
Example 10 from Chapter 11: Building Systems - Object-Oriented Programming
Python Programming Fundamentals by Rajesh Aadi

Product
"""

class Product:
    """Product with validated price"""

    def __init__(self, name, price):
        self.name = name
        self._price = 0  # Protected attribute (single underscore)
        self.price = price  # Uses setter

    @property
    def price(self):
        """Get price"""
        return self._price

    @price.setter
    def price(self, value):
        """Set price with validation"""
        if value < 0:
            raise ValueError("Price cannot be negative")
        if value > 10000:
            raise ValueError("Price seems unreasonably high")
        self._price = round(value, 2)

    @property
    def price_with_tax(self):
        """Calculated property"""
        return round(self._price * 1.08, 2)

# Usage
product = Product("Python Book", 29.99)
print(product.price)           # 29.99
print(product.price_with_tax)  # 32.39

product.price = 34.99          # Uses setter
print(product.price)           # 34.99

# Validation works
# product.price = -10  # ValueError: Price cannot be negative
