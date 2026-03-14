"""
Example 3 from Chapter 9: Preserving Data - File Operations
Python Programming Fundamentals by Rajesh Aadi

Add To Existing File Without E
"""

# Add to existing file without erasing
with open("log.txt", "a") as file:
    file.write("New entry\n")
    file.write("Another entry\n")

# Each time you run this, it adds to the file
