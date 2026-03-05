"""
Example 12 from Chapter 6: Managing Collections - Lists and Tuples
Python Programming Fundamentals by Rajesh Aadi

Syntax Liststartstopstep
"""

books = ["Python", "JavaScript", "Java", "Ruby", "Go", "PHP", "Swift"]

# Syntax: list[start:stop:step]

# Every other item
every_other = books[::2]
print(every_other)  # ['Python', 'Java', 'Go', 'Swift']

# Every other item starting from index 1
every_other_from_1 = books[1::2]
print(every_other_from_1)  # ['JavaScript', 'Ruby', 'PHP']

# Reverse a list
reversed_books = books[::-1]
print(reversed_books)  # ['Swift', 'PHP', 'Go', 'Ruby', 'Java', 'JavaScript', 'Python']

# Copy a list
books_copy = books[:]
print(books_copy)  # ['Python', 'JavaScript', 'Java', 'Ruby', 'Go', 'PHP', 'Swift']
