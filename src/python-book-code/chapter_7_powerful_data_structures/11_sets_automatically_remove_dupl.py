"""
Example 11 from Chapter 7: Powerful Data Structures - Dictionaries and Sets
Python Programming Fundamentals by Rajesh Aadi

Sets Automatically Remove Dupl
"""

# Sets automatically remove duplicates
visitors = {"Alice", "Bob", "Alice", "Charlie", "Bob"}
print(visitors)  # {'Alice', 'Bob', 'Charlie'} - only unique values

# Sets are unordered - no indexing
# visitors[0]  # TypeError! Can't index sets

# Sets are mutable (can be changed)
visitors.add("David")
visitors.remove("Bob")
