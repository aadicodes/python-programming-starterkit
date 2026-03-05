"""
Example 20 from Chapter 3: Making Decisions - Conditional Statements
Python Programming Fundamentals by Rajesh Aadi

Wrong Case Matters
"""

user_input = "Yes"

# WRONG - Case matters!
if user_input == "yes":  # False!
    print("Confirmed")

# CORRECT - Convert to lowercase
if user_input.lower() == "yes":
    print("Confirmed")
