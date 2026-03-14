"""
Example 12 from Chapter 8: Working with Text - String Manipulation
Python Programming Fundamentals by Rajesh Aadi

Basic F String
"""

# Basic f-string
name = "Alice"
age = 25
print(f"{name} is {age} years old")

# Expressions in f-strings
price = 29.99
quantity = 3
print(f"Total: ${price * quantity}")  # Total: $89.97

# Formatting numbers
amount = 1234.5678

print(f"{amount:.2f}")       # 1234.57 (2 decimals)
print(f"{amount:,.2f}")      # 1,234.57 (thousands separator)
print(f"{amount:>10.2f}")    # "   1234.57" (right-aligned, width 10)
print(f"{amount:<10.2f}")    # "1234.57   " (left-aligned)
print(f"{amount:^10.2f}")    # " 1234.57  " (centered)
print(f"{amount:0>10.2f}")   # 0001234.57 (zero-padded)

# Percentages
discount = 0.15
print(f"Discount: {discount:.1%}")  # Discount: 15.0%

# Dates
from datetime import datetime
now = datetime.now()
print(f"Date: {now:%Y-%m-%d}")      # Date: 2026-02-09
print(f"Time: {now:%H:%M:%S}")      # Time: 14:30:45
print(f"Full: {now:%B %d, %Y}")     # Full: February 09, 2026
