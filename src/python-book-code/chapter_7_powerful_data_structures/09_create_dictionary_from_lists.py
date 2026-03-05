"""
Example 9 from Chapter 7: Powerful Data Structures - Dictionaries and Sets
Python Programming Fundamentals by Rajesh Aadi

Create Dictionary From Lists
"""

# Create dictionary from lists
titles = ["Python", "JavaScript", "Java"]
prices = [29.99, 24.99, 34.99]

catalog = {title: price for title, price in zip(titles, prices)}
print(catalog)
# {'Python': 29.99, 'JavaScript': 24.99, 'Java': 34.99}

# Transform dictionary values
prices = {"Python": 29.99, "JavaScript": 24.99, "Java": 34.99}
with_tax = {book: price * 1.08 for book, price in prices.items()}
print(with_tax)
# {'Python': 32.39, 'JavaScript': 26.99, 'Java': 37.79}

# Filter dictionary
expensive = {book: price for book, price in prices.items() if price > 25}
print(expensive)
# {'Python': 29.99, 'Java': 34.99}

# Create from range
squares = {x: x**2 for x in range(1, 6)}
print(squares)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
