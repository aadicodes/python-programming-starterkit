"""
Example 11 from Chapter 9: Preserving Data - File Operations
Python Programming Fundamentals by Rajesh Aadi

Multiple Customers
"""

import json

# Multiple customers
database = {
    "customers": [
        {
            "id": 1,
            "name": "Alice Johnson",
            "email": "alice@email.com",
            "member_type": "premium",
            "points": 1250
        },
        {
            "id": 2,
            "name": "Bob Smith",
            "email": "bob@email.com",
            "member_type": "member",
            "points": 450
        }
    ],
    "metadata": {
        "version": "1.0",
        "last_updated": "2026-02-09"
    }
}

# Save
with open("database.json", "w") as file:
    json.dump(database, file, indent=2)

# Load
with open("database.json", "r") as file:
    data = json.load(file)

# Access nested data
for customer in data["customers"]:
    print(f"{customer['name']}: {customer['points']} points")
