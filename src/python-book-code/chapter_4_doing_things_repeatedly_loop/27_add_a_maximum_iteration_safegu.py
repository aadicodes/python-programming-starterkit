"""
Example 27 from Chapter 4: Doing Things Repeatedly - Loops
Python Programming Fundamentals by Rajesh Aadi

Add A Maximum Iteration Safegu
"""

# Add a maximum iteration safeguard
max_attempts = 100
attempts = 0

while True:
    attempts += 1

    if attempts > max_attempts:
        print("Maximum attempts reached. Exiting.")
        break

    # Your loop code here
    response = input("Enter command (or 'quit'): ")
    if response == 'quit':
        break
