"""
Example 22 from Chapter 5: Organizing Code - Functions
Python Programming Fundamentals by Rajesh Aadi

Define Function
"""

# Define Function
def function_name(param1, param2):
    """Docstring describing function"""
    result = param1 + param2
    return result

# Call Function
value = function_name(5, 10)

# Default Parameters
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Multiple Return Values
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)

min_val, max_val, total = get_stats([1, 2, 3, 4, 5])

# Variable Scope
global_var = 10

def my_function():
    local_var = 5        # Only exists in function
    return local_var + global_var

# Lambda Function
square = lambda x: x ** 2
print(square(5))  # 25

# Docstring
def my_func():
    """This describes what my_func does"""
    pass

# Common Patterns
def validate_input(value, min_val=0):
    """Return True if valid, False otherwise"""
    return value >= min_val

def calculate_total(items):
    """Sum all items"""
    total = 0
    for item in items:
        total += item
    return total
