"""
Example 1 from Chapter 11: Building Systems - Object-Oriented Programming
Python Programming Fundamentals by Rajesh Aadi

Customer Data
"""

# Customer data
customer_name = "Alice"
customer_email = "alice@email.com"
customer_points = 1250

# Customer functions
def add_points(points, amount):
    return points + amount

def send_email(email, message):
    print(f"Sending to {email}: {message}")

# Everything is disconnected!
