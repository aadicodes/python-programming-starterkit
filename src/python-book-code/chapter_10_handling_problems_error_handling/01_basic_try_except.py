"""
Example 1 from Chapter 10: Handling Problems - Error Handling and Exceptions
Python Programming Fundamentals by Rajesh Aadi

Example 01: Basic Error Handling - Try/Except
"""

# Basic try-except block
try:
    # This might cause an error
    quantity = int("abc")  # ValueError will occur
except ValueError:
    # Handle the error gracefully
    print("Please enter a valid number")
    quantity = 0

print(f"Quantity set to: {quantity}")

# Another example with different error types
try:
    # Simulating user input for testing
    user_input = "42"
    number = int(user_input)
    result = 100 / number
    print(f"Result: {result}")
except ValueError:
    print("Error: Invalid number format")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
except Exception as e:
    print(f"Unexpected error: {e}")
