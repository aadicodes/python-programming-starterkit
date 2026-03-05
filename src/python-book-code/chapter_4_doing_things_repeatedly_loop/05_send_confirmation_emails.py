"""
Example 5 from Chapter 4: Doing Things Repeatedly - Loops
Python Programming Fundamentals by Rajesh Aadi

Send Confirmation Emails
"""

# Send confirmation emails
email_count = 1
max_emails = 10

while email_count <= max_emails:
    print(f"Sending confirmation email {email_count}...")
    email_count += 1

print(f"All {max_emails} emails sent!")
