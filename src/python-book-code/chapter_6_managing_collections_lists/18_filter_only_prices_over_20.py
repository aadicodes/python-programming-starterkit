"""
Example 18 from Chapter 6: Managing Collections - Lists and Tuples
Python Programming Fundamentals by Rajesh Aadi

Filter Only Prices Over 20
"""

prices = [29.99, 15.99, 45.00, 12.50, 35.99]

# Filter: only prices over $20
expensive = [price for price in prices if price > 20]
print(expensive)  # [29.99, 45.00, 35.99]

# Transform and filter
discounted = [price * 0.9 for price in prices if price > 30]
print(discounted)  # [40.5, 32.39]

# If-else in comprehension
stock = [25, 5, 0, 15, 3]
status = ["In Stock" if qty > 10 else "Low Stock" for qty in stock]
print(status)  # ['In Stock', 'Low Stock', 'Low Stock', 'In Stock', 'Low Stock']
