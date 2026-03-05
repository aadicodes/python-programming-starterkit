"""
Example 11 from Chapter 2: Understanding Data - Types and Operations
Python Programming Fundamentals by Rajesh Aadi

Changing Case
"""

book_title = "python programming fundamentals"

# Changing case
print(book_title.upper())       # PYTHON PROGRAMMING FUNDAMENTALS
print(book_title.lower())       # python programming fundamentals
print(book_title.title())       # Python Programming Fundamentals
print(book_title.capitalize())  # Python programming fundamentals

# Checking content
email = "customer@email.com"
print(email.endswith(".com"))   # True
print(email.startswith("cust")) # True

# Finding and replacing
description = "This book teaches Python basics"
print(description.find("Python"))        # 17 (index position)
print(description.replace("Python", "programming"))  # Replace text

# Stripping whitespace
user_input = "  john@email.com  "
clean_email = user_input.strip()  # "john@email.com"

# Splitting strings
csv_data = "John,Smith,john@email.com"
parts = csv_data.split(",")
print(parts)  # ['John', 'Smith', 'john@email.com']

# Joining strings
words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print(sentence)  # Python is awesome
