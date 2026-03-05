"""
Example 19 from Chapter 7: Powerful Data Structures - Dictionaries and Sets
Python Programming Fundamentals by Rajesh Aadi

Dictionaries
"""

# DICTIONARIES

# Create
my_dict = {"key": "value"}
my_dict = dict(key="value")

# Access
value = my_dict["key"]
value = my_dict.get("key", "default")

# Add/Update
my_dict["new_key"] = "new_value"
my_dict.update({"key1": "val1", "key2": "val2"})

# Remove
value = my_dict.pop("key")
del my_dict["key"]
my_dict.clear()

# Check
if "key" in my_dict:
    pass

# Iterate
for key in my_dict:
    print(key, my_dict[key])

for key, value in my_dict.items():
    print(key, value)

# Methods
my_dict.keys()
my_dict.values()
my_dict.items()

# Comprehension
{k: v*2 for k, v in my_dict.items()}

# SETS

# Create
my_set = {1, 2, 3}
my_set = set([1, 2, 3])

# Add/Remove
my_set.add(4)
my_set.remove(1)
my_set.discard(1)  # No error if not found

# Operations
set1 | set2         # Union
set1 & set2         # Intersection
set1 - set2         # Difference
set1 ^ set2         # Symmetric difference

# Comparisons
set1 <= set2        # Subset
set1 < set2         # Proper subset
set1 >= set2        # Superset

# Remove duplicates
unique = list(set(my_list))
