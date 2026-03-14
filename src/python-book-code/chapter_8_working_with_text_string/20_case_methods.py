"""
Example 20 from Chapter 8: Working with Text - String Manipulation
Python Programming Fundamentals by Rajesh Aadi

Case Methods
"""

# Case Methods
text.upper()           # UPPERCASE
text.lower()           # lowercase
text.title()           # Title Case
text.capitalize()      # Capitalize first

# Trimming
text.strip()           # Remove whitespace both ends
text.lstrip()          # Remove from left
text.rstrip()          # Remove from right

# Searching
text.startswith("ab")  # Check start
text.endswith("xyz")   # Check end
text.find("sub")       # Find position (-1 if not found)
text.count("a")        # Count occurrences

# Testing
text.isdigit()         # All digits
text.isalpha()         # All letters
text.isalnum()         # Letters and digits
text.isspace()         # All whitespace

# Splitting/Joining
text.split(",")        # Split by delimiter
",".join(list)         # Join list

# Replacing
text.replace("old", "new")  # Replace text

# Formatting
f"{value:.2f}"         # 2 decimal places
f"{value:>10}"         # Right align, width 10
f"{value:,}"           # Thousands separator

# Regex
import re
re.findall(pattern, text)    # Find all matches
re.search(pattern, text)     # Find first match
re.sub(pattern, repl, text)  # Replace matches
