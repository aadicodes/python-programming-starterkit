"""
Example 8 from Chapter 4: Doing Things Repeatedly - Loops
Python Programming Fundamentals by Rajesh Aadi

Rangestop Starts At 0
"""

# range(stop) - starts at 0
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(start, stop) - custom start
for i in range(1, 6):
    print(i)  # 1, 2, 3, 4, 5

# range(start, stop, step) - custom increment
for i in range(0, 11, 2):
    print(i)  # 0, 2, 4, 6, 8, 10

# Counting backwards
for i in range(10, 0, -1):
    print(i)  # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
