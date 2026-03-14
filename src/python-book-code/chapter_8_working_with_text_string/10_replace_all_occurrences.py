"""
Example 10 from Chapter 8: Working with Text - String Manipulation
Python Programming Fundamentals by Rajesh Aadi

Replace All Occurrences
"""

# Replace all occurrences
text = "Python is great. Python is powerful."
new_text = text.replace("Python", "Programming")
print(new_text)
# Programming is great. Programming is powerful.

# Replace with limit
text = "one, two, one, three, one"
new_text = text.replace("one", "1", 2)  # Replace first 2
print(new_text)  # 1, two, 1, three, one

# Remove by replacing with empty string
phone = "555-123-4567"
digits_only = phone.replace("-", "")
print(digits_only)  # 5551234567

# Chain replacements
text = "  Too   many    spaces  "
clean = text.strip().replace("   ", " ").replace("  ", " ")
print(clean)  # Too many spaces
