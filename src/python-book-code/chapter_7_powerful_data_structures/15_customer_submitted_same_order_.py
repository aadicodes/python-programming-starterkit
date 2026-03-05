"""
Example 15 from Chapter 7: Powerful Data Structures - Dictionaries and Sets
Python Programming Fundamentals by Rajesh Aadi

Customer Submitted Same Order 
"""

# Customer submitted same order multiple times
order_items = ["Python", "Java", "Python", "JavaScript", "Java", "Python"]

# Remove duplicates
unique_items = list(set(order_items))
print(unique_items)  # ['Python', 'Java', 'JavaScript']

# Preserve order (Python 3.7+)
unique_ordered = list(dict.fromkeys(order_items))
print(unique_ordered)  # ['Python', 'Java', 'JavaScript']
