"""
Example 6 from Chapter 6: Managing Collections - Lists and Tuples
Python Programming Fundamentals by Rajesh Aadi

Append Add To End
"""

books = ["Python", "JavaScript"]

# append() - Add to end
books.append("Java")
print(books)  # ['Python', 'JavaScript', 'Java']

books.append("Ruby")
print(books)  # ['Python', 'JavaScript', 'Java', 'Ruby']

# insert() - Add at specific position
books.insert(0, "C++")  # Insert at beginning
print(books)  # ['C++', 'Python', 'JavaScript', 'Java', 'Ruby']

books.insert(2, "Go")  # Insert at index 2
print(books)  # ['C++', 'Python', 'Go', 'JavaScript', 'Java', 'Ruby']

# extend() - Add multiple items
more_books = ["PHP", "Swift"]
books.extend(more_books)
print(books)  # ['C++', 'Python', 'Go', 'JavaScript', 'Java', 'Ruby', 'PHP', 'Swift']
