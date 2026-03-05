"""
Example 4 from Chapter 6: Managing Collections - Lists and Tuples
Python Programming Fundamentals by Rajesh Aadi

Get Number Of Items
"""

book_titles = ["Python", "JavaScript", "Java"]

# Get number of items
count = len(book_titles)
print(f"We have {count} books")  # We have 3 books

# Access last item safely
if len(book_titles) > 0:
    last_book = book_titles[len(book_titles) - 1]
    # Or use: last_book = book_titles[-1]
    print(f"Last book: {last_book}")
