"""
Example 16 from Chapter 6: Managing Collections - Lists and Tuples
Python Programming Fundamentals by Rajesh Aadi

Sort By Specific Criteria Usin
"""

# Sort by specific criteria using key parameter
books = [
    {"title": "Python Programming", "price": 29.99},
    {"title": "JavaScript Basics", "price": 19.99},
    {"title": "Data Science", "price": 39.99}
]

# Sort by price
books.sort(key=lambda book: book["price"])
for book in books:
    print(f"{book['title']}: ${book['price']}")

# Sort by title
books.sort(key=lambda book: book["title"])
for book in books:
    print(f"{book['title']}: ${book['price']}")
