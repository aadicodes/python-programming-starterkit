"""
Example 5 from Chapter 9: Preserving Data - File Operations
Python Programming Fundamentals by Rajesh Aadi

Get Current Directory
"""

import os

# Get current directory
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

# Join paths (works on all operating systems)
file_path = os.path.join("data", "customers", "alice.txt")
print(file_path)  # data/customers/alice.txt (or data\customers\alice.txt on Windows)

# Check if file exists
if os.path.exists("data.txt"):
    print("File exists")

# Check if it's a file or directory
if os.path.isfile("data.txt"):
    print("It's a file")

if os.path.isdir("data"):
    print("It's a directory")

# Get file size
size = os.path.getsize("data.txt")
print(f"Size: {size} bytes")

# Split path into directory and filename
directory, filename = os.path.split("/path/to/file.txt")
print(f"Directory: {directory}, File: {filename}")

# Get file extension
name, extension = os.path.splitext("document.txt")
print(f"Name: {name}, Extension: {extension}")
