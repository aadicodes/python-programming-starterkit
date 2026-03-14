"""
Example 2 from Chapter 11: Building Systems - Object-Oriented Programming
Python Programming Fundamentals by Rajesh Aadi

Customer
"""

class Customer:
    """Represents a customer"""

    def __init__(self, name, email):
        """Initialize a new customer"""
        self.name = name
        self.email = email
        self.points = 0
        self.orders = []

    def add_points(self, amount):
        """Add loyalty points"""
        self.points += amount

    def get_info(self):
        """Get customer information"""
        return f"{self.name} ({self.email}) - {self.points} points"

# Create objects (instances)
customer1 = Customer("Alice Johnson", "alice@email.com")
customer2 = Customer("Bob Smith", "bob@email.com")

# Use methods
customer1.add_points(100)
customer2.add_points(50)

# Access attributes
print(customer1.name)       # Alice Johnson
print(customer1.points)     # 100
print(customer2.get_info()) # Bob Smith (bob@email.com) - 50 points
