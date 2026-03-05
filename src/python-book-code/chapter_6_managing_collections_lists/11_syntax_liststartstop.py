"""
Example 11 from Chapter 6: Managing Collections - Lists and Tuples
Python Programming Fundamentals by Rajesh Aadi

Syntax Liststartstop
"""

books = ["Python", "JavaScript", "Java", "Ruby", "Go", "PHP", "Swift"]

# Syntax: list[start:stop]
# start is inclusive, stop is exclusive

# Get first 3 items (indices 0, 1, 2)
first_three = books[0:3]
print(first_three)  # ['Python', 'JavaScript', 'Java']

# Shorthand for starting at beginning
first_three = books[:3]
print(first_three)  # ['Python', 'JavaScript', 'Java']

# Get items from index 2 to end
from_index_2 = books[2:]
print(from_index_2)  # ['Java', 'Ruby', 'Go', 'PHP', 'Swift']

# Get middle items
middle = books[2:5]
print(middle)  # ['Java', 'Ruby', 'Go']

# Get last 3 items
last_three = books[-3:]
print(last_three)  # ['PHP', 'Swift']
