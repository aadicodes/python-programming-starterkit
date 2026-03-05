"""
Example 20 from Chapter 6: Managing Collections - Lists and Tuples
Python Programming Fundamentals by Rajesh Aadi

Function Returning Multiple Va
"""

# Function returning multiple values
def get_book_info():
    title = "Python Programming"
    price = 29.99
    stock = 25
    return title, price, stock  # Returns a tuple

# Unpack the tuple
book_title, book_price, book_stock = get_book_info()
print(f"{book_title}: ${book_price}, Stock: {book_stock}")
