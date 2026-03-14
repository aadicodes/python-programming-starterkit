"""
Example 6 from Chapter 10: Handling Problems - Error Handling and Exceptions
Python Programming Fundamentals by Rajesh Aadi

Or Handle Separately
"""

try:
    value = int(input("Enter a number: "))
    result = 100 / value

except (ValueError, ZeroDivisionError) as error:
    print(f"Error occurred: {error}")

# Or handle separately
except ValueError:
    print("Invalid number format")
except ZeroDivisionError:
    print("Cannot divide by zero")
