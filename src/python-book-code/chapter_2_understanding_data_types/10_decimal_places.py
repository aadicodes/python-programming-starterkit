"""
Example 10 from Chapter 2: Understanding Data - Types and Operations
Python Programming Fundamentals by Rajesh Aadi

Decimal Places
"""

amount = 1234.5678

# Decimal places
print(f"${amount:.2f}")      # $1234.57 (2 decimals)
print(f"${amount:.0f}")      # $1235 (no decimals)

# Width and alignment
print(f"|{amount:10.2f}|")   # |   1234.57| (right-aligned, width 10)
print(f"|{amount:<10.2f}|")  # |1234.57   | (left-aligned)
print(f"|{amount:^10.2f}|")  # | 1234.57  | (center-aligned)

# Padding with zeros
order_number = 42
print(f"Order #{order_number:05d}")  # Order #00042

# Thousands separator
large_number = 1000000
print(f"${large_number:,.2f}")  # $1,000,000.00

# Percentage
discount = 0.15
print(f"Discount: {discount:.1%}")  # Discount: 15.0%
