"""
Example 8 from Chapter 11: Building Systems - Object-Oriented Programming
Python Programming Fundamentals by Rajesh Aadi

Shoppingcart
"""

class ShoppingCart:
    def __init__(self):
        self.items = []

    def __len__(self):
        """Length of cart"""
        return len(self.items)

    def __getitem__(self, index):
        """Access by index"""
        return self.items[index]

    def __contains__(self, item):
        """Check if item in cart"""
        return item in self.items

    def add(self, item):
        """Add item to cart"""
        self.items.append(item)

# Usage
cart = ShoppingCart()
cart.add("Python Book")
cart.add("Java Book")

print(len(cart))           # 2
print(cart[0])             # Python Book
print("Python Book" in cart)  # True
