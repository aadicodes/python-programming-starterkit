"""
Example 12 from Chapter 11: Building Systems - Object-Oriented Programming
Python Programming Fundamentals by Rajesh Aadi

Person
"""

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"Hi, I'm {self.name}"

class Customer(Person):
    def __init__(self, name, points):
        super().__init__(name)
        self.points = points

    def introduce(self):
        """Override parent method"""
        return f"Hi, I'm {self.name}, a customer with {self.points} points"

class Employee(Person):
    def __init__(self, name, title):
        super().__init__(name)
        self.title = title

    def introduce(self):
        """Override parent method"""
        return f"Hi, I'm {self.name}, {self.title}"

# Usage
person = Person("Charlie")
customer = Customer("Alice", 1250)
employee = Employee("Bob", "Sales Manager")

print(person.introduce())    # Hi, I'm Charlie
print(customer.introduce())  # Hi, I'm Alice, a customer with 1250 points
print(employee.introduce())  # Hi, I'm Bob, Sales Manager
