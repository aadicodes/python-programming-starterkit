"""
Example 7 from Chapter 6: Managing Collections - Lists and Tuples
Python Programming Fundamentals by Rajesh Aadi

Remove Remove By Value
"""

books = ["Python", "JavaScript", "Java", "Ruby", "Go"]

# remove() - Remove by value
books.remove("Java")
print(books)  # ['Python', 'JavaScript', 'Ruby', 'Go']

# pop() - Remove and return last item
last = books.pop()
print(last)   # Go
print(books)  # ['Python', 'JavaScript', 'Ruby']

# pop(index) - Remove and return item at index
second = books.pop(1)
print(second)  # JavaScript
print(books)   # ['Python', 'Ruby']

# del - Delete by index
del books[0]
print(books)  # ['Ruby']

# clear() - Remove all items
books.clear()
print(books)  # []
