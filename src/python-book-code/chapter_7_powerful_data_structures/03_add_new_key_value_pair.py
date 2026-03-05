"""
Example 3 from Chapter 7: Powerful Data Structures - Dictionaries and Sets
Python Programming Fundamentals by Rajesh Aadi

Add New Key Value Pair
"""

customer = {
    "name": "Alice Johnson",
    "email": "alice@email.com"
}

# Add new key-value pair
customer["phone"] = "555-1234"
customer["points"] = 100

print(customer)
# {'name': 'Alice Johnson', 'email': 'alice@email.com',
#  'phone': '555-1234', 'points': 100}

# Update existing value
customer["points"] = 150
customer["email"] = "alice.j@email.com"

# Update multiple values at once
customer.update({
    "points": 200,
    "member_type": "premium",
    "address": "123 Main St"
})
