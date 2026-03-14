"""
Example 9 from Chapter 9: Preserving Data - File Operations
Python Programming Fundamentals by Rajesh Aadi

Python Dictionary
"""

import json

# Python dictionary
customer = {
    "name": "Alice Johnson",
    "email": "alice@email.com",
    "member_type": "premium",
    "points": 1250,
    "orders": [
        {"id": 1001, "total": 89.99, "date": "2026-01-15"},
        {"id": 1002, "total": 124.50, "date": "2026-02-01"}
    ],
    "address": {
        "street": "123 Main St",
        "city": "Boston",
        "state": "MA"
    }
}

# Write to JSON file
with open("customer.json", "w") as file:
    json.dump(customer, file, indent=4)  # indent makes it readable

# Convert to JSON string
json_string = json.dumps(customer, indent=2)
print(json_string)
