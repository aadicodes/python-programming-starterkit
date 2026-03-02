"""
Example 5 from Chapter 1: The Beginning - Variables and Your First Program
Python Programming Fundamentals by Rajesh Aadi
Practice Exercises
"""

# Exercise 1: Personal Bookstore
print("=== Exercise 1: Personal Bookstore ===")
title = "The Great Gatsby"
author = "F. Scott Fitzgerald"
year_published = 1925
rating = 5

print(f"Title: {title}")
print(f"Author: {author}")
print(f"Year Published: {year_published}")
print(f"Rating: {'*' * rating} ({rating}/5)")

print()

# Exercise 2: Profit Calculator
print("=== Exercise 2: Profit Calculator ===")
books_sold = 150
cost_per_book = 8.50
selling_price = 24.99

total_cost = books_sold * cost_per_book
total_revenue = books_sold * selling_price
total_profit = total_revenue - total_cost

print(f"Books Sold: {books_sold}")
print(f"Cost per Book: ${cost_per_book:.2f}")
print(f"Selling Price: ${selling_price:.2f}")
print(f"Total Cost: ${total_cost:.2f}")
print(f"Total Revenue: ${total_revenue:.2f}")
print(f"Total Profit: ${total_profit:.2f}")
