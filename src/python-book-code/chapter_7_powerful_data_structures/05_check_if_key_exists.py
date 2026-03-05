"""
Example 5 from Chapter 7: Powerful Data Structures - Dictionaries and Sets
Python Programming Fundamentals by Rajesh Aadi

Check If Key Exists
"""

customer = {
    "name": "Alice Johnson",
    "email": "alice@email.com",
    "member_type": "premium"
}

# Check if key exists
if "email" in customer:
    print(f"Email: {customer['email']}")

if "phone" not in customer:
    print("No phone number on file")

# Get number of key-value pairs
print(len(customer))  # 3

# Get all keys
keys = customer.keys()
print(keys)  # dict_keys(['name', 'email', 'member_type'])

# Get all values
values = customer.values()
print(values)  # dict_values(['Alice Johnson', 'alice@email.com', 'premium'])

# Get all key-value pairs
items = customer.items()
print(items)  # dict_items([('name', 'Alice Johnson'), ...])
