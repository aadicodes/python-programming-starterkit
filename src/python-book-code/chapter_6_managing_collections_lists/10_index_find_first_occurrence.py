"""
Example 10 from Chapter 6: Managing Collections - Lists and Tuples
Python Programming Fundamentals by Rajesh Aadi

Index Find First Occurrence
"""

books = ["Python", "JavaScript", "Java", "Python", "Ruby"]

# index() - Find first occurrence
position = books.index("Python")
print(f"First Python book at index: {position}")  # 0

# Find in a range
position = books.index("Python", 1)  # Start searching from index 1
print(f"Next Python book at index: {position}")  # 3

# Handle not found with try-except (preview of Chapter 10)
try:
    position = books.index("C++")
except ValueError:
    print("C++ not found in list")
