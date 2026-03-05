"""
Example 3 from Chapter 6: Managing Collections - Lists and Tuples
Python Programming Fundamentals by Rajesh Aadi

Access By Index
"""

book_titles = ["Python", "JavaScript", "Java", "C++", "Ruby"]

# Access by index
print(book_titles[0])   # Python (first item)
print(book_titles[1])   # JavaScript (second item)
print(book_titles[4])   # Ruby (fifth item)

# Negative indexing (from the end)
print(book_titles[-1])  # Ruby (last item)
print(book_titles[-2])  # C++ (second to last)

# Index out of range causes error
# print(book_titles[10])  # IndexError!
