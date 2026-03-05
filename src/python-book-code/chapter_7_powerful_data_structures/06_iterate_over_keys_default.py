"""
Example 6 from Chapter 7: Powerful Data Structures - Dictionaries and Sets
Python Programming Fundamentals by Rajesh Aadi

Iterate Over Keys Default
"""

customer = {
    "name": "Alice Johnson",
    "email": "alice@email.com",
    "points": 1250,
    "member_type": "premium"
}

# Iterate over keys (default)
for key in customer:
    print(key)

# Iterate over keys explicitly
for key in customer.keys():
    print(f"{key}: {customer[key]}")

# Iterate over values
for value in customer.values():
    print(value)

# Iterate over key-value pairs (most common)
for key, value in customer.items():
    print(f"{key}: {value}")

# Output:
# name: Alice Johnson
# email: alice@email.com
# points: 1250
# member_type: premium
