"""
Example 20 from Chapter 5: Organizing Code - Functions
Python Programming Fundamentals by Rajesh Aadi

Traditional Function
"""

# Traditional function
def add_ten(x):
    return x + 10

# Lambda equivalent - one-line anonymous function
add_ten_lambda = lambda x: x + 10

print(add_ten(5))          # 15
print(add_ten_lambda(5))   # 15

# Useful for simple operations
prices = [19.99, 29.99, 39.99]
with_tax = list(map(lambda p: p * 1.08, prices))
print(with_tax)  # [21.59, 32.39, 43.19]
