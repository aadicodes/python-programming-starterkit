"""
Example 3 from Chapter 8: Working with Text - String Manipulation
Python Programming Fundamentals by Rajesh Aadi

Email Validation Case Insensit
"""

# Email validation (case-insensitive)
def validate_email(email):
    email = email.lower().strip()
    return "@" in email and "." in email

# Product search (case-insensitive)
def search_products(query, catalog):
    query = query.lower()
    return [product for product in catalog
            if query in product['title'].lower()]

# Name formatting
def format_name(name):
    return name.strip().title()

customer_name = "  aLiCe   jOhNsOn  "
print(format_name(customer_name))  # Alice Johnson
