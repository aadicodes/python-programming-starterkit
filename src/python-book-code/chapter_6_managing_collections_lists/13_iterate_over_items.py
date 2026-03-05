"""
Example 13 from Chapter 6: Managing Collections - Lists and Tuples
Python Programming Fundamentals by Rajesh Aadi

Iterate Over Items
"""

books = ["Python Programming", "JavaScript Basics", "Data Science"]

# Iterate over items
for book in books:
    print(f"- {book}")

# Iterate with index using enumerate()
for index, book in enumerate(books):
    print(f"{index + 1}. {book}")

# Output:
# 1. Python Programming
# 2. JavaScript Basics
# 3. Data Science

# Iterate with index using range()
for i in range(len(books)):
    print(f"Book at index {i}: {books[i]}")
