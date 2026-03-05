"""
Example 18 from Chapter 4: Doing Things Repeatedly - Loops
Python Programming Fundamentals by Rajesh Aadi

Create A Simple Receipt Border
"""

# Create a simple receipt border
print("Receipt Border Pattern:\n")

rows = 5
cols = 30

for row in range(rows):
    for col in range(cols):
        if row == 0 or row == rows - 1:
            print("=", end="")
        elif col == 0 or col == cols - 1:
            print("|", end="")
        else:
            print(" ", end="")
    print()  # New line after each row
