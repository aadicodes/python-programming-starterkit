"""
Example 13 from Chapter 3: Making Decisions - Conditional Statements
Python Programming Fundamentals by Rajesh Aadi

Example 13
"""

print("Are you a member? (yes/no)")
response = input("> ").lower().strip()

if response == "yes" or response == "y":
    is_member = True
    print("Member status confirmed")
elif response == "no" or response == "n":
    is_member = False
    print("Proceeding as guest")
else:
    print("Invalid response. Please enter yes or no.")
    is_member = False
