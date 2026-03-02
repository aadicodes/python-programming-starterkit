"""
Example 3 from Chapter 1: The Beginning - Variables and Your First Program
Python Programming Fundamentals by Rajesh Aadi

Variable Naming Rules
"""

# Valid variable names
book_price = 29.99
total_revenue = 1500.00
customer_name_1 = "Alice"
_private_note = "internal use"

print("=== Valid Variable Names ===")
print(f"book_price = {book_price}")
print(f"total_revenue = {total_revenue}")
print(f"customer_name_1 = {customer_name_1}")
print(f"_private_note = {_private_note}")

# Invalid variable names (shown as comments - these would cause errors)
# 1st_book = "Error"       # Can't start with a number
# book-price = 29.99       # No hyphens allowed
# class = "Fiction"        # 'class' is a reserved keyword

print("\n=== Invalid Variable Names (would cause errors) ===")
print("1st_book      - Can't start with a number")
print("book-price    - No hyphens allowed")
print("class         - 'class' is a reserved keyword")

# Best practices: use snake_case
print("\n=== Best Practices ===")
print("Use lowercase with underscores (snake_case):")
print("  book_price      (good)")
print("  totalRevenue    (not Pythonic)")
print("  tr              (too short, not descriptive)")
