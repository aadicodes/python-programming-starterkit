"""
Example 6 from Chapter 5: Organizing Code - Functions
Python Programming Fundamentals by Rajesh Aadi

Calculate Shipping
"""

def calculate_shipping(distance):
    if distance <= 50:
        return 5.99
    elif distance <= 200:
        return 8.99
    else:
        return 12.99

# Using the function
cost1 = calculate_shipping(30)
cost2 = calculate_shipping(150)
cost3 = calculate_shipping(300)

print(f"30 miles: ${cost1:.2f}")
print(f"150 miles: ${cost2:.2f}")
print(f"300 miles: ${cost3:.2f}")
