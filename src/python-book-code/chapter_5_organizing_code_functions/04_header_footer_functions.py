"""
Example 4 from Chapter 5: Organizing Code - Functions
Python Programming Fundamentals by Rajesh Aadi

Example 04: Functions to organize repeated code
"""

def print_header():
    """Print the Bookish Corner header"""
    print("=" * 50)
    print(" " * 15 + "BOOKISH CORNER")
    print("=" * 50)

def print_welcome():
    """Print welcome message"""
    print("Welcome to our store!")

# Call the functions
print_header()
print_welcome()
print_header()
