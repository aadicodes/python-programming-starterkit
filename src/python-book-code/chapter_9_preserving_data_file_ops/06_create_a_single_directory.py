"""
Example 6 from Chapter 9: Preserving Data - File Operations
Python Programming Fundamentals by Rajesh Aadi

Create A Single Directory
"""

import os

# Create a single directory
if not os.path.exists("data"):
    os.mkdir("data")

# Create nested directories
if not os.path.exists("data/customers/premium"):
    os.makedirs("data/customers/premium")

# List files in directory
files = os.listdir("data")
print(files)

# List with full paths
for filename in os.listdir("data"):
    full_path = os.path.join("data", filename)
    print(full_path)
