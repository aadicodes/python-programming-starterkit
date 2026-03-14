"""
Example 15 from Chapter 10: Handling Problems - Error Handling and Exceptions
Python Programming Fundamentals by Rajesh Aadi

Get Positive Integer
"""

def get_positive_integer(prompt):
    """Get positive integer from user with validation"""
    while True:
        try:
            value = int(input(prompt))

            if value <= 0:
                raise ValueError("Value must be positive")

            return value

        except ValueError as e:
            print(f"Invalid input: {e}")
            print("Please try again.\n")

# Usage
quantity = get_positive_integer("Enter quantity: ")
