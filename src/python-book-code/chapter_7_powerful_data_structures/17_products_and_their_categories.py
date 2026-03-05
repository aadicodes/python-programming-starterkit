"""
Example 17 from Chapter 7: Powerful Data Structures - Dictionaries and Sets
Python Programming Fundamentals by Rajesh Aadi

Products And Their Categories
"""

# Products and their categories
product_categories = {
    "Python Programming": {"Programming", "Beginner", "Popular"},
    "JavaScript Basics": {"Programming", "Beginner", "Web"},
    "Data Science": {"Programming", "Advanced", "Analytics"},
    "Business 101": {"Business", "Beginner", "Popular"}
}

# Find all unique categories
all_categories = set()
for categories in product_categories.values():
    all_categories.update(categories)

print("All categories:", all_categories)

# Find products in multiple categories
programming_books = []
for book, categories in product_categories.items():
    if "Programming" in categories and "Beginner" in categories:
        programming_books.append(book)

print("Beginner programming books:", programming_books)
