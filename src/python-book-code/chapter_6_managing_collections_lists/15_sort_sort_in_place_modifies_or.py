"""
Example 15 from Chapter 6: Managing Collections - Lists and Tuples
Python Programming Fundamentals by Rajesh Aadi

Sort Sort In Place Modifies Or
"""

prices = [29.99, 34.50, 19.99, 44.50, 24.99]

# sort() - Sort in place (modifies original list)
prices.sort()
print(prices)  # [19.99, 24.99, 29.99, 34.50, 44.50]

# sort(reverse=True) - Sort descending
prices.sort(reverse=True)
print(prices)  # [44.50, 34.50, 29.99, 24.99, 19.99]

# sorted() - Return new sorted list (original unchanged)
original = [29.99, 19.99, 39.99]
sorted_prices = sorted(original)
print(original)       # [29.99, 19.99, 39.99] (unchanged)
print(sorted_prices)  # [19.99, 29.99, 39.99]

# reverse() - Reverse in place
books = ["Python", "JavaScript", "Java"]
books.reverse()
print(books)  # ['Java', 'JavaScript', 'Python']
