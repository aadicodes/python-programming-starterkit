"""
Example 17 from Chapter 8: Working with Text - String Manipulation
Python Programming Fundamentals by Rajesh Aadi

Simple Search
"""

import re

# Simple search
text = "Call us at 555-123-4567 or 555-987-6543"

# Find all phone numbers
pattern = r"\d{3}-\d{3}-\d{4}"
phones = re.findall(pattern, text)
print(phones)  # ['555-123-4567', '555-987-6543']

# Check if string matches pattern
email = "alice@email.com"
pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
if re.match(pattern, email):
    print("Valid email format")

# Replace using regex
text = "Order #12345 and order #67890"
pattern = r"#(\d+)"
result = re.sub(pattern, r"Order Number: \1", text)
print(result)  # Order Order Number: 12345 and order Order Number: 67890

# Extract information
text = "Price: $29.99, Quantity: 5"
pattern = r"Price: \$(\d+\.\d{2}), Quantity: (\d+)"
match = re.search(pattern, text)
if match:
    price = match.group(1)
    quantity = match.group(2)
    print(f"Price: ${price}, Qty: {quantity}")
