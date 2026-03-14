"""
Example 14 from Chapter 8: Working with Text - String Manipulation
Python Programming Fundamentals by Rajesh Aadi

Validate Email
"""

def validate_email(email):
    """Validate email address format"""
    email = email.strip().lower()

    # Basic checks
    if not email:
        return False, "Email cannot be empty"

    if email.count("@") != 1:
        return False, "Email must contain exactly one @"

    if not "." in email:
        return False, "Email must contain a domain"

    # Split into parts
    username, domain = email.split("@")

    if not username:
        return False, "Username part is empty"

    if not domain:
        return False, "Domain part is empty"

    if domain.startswith(".") or domain.endswith("."):
        return False, "Invalid domain format"

    return True, "Valid email"

# Test
emails = [
    "alice@email.com",
    "invalid",
    "@email.com",
    "user@",
    "user@@domain.com"
]

for email in emails:
    valid, message = validate_email(email)
    print(f"{email:30} - {message}")
