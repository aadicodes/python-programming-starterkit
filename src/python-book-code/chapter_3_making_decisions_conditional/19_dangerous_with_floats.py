"""
Example 19 from Chapter 3: Making Decisions - Conditional Statements
Python Programming Fundamentals by Rajesh Aadi

Dangerous With Floats
"""

# Dangerous with floats
price = 0.1 + 0.1 + 0.1
if price == 0.3:  # Might be False due to floating-point precision!
    print("Match")

# Better approach
if abs(price - 0.3) < 0.0001:  # Check if "close enough"
    print("Match")
