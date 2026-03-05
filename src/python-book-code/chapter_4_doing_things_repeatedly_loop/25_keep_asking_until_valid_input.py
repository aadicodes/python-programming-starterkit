"""
Example 25 from Chapter 4: Doing Things Repeatedly - Loops
Python Programming Fundamentals by Rajesh Aadi

Keep Asking Until Valid Input
"""

# Keep asking until valid input
while True:
    age_str = input("Enter customer age: ")

    if age_str.isdigit():
        age = int(age_str)
        if 13 <= age <= 120:
            print(f"Age {age} accepted")
            break
        else:
            print("Age must be between 13 and 120")
    else:
        print("Please enter a valid number")
