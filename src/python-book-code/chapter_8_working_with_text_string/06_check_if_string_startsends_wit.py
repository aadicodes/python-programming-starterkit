"""
Example 6 from Chapter 8: Working with Text - String Manipulation
Python Programming Fundamentals by Rajesh Aadi

Check If String Startsends Wit
"""

email = "customer@bookishcorner.com"

# Check if string starts/ends with
print(email.startswith("customer"))  # True
print(email.endswith(".com"))        # True
print(email.endswith(".org"))        # False

# Find position of substring
pos = email.find("@")
print(pos)  # 8

# find() returns -1 if not found
pos = email.find("xyz")
print(pos)  # -1

# index() raises error if not found
# pos = email.index("xyz")  # ValueError!

# Count occurrences
text = "Python is awesome. Python is powerful."
count = text.count("Python")
print(count)  # 2
