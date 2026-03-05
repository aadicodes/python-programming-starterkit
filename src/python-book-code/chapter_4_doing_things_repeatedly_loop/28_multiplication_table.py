"""
Example 28 from Chapter 4: Doing Things Repeatedly - Loops
Python Programming Fundamentals by Rajesh Aadi

Example 28: Multiplication table using a loop
"""

number = 5

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")
