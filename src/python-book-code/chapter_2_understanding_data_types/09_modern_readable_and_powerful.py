"""
Example 9 from Chapter 2: Understanding Data - Types and Operations
Python Programming Fundamentals by Rajesh Aadi

Modern Readable And Powerful
"""

# Modern, readable, and powerful
message = f"Dear {customer_name}, your total is ${total_amount}"
print(message)

# Can include expressions
quantity = 5
price = 29.99
print(f"Total: ${quantity * price}")  # Total: $149.95

# Format numbers
print(f"Total: ${quantity * price:.2f}")  # Total: $149.95 (2 decimals)
