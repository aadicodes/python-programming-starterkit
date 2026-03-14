"""
Example 5 from Chapter 12: Scaling Up - Modules and Packages
Python Programming Fundamentals by Rajesh Aadi

Good - Clear What's Being Used (Import Best Practices)
"""

# Define math_utils functions inline for demonstration
def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def calculate_tax(amount, rate=0.08):
    """Calculate tax on an amount"""
    return amount * rate

# ✓ GOOD - Clear what's being used
from_imports = [add, subtract, calculate_tax]
print("✓ GOOD - Explicit imports are clear")
result1 = add(10, 5)
print(f"add(10, 5) = {result1}")
result2 = calculate_tax(100)
print(f"calculate_tax(100) = {result2}")

# ✓ GOOD - Clear where it comes from
print("\n✓ GOOD - Module-qualified imports are clear")
def math_utils_add(a, b):
    return a + b
result = math_utils_add(10, 5)
print(f"math_utils.add(10, 5) = {result}")

# ✗ AVOID - Unclear where functions come from
# (Commented out to avoid namespace pollution)
# from math_utils import *

# ✓ GOOD - Descriptive alias
import_as = add
print("\n✓ GOOD - Descriptive alias (math_ops = add)")
result = import_as(10, 5)
print(f"math_ops(10, 5) = {result}")

# ✗ AVOID - Confusing alias (commented out)
# import math_utils as m  # What does 'm' mean?

print("\nBest practice: Use explicit imports or qualified names!")
