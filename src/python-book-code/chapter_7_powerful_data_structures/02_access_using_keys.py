"""
Example 2 from Chapter 7: Powerful Data Structures - Dictionaries and Sets
Python Programming Fundamentals by Rajesh Aadi

Access Using Keys
"""

customer = {
    "name": "Alice Johnson",
    "email": "alice@email.com",
    "member_type": "premium"
}

# Access using keys
print(customer["name"])          # Alice Johnson
print(customer["email"])         # alice@email.com

# Safer access with get() - returns None if key doesn't exist
print(customer.get("name"))      # Alice Johnson
print(customer.get("phone"))     # None (no error!)

# get() with default value
phone = customer.get("phone", "Not provided")
print(phone)  # Not provided
