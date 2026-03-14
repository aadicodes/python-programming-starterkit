"""
Example 15 from Chapter 9: Preserving Data - File Operations
Python Programming Fundamentals by Rajesh Aadi

Text Files
"""

# TEXT FILES

# Write
with open("file.txt", "w") as f:
    f.write("Hello\n")

# Read
with open("file.txt", "r") as f:
    content = f.read()         # All at once
    # Or
    for line in f:             # Line by line
        print(line.strip())

# Append
with open("file.txt", "a") as f:
    f.write("New line\n")

# CSV FILES

import csv

# Write
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Alice", 25])

# Read
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["Name"])

# JSON FILES

import json

# Write
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

# Read
with open("data.json", "r") as f:
    data = json.load(f)

# FILE PATHS

import os

os.path.join("dir", "file.txt")  # Join paths
os.path.exists("file.txt")       # Check existence
os.makedirs("path/to/dir")       # Create directories
os.listdir("dir")                # List files
os.path.getsize("file.txt")      # File size

# ERROR HANDLING

try:
    with open("file.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"Error: {e}")
