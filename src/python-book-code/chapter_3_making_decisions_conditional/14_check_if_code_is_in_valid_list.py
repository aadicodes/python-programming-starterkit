"""
Example 14 from Chapter 3: Making Decisions - Conditional Statements
Python Programming Fundamentals by Rajesh Aadi

Check If Code Is In Valid List
"""

discount_code = input("Enter discount code: ").upper()

# Check if code is in valid list
if discount_code in ["SAVE10", "WELCOME", "LOYAL"]:
    print("Valid discount code!")
else:
    print("Invalid discount code")

# Range checking
customer_age = int(input("Enter your age: "))

if 13 <= customer_age <= 18:
    print("Student discount available!")
elif customer_age < 13:
    print("Parental consent required")
else:
    print("Standard pricing applies")
