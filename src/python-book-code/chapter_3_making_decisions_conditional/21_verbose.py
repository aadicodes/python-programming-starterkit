"""
Example 21 from Chapter 3: Making Decisions - Conditional Statements
Python Programming Fundamentals by Rajesh Aadi

Verbose
"""

# Verbose
if status == "member" or status == "premium" or status == "vip":
    apply_discount()

# Better
if status in ["member", "premium", "vip"]:
    apply_discount()
