"""
Example 8 from Chapter 2: Understanding Data - Types and Operations
Python Programming Fundamentals by Rajesh Aadi

Named Placeholders
"""

message = "Dear {}, your total is ${}".format(customer_name, total_amount)
print(message)

# Named placeholders
message = "Dear {name}, your total is ${amount}".format(
    name=customer_name,
    amount=total_amount
)
