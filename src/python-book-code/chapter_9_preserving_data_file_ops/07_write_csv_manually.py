"""
Example 7 from Chapter 9: Preserving Data - File Operations
Python Programming Fundamentals by Rajesh Aadi

Write Csv Manually
"""

import csv

# Write CSV manually
with open("customers.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Write header
    writer.writerow(["Name", "Email", "Member Type", "Points"])

    # Write data rows
    writer.writerow(["Alice Johnson", "alice@email.com", "premium", 1250])
    writer.writerow(["Bob Smith", "bob@email.com", "member", 450])

# Write using dictionaries
customers = [
    {"name": "Alice Johnson", "email": "alice@email.com", "points": 1250},
    {"name": "Bob Smith", "email": "bob@email.com", "points": 450}
]

with open("customers.csv", "w", newline="") as file:
    fieldnames = ["name", "email", "points"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(customers)
