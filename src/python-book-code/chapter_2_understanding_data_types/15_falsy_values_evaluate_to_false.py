"""
Example 15 from Chapter 2: Understanding Data - Types and Operations
Python Programming Fundamentals by Rajesh Aadi

Falsy Values Evaluate To False
"""

# Falsy values (evaluate to False)
print(bool(0))          # False
print(bool(0.0))        # False
print(bool(""))         # False (empty string)
print(bool([]))         # False (empty list)
print(bool(None))       # False

# Truthy values (evaluate to True)
print(bool(1))          # True
print(bool(-1))         # True
print(bool("text"))     # True
print(bool([1, 2]))     # True

# Practical use
customer_email = ""
if customer_email:  # Checks if string is not empty
    print("Email provided")
else:
    print("No email provided")  # This will print
