"""
Example 9 from Chapter 8: Working with Text - String Manipulation
Python Programming Fundamentals by Rajesh Aadi

Join List Into String
"""

# Join list into string
words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print(sentence)  # Python is awesome

# Join with different separator
csv_fields = ["John", "Doe", "john@email.com"]
csv_line = ",".join(csv_fields)
print(csv_line)  # John,Doe,john@email.com

# Join file path
path_parts = ["folder", "subfolder", "file.txt"]
path = "/".join(path_parts)
print(path)  # folder/subfolder/file.txt

# Join empty string (concatenate)
letters = ["H", "e", "l", "l", "o"]
word = "".join(letters)
print(word)  # Hello
