"""
Example 5 from Chapter 8: Working with Text - String Manipulation
Python Programming Fundamentals by Rajesh Aadi

Center Text
"""

# Center text
title = "INVOICE"
print(title.center(50, "="))
# ======================INVOICE======================

# Left align
product = "Python Book"
print(product.ljust(30, "."))
# Python Book...................

# Right align
price = "29.99"
print(price.rjust(10))
#      29.99

# Zero padding for numbers
order_id = "42"
print(order_id.zfill(6))  # 000042
