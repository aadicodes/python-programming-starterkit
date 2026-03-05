"""
Example 19 from Chapter 4: Doing Things Repeatedly - Loops
Python Programming Fundamentals by Rajesh Aadi

Example 19: Nested loops for pattern drawing
"""

width = 30
height = 4

# Draw top border
print("=" * width)

# Draw middle rows
for _ in range(height - 2):
    print("|" + " " * (width - 2) + "|")

# Draw bottom border
print("=" * width)
