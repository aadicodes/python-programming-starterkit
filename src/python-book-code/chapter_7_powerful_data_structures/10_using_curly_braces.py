"""
Example 10 from Chapter 7: Powerful Data Structures - Dictionaries and Sets
Python Programming Fundamentals by Rajesh Aadi

Using Curly Braces
"""

# Using curly braces
categories = {"Programming", "Business", "Science"}

# Using set() constructor
languages = set(["Python", "Java", "JavaScript"])

# Create from string (unique characters)
letters = set("hello")
print(letters)  # {'h', 'e', 'l', 'o'}

# Empty set (must use set(), not {})
empty = set()  # Correct
# empty = {}   # This creates an empty DICTIONARY!
