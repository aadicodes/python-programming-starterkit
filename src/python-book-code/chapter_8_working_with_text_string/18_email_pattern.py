"""
Example 18 from Chapter 8: Working with Text - String Manipulation
Python Programming Fundamentals by Rajesh Aadi

Email Pattern
"""

import re

# Email pattern
email_pattern = r"[\w\.-]+@[\w\.-]+\.\w+"

# Phone pattern (various formats)
phone_pattern = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"

# URL pattern
url_pattern = r"https?://[\w\.-]+\.\w+"

# Postal code pattern (US ZIP)
zip_pattern = r"\d{5}(-\d{4})?"

# ISBN-10 pattern
isbn_pattern = r"\d{1,5}-\d{1,7}-\d{1,7}-[\dX]"

# Test
text = """
Contact: alice@email.com
Phone: (555) 123-4567
Website: https://bookishcorner.com
ZIP: 02101-1234
ISBN: 978-0-123456-78-9
"""

print("Emails:", re.findall(email_pattern, text))
print("Phones:", re.findall(phone_pattern, text))
print("URLs:", re.findall(url_pattern, text))
print("ZIP codes:", re.findall(zip_pattern, text))
