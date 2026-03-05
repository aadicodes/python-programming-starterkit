"""
Example 14 from Chapter 6: Managing Collections - Lists and Tuples
Python Programming Fundamentals by Rajesh Aadi

Calculate Total
"""

prices = [29.99, 34.50, 39.99, 24.99, 44.50]

# Calculate total
total = 0
for price in prices:
    total += price
print(f"Total inventory value: ${total:.2f}")

# Find maximum
max_price = prices[0]
for price in prices:
    if price > max_price:
        max_price = price
print(f"Most expensive book: ${max_price:.2f}")

# Or use built-in functions
print(f"Minimum price: ${min(prices):.2f}")
print(f"Maximum price: ${max(prices):.2f}")
print(f"Average price: ${sum(prices) / len(prices):.2f}")
