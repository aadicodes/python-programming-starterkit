"""
Example 13 from Chapter 8: Working with Text - String Manipulation
Python Programming Fundamentals by Rajesh Aadi

Positional Arguments
"""

# Positional arguments
template = "Name: {}, Email: {}, Points: {}"
result = template.format("Alice", "alice@email.com", 1250)
print(result)

# Named arguments
template = "Name: {name}, Email: {email}, Points: {points}"
result = template.format(name="Alice", email="alice@email.com", points=1250)
print(result)

# Mixed
template = "{0} ordered {1} books for ${2:.2f}"
result = template.format("Alice", 3, 89.97)
print(result)

# Formatting in format()
template = "Price: ${0:,.2f}"
print(template.format(1234.567))  # Price: $1,234.57
