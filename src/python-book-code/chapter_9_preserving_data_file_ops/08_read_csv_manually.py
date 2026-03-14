"""
Example 8 from Chapter 9: Preserving Data - File Operations
Python Programming Fundamentals by Rajesh Aadi

Read Csv Manually
"""

import csv

# Read CSV manually
with open("customers.csv", "r") as file:
    reader = csv.reader(file)

    # Skip header
    header = next(reader)

    # Read rows
    for row in reader:
        name, email, member_type, points = row
        print(f"{name}: {points} points")

# Read as dictionaries (easier!)
with open("customers.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(f"{row['Name']}: {row['Points']} points")
