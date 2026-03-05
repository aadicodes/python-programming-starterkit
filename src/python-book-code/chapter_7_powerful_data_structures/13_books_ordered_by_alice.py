"""
Example 13 from Chapter 7: Powerful Data Structures - Dictionaries and Sets
Python Programming Fundamentals by Rajesh Aadi

Books Ordered By Alice
"""

# Books ordered by Alice
alice_books = {"Python", "JavaScript", "Java", "Data Science"}

# Books ordered by Bob
bob_books = {"Python", "Ruby", "Java", "Machine Learning"}

# Union - Books ordered by either Alice or Bob
all_books = alice_books | bob_books
# Or: all_books = alice_books.union(bob_books)
print(all_books)
# {'Python', 'JavaScript', 'Java', 'Ruby', 'Data Science', 'Machine Learning'}

# Intersection - Books ordered by both
common_books = alice_books & bob_books
# Or: common_books = alice_books.intersection(bob_books)
print(common_books)
# {'Python', 'Java'}

# Difference - Books only Alice ordered
alice_only = alice_books - bob_books
# Or: alice_only = alice_books.difference(bob_books)
print(alice_only)
# {'JavaScript', 'Data Science'}

# Symmetric Difference - Books ordered by only one person
unique_to_each = alice_books ^ bob_books
# Or: unique_to_each = alice_books.symmetric_difference(bob_books)
print(unique_to_each)
# {'JavaScript', 'Ruby', 'Data Science', 'Machine Learning'}
