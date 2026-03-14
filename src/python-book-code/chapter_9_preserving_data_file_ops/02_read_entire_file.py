"""
Example 2 from Chapter 9: Preserving Data - File Operations
Python Programming Fundamentals by Rajesh Aadi

Read Entire File
"""

# Read entire file
with open("message.txt", "r") as file:
    content = file.read()
    print(content)

# Read line by line
with open("message.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes the newline

# Read all lines into a list
with open("message.txt", "r") as file:
    lines = file.readlines()
    print(lines)  # ['Hello, World!\n', 'This is Bookish Corner.\n']

# Read one line at a time
with open("message.txt", "r") as file:
    first_line = file.readline()
    second_line = file.readline()
