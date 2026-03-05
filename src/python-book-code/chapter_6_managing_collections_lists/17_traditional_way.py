"""
Example 17 from Chapter 6: Managing Collections - Lists and Tuples
Python Programming Fundamentals by Rajesh Aadi

Traditional Way
"""

# Traditional way
prices = [29.99, 34.50, 39.99]
prices_with_tax = []
for price in prices:
    prices_with_tax.append(price * 1.08)

# List comprehension way
prices_with_tax = [price * 1.08 for price in prices]
print(prices_with_tax)  # [32.39, 37.26, 43.19]

# More examples
numbers = [1, 2, 3, 4, 5]
squares = [n ** 2 for n in numbers]
print(squares)  # [1, 4, 9, 16, 25]

books = ["python", "javascript", "java"]
uppercase = [book.upper() for book in books]
print(uppercase)  # ['PYTHON', 'JAVASCRIPT', 'JAVA']
