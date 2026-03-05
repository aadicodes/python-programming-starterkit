"""
Example 29 from Chapter 4: Doing Things Repeatedly - Loops
Python Programming Fundamentals by Rajesh Aadi

While Loop
"""

# While Loop
while condition:
    # code block
    # update condition variable

# For Loop with range()
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):       # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):   # 0, 2, 4, 6, 8
    print(i)

# For Loop with String
for char in "Python":
    print(char)

# Break (exit loop)
for i in range(10):
    if i == 5:
        break           # Stops at 5
    print(i)

# Continue (skip iteration)
for i in range(5):
    if i == 2:
        continue        # Skips 2
    print(i)            # Prints 0, 1, 3, 4

# Nested Loops
for i in range(3):
    for j in range(3):
        print(f"{i},{j}")

# Common Patterns
# Accumulator
total = 0
for i in range(1, 6):
    total += i          # Sum 1+2+3+4+5

# Counter
count = 0
for item in items:
    if condition:
        count += 1

# Validation Loop
while True:
    value = input("Enter: ")
    if valid(value):
        break
