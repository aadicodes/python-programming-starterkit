"""
Example 16 from Chapter 4: Doing Things Repeatedly - Loops
Python Programming Fundamentals by Rajesh Aadi

Demonstrating The Difference
"""

# Demonstrating the difference
print("BREAK example:")
for i in range(1, 6):
    if i == 3:
        break  # Exits loop completely
    print(i)  # Output: 1, 2

print("\nCONTINUE example:")
for i in range(1, 6):
    if i == 3:
        continue  # Skips only this iteration
    print(i)  # Output: 1, 2, 4, 5
