"""
Example 1 from Chapter 9: Preserving Data - File Operations
Python Programming Fundamentals by Rajesh Aadi

Example 01
"""

# Write to a file (creates new or overwrites existing)
with open("message.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is Bookish Corner.\n")

# File is automatically closed after the 'with' block
