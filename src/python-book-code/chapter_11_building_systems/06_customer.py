"""
Example 6 from Chapter 11: Building Systems - Object-Oriented Programming
Python Programming Fundamentals by Rajesh Aadi

Customer
"""

class Customer:
    def __init__(self, name, email, points=0):
        self.name = name
        self.email = email
        self.points = points

    def __str__(self):
        """User-friendly string representation"""
        return f"{self.name} ({self.points} points)"

    def __repr__(self):
        """Developer-friendly representation"""
        return f"Customer('{self.name}', '{self.email}', {self.points})"

# Usage
customer = Customer("Alice Johnson", "alice@email.com", 1250)

print(str(customer))   # Alice Johnson (1250 points)
print(repr(customer))  # Customer('Alice Johnson', 'alice@email.com', 1250)
print(customer)        # Uses __str__ - Alice Johnson (1250 points)
