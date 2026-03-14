"""
Example 10 from Chapter 9: Preserving Data - File Operations
Python Programming Fundamentals by Rajesh Aadi

Read From Json File
"""

import json

# Read from JSON file
with open("customer.json", "r") as file:
    customer = json.load(file)

print(customer["name"])
print(customer["points"])
print(customer["orders"][0]["total"])

# Parse JSON string
json_string = '{"name": "Alice", "points": 1250}'
data = json.loads(json_string)
print(data["name"])
