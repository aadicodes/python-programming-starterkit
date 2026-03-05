"""
Example 17 from Chapter 5: Organizing Code - Functions
Python Programming Fundamentals by Rajesh Aadi

Now Sarah Can Use These Functi
"""

# Now Sarah can use these functions in any program!

# Example program using the utilities
from businessutils import *

print_header("BOOKISH CORNER - QUICK ORDER")

# Get order information
subtotal = get_validated_number("Enter order subtotal: $", 0)
is_member = get_yes_no("Is customer a member?")

if is_member:
    customer_type = input("Member type (member/premium): ").lower()
    if customer_type not in ["member", "premium"]:
        customer_type = "member"
else:
    customer_type = "regular"

location = input("Location (local/regional/remote): ").lower()
if location not in ["local", "regional", "remote"]:
    location = "regional"

# Calculate order
order_details = calculate_order_total(subtotal, customer_type, is_member, location)

# Display results
print()
print_order_summary(order_details)

# Optional email collection
print()
if get_yes_no("Would you like to receive confirmation by email?"):
    while True:
        email = input("Enter email address: ")
        if validate_email(email):
            print(f"✓ Confirmation will be sent to {email}")
            break
        else:
            print("✗ Invalid email address. Please try again.")

print("\nThank you for your order!")
