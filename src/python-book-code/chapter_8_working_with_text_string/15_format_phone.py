"""
Example 15 from Chapter 8: Working with Text - String Manipulation
Python Programming Fundamentals by Rajesh Aadi

Format Phone
"""

def format_phone(phone):
    """Format phone number to (XXX) XXX-XXXX"""
    # Remove all non-digits
    digits = "".join(c for c in phone if c.isdigit())

    # Check length
    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    elif len(digits) == 11 and digits[0] == "1":
        return f"+1 ({digits[1:4]}) {digits[4:7]}-{digits[7:]}"
    else:
        return "Invalid phone number"

# Test
phones = [
    "5551234567",
    "555-123-4567",
    "(555) 123-4567",
    "1-555-123-4567",
    "15551234567"
]

for phone in phones:
    print(f"{phone:20} -> {format_phone(phone)}")
