"""
Example 26 from Chapter 4: Doing Things Repeatedly - Loops
Python Programming Fundamentals by Rajesh Aadi

Dangerous Infinite Loop
"""

# DANGEROUS - Infinite loop!
# count = 1
# while count < 10:
#     print(count)
#     # Forgot to increment count!

# FIXED - Proper loop
count = 1
while count < 10:
    print(count)
    count += 1  # Don't forget this!

# DANGEROUS - Condition never becomes False
# while True:
#     print("This runs forever!")

# FIXED - Add exit condition
while True:
    response = input("Continue? (yes/no): ")
    if response.lower() == 'no':
        break  # Exit the loop
