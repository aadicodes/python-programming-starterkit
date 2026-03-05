"""
Example 4 from Chapter 2: Understanding Data - Types and Operations
Python Programming Fundamentals by Rajesh Aadi

Float Precision Issues
"""

# Float precision issues
price1 = 0.1 + 0.1 + 0.1
print(price1)  # 0.30000000000000004 (surprise!)

# Solution: Round for display
price1_rounded = round(price1, 2)
print(price1_rounded)  # 0.3

# Better solution for money: use integers (cents)
price_cents = 2999  # $29.99
price_dollars = price_cents / 100
print(f"${price_dollars:.2f}")  # $29.99
