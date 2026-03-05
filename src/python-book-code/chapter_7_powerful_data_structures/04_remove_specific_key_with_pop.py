"""
Example 4 from Chapter 7: Powerful Data Structures - Dictionaries and Sets
Python Programming Fundamentals by Rajesh Aadi

Remove Specific Key With Pop
"""

customer = {
    "name": "Alice Johnson",
    "email": "alice@email.com",
    "phone": "555-1234",
    "temp_note": "Follow up"
}

# Remove specific key with pop()
temp = customer.pop("temp_note")
print(temp)      # Follow up
print(customer)  # No longer has 'temp_note'

# Remove with default if key doesn't exist
result = customer.pop("fax", "No fax number")
print(result)  # No fax number

# Remove arbitrary item with popitem()
key, value = customer.popitem()
print(f"Removed: {key} = {value}")

# Delete with del
del customer["phone"]

# Clear all items
customer.clear()
print(customer)  # {}
