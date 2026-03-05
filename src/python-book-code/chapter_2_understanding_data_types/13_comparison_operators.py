"""
Example 13 from Chapter 2: Understanding Data - Types and Operations
Python Programming Fundamentals by Rajesh Aadi

Comparison Operators
"""

order_total = 150
minimum_for_free_shipping = 100

# Comparison operators
print(order_total > minimum_for_free_shipping)   # True (greater than)
print(order_total < minimum_for_free_shipping)   # False (less than)
print(order_total >= 150)                        # True (greater or equal)
print(order_total <= 150)                        # True (less or equal)
print(order_total == 150)                        # True (equal to)
print(order_total != 150)                        # False (not equal to)

# String comparisons
customer_name = "Alice"
print(customer_name == "Alice")   # True
print(customer_name == "alice")   # False (case-sensitive!)

# Using lower() for case-insensitive comparison
user_input = "ALICE"
print(user_input.lower() == "alice")  # True
