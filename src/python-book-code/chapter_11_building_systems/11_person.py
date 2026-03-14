"""
Example 11 from Chapter 11: Building Systems - Object-Oriented Programming
Python Programming Fundamentals by Rajesh Aadi

Person
"""

class Person:
    """Base class for all people"""

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def send_email(self, message):
        """Send email to person"""
        print(f"Sending to {self.email}: {message}")

class Customer(Person):
    """Customer inherits from Person"""

    def __init__(self, name, email, member_type="regular"):
        super().__init__(name, email)  # Call parent constructor
        self.member_type = member_type
        self.points = 0
        self.orders = []

    def add_points(self, amount):
        """Add loyalty points"""
        self.points += amount

    def place_order(self, order):
        """Place an order"""
        self.orders.append(order)

class Employee(Person):
    """Employee inherits from Person"""

    def __init__(self, name, email, employee_id, department):
        super().__init__(name, email)
        self.employee_id = employee_id
        self.department = department
        self.salary = 0

    def assign_to_department(self, department):
        """Assign to new department"""
        self.department = department

# Usage
customer = Customer("Alice Johnson", "alice@email.com", "premium")
customer.send_email("Welcome!")  # Inherited method
customer.add_points(100)         # Customer method

employee = Employee("Bob Smith", "bob@company.com", "E001", "Sales")
employee.send_email("Meeting at 2pm")  # Inherited method
employee.assign_to_department("Marketing")  # Employee method
