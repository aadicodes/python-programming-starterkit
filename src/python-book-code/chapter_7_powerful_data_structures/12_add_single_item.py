"""
Example 12 from Chapter 7: Powerful Data Structures - Dictionaries and Sets
Python Programming Fundamentals by Rajesh Aadi

Add Single Item
"""

categories = {"Programming", "Business"}

# Add single item
categories.add("Science")
print(categories)  # {'Programming', 'Business', 'Science'}

# Add multiple items
categories.update(["Fiction", "History", "Art"])
print(categories)

# Remove item (raises error if not found)
categories.remove("Fiction")

# Discard item (no error if not found)
categories.discard("Fiction")  # No error
categories.discard("NonExistent")  # Still no error

# Remove and return arbitrary item
item = categories.pop()
print(f"Removed: {item}")

# Clear all items
categories.clear()
