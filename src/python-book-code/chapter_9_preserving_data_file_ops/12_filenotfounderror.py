"""
Example 12 from Chapter 9: Preserving Data - File Operations
Python Programming Fundamentals by Rajesh Aadi

Filenotfounderror
"""

# FileNotFoundError
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")

# PermissionError
try:
    with open("/root/protected.txt", "w") as file:
        file.write("data")
except PermissionError:
    print("No permission to write this file")

# General exception handling
try:
    with open("data.txt", "r") as file:
        content = file.read()
        data = json.loads(content)
except FileNotFoundError:
    print("File doesn't exist, creating new one")
    data = {}
except json.JSONDecodeError:
    print("Invalid JSON format")
    data = {}
except Exception as e:
    print(f"Unexpected error: {e}")
    data = {}
