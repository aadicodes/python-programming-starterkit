"""
Example 2 from Chapter 8: Working with Text - String Manipulation
Python Programming Fundamentals by Rajesh Aadi

Case Methods
"""

book_title = "python programming for beginners"

# Case methods
print(book_title.upper())       # PYTHON PROGRAMMING FOR BEGINNERS
print(book_title.lower())       # python programming for beginners
print(book_title.title())       # Python Programming For Beginners
print(book_title.capitalize())  # Python programming for beginners

# Swap case
mixed = "Python 3.9"
print(mixed.swapcase())  # pYTHON 3.9

# Check case
print("HELLO".isupper())     # True
print("hello".islower())     # True
print("Hello".istitle())     # True
