"""
Example 5 from Chapter 5: Organizing Code - Functions
Python Programming Fundamentals by Rajesh Aadi

Send Confirmation Email
"""

def send_confirmation_email(customer_name, order_number):
    print(f"Sending confirmation to {customer_name}")
    print(f"Order #{order_number} has been processed")
    print("Thank you for your purchase!\n")

# Call the function
send_confirmation_email("Alice Johnson", 1234)
send_confirmation_email("Bob Smith", 1235)
