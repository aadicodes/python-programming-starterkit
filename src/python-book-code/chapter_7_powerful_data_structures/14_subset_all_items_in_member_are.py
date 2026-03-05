"""
Example 14 from Chapter 7: Powerful Data Structures - Dictionaries and Sets
Python Programming Fundamentals by Rajesh Aadi

Subset All Items In Member Are
"""

premium_features = {"discount", "free_shipping", "priority_support"}
member_features = {"discount", "free_shipping"}

# Subset - all items in member are in premium
is_subset = member_features <= premium_features
print(is_subset)  # True

# Proper subset - subset but not equal
is_proper_subset = member_features < premium_features
print(is_proper_subset)  # True

# Superset
is_superset = premium_features >= member_features
print(is_superset)  # True

# Disjoint - no common elements
set1 = {"a", "b", "c"}
set2 = {"d", "e", "f"}
print(set1.isdisjoint(set2))  # True
