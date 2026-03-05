"""
Example 23 from Chapter 6: Managing Collections - Lists and Tuples
Python Programming Fundamentals by Rajesh Aadi

Create List
"""

# Create List
my_list = [1, 2, 3]
empty = []

# Access Items
first = my_list[0]
last = my_list[-1]

# Add Items
my_list.append(4)           # Add to end
my_list.insert(0, 0)        # Insert at position
my_list.extend([5, 6])      # Add multiple

# Remove Items
my_list.remove(3)           # Remove by value
last = my_list.pop()        # Remove and return last
item = my_list.pop(0)       # Remove at index
del my_list[0]              # Delete at index
my_list.clear()             # Remove all

# Operations
len(my_list)                # Length
item in my_list             # Membership
my_list.count(2)            # Count occurrences
my_list.index(3)            # Find index

# Slicing
my_list[1:4]                # Items 1-3
my_list[:3]                 # First 3
my_list[2:]                 # From index 2
my_list[::2]                # Every other
my_list[::-1]               # Reversed

# Sorting
my_list.sort()              # Sort in place
sorted(my_list)             # Return sorted copy
my_list.reverse()           # Reverse in place

# List Comprehension
[x*2 for x in numbers]                    # Transform
[x for x in numbers if x > 10]            # Filter
[x*2 for x in numbers if x > 5]           # Both

# Tuples
my_tuple = (1, 2, 3)
a, b, c = my_tuple          # Unpack
