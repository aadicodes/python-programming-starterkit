"""
Example 11 from Chapter 8: Working with Text - String Manipulation
Python Programming Fundamentals by Rajesh Aadi

Remove Punctuation
"""

# Remove punctuation
import string

text = "Hello, World! How are you?"

# Create translation table to remove punctuation
translator = str.maketrans("", "", string.punctuation)
clean = text.translate(translator)
print(clean)  # Hello World How are you

# Replace characters
text = "Hello World"
# Replace H->J, W->V
translator = str.maketrans("HW", "JV")
result = text.translate(translator)
print(result)  # Jello Vorld

# Remove specific characters
text = "Price: $29.99"
translator = str.maketrans("", "", "$:")
clean = text.translate(translator)
print(clean)  # Price 29.99
