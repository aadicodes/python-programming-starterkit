"""
Example 9 from Chapter 6: Managing Collections - Lists and Tuples
Python Programming Fundamentals by Rajesh Aadi

Check If Item Exists
"""

inventory = ["Python Programming", "JavaScript Basics", "Data Science"]

# Check if item exists
if "Python Programming" in inventory:
    print("We have Python Programming in stock!")

if "Ruby Guide" not in inventory:
    print("Ruby Guide is not available")

# Count occurrences
cart = ["Python", "Java", "Python", "Python", "JavaScript"]
python_count = cart.count("Python")
print(f"Python books in cart: {python_count}")  # 3
