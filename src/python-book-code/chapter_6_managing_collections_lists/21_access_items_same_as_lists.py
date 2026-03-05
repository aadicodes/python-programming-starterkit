"""
Example 21 from Chapter 6: Managing Collections - Lists and Tuples
Python Programming Fundamentals by Rajesh Aadi

Access Items Same As Lists
"""

book = ("Python Programming", 29.99, 25)

# Access items (same as lists)
title = book[0]
price = book[1]
stock = book[2]

# Unpack into variables
title, price, stock = book

# Length
print(len(book))  # 3

# Membership
if "Python Programming" in book:
    print("Found!")

# Iteration
for item in book:
    print(item)

# Count and index (same as lists)
numbers = (1, 2, 3, 2, 2, 4)
print(numbers.count(2))  # 3
print(numbers.index(3))  # 2
