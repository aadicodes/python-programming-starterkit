"""
Example 8 from Chapter 7: Powerful Data Structures - Dictionaries and Sets
Python Programming Fundamentals by Rajesh Aadi

Getkey Default Safe Access
"""

customer = {"name": "Alice", "email": "alice@email.com", "points": 100}

# get(key, default) - Safe access
email = customer.get("email", "unknown")

# setdefault(key, default) - Get or set if missing
phone = customer.setdefault("phone", "Not provided")
# Now customer has 'phone': 'Not provided'

# update(dict) - Merge dictionaries
customer.update({"points": 150, "status": "active"})

# pop(key, default) - Remove and return
points = customer.pop("points", 0)

# popitem() - Remove and return arbitrary item
key, value = customer.popitem()

# clear() - Remove all items
customer.clear()

# copy() - Shallow copy
customer_copy = customer.copy()

# keys(), values(), items() - Get views
keys = customer.keys()
values = customer.values()
items = customer.items()

# fromkeys(keys, value) - Create dict from keys
defaults = dict.fromkeys(["name", "email", "phone"], "Unknown")
# {'name': 'Unknown', 'email': 'Unknown', 'phone': 'Unknown'}
