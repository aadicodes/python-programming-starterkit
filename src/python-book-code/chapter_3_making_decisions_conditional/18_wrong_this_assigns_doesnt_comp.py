"""
Example 18 from Chapter 3: Making Decisions - Conditional Statements
Python Programming Fundamentals by Rajesh Aadi

Wrong This Assigns Doesnt Comp
"""

# WRONG - This assigns, doesn't compare!
if customer_type = "member":  # SyntaxError!
    print("Member")

# CORRECT - Use == for comparison
if customer_type == "member":
    print("Member")
