"""
Example 8 from Chapter 8: Working with Text - String Manipulation
Python Programming Fundamentals by Rajesh Aadi

Split By Whitespace Default
"""

# Split by whitespace (default)
sentence = "Python is awesome"
words = sentence.split()
print(words)  # ['Python', 'is', 'awesome']

# Split by specific character
csv_line = "John,Doe,john@email.com,555-1234"
fields = csv_line.split(",")
print(fields)  # ['John', 'Doe', 'john@email.com', '555-1234']

# Limit splits
text = "one,two,three,four,five"
parts = text.split(",", 2)  # Split max 2 times
print(parts)  # ['one', 'two', 'three,four,five']

# Split by lines
multi_line = """Line 1
Line 2
Line 3"""
lines = multi_line.split("\n")
print(lines)  # ['Line 1', 'Line 2', 'Line 3']

# Split from right
path = "folder/subfolder/file.txt"
parts = path.rsplit("/", 1)
print(parts)  # ['folder/subfolder', 'file.txt']

# Partition - split into 3 parts
email = "customer@bookishcorner.com"
username, at, domain = email.partition("@")
print(username)  # customer
print(domain)    # bookishcorner.com
