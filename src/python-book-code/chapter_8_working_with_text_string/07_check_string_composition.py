"""
Example 7 from Chapter 8: Working with Text - String Manipulation
Python Programming Fundamentals by Rajesh Aadi

Check String Composition
"""

# Check string composition
isbn = "1234567890"
print(isbn.isdigit())      # True - all digits

code = "ABC123"
print(code.isalnum())      # True - alphanumeric

name = "Alice"
print(name.isalpha())      # True - all letters

email = "alice@email.com"
print(email.isalnum())     # False - contains @ and .

# Check for whitespace
print("   ".isspace())     # True
print("Hello World".isspace())  # False

# Practical validation
def is_valid_isbn_10(isbn):
    """Validate 10-digit ISBN"""
    clean = isbn.replace("-", "").replace(" ", "")
    return len(clean) == 10 and clean.isdigit()

print(is_valid_isbn_10("1-234-567-890"))  # True
print(is_valid_isbn_10("ABC-123"))        # False
