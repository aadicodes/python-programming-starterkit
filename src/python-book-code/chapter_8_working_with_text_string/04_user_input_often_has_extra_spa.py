"""
Example 4 from Chapter 8: Working with Text - String Manipulation
Python Programming Fundamentals by Rajesh Aadi

User Input Often Has Extra Spa
"""

# User input often has extra spaces
user_input = "  alice@email.com  \n"

# Remove from both ends
clean = user_input.strip()     # "alice@email.com"

# Remove from left only
clean = user_input.lstrip()    # "alice@email.com  \n"

# Remove from right only
clean = user_input.rstrip()    # "  alice@email.com"

# Remove specific characters
price = "$29.99"
number = price.strip("$")      # "29.99"

code = "***DISCOUNT***"
clean_code = code.strip("*")   # "DISCOUNT"
