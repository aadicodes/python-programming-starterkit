"""
Example 18 from Chapter 5: Organizing Code - Functions
Python Programming Fundamentals by Rajesh Aadi

Calculate Loyalty Points
"""

def calculate_loyalty_points(amount, customer_type):
    """
    Calculate loyalty points earned for a purchase.

    Parameters:
        amount (float): The purchase amount in dollars
        customer_type (str): Type of customer ('regular', 'member', 'premium')

    Returns:
        int: Number of loyalty points earned

    Examples:
        >>> calculate_loyalty_points(100, 'member')
        100
        >>> calculate_loyalty_points(100, 'premium')
        200
    """
    if customer_type == "premium":
        return int(amount * 2)
    elif customer_type == "member":
        return int(amount)
    else:
        return 0

# Access the docstring
print(calculate_loyalty_points.__doc__)

# Or use help()
help(calculate_loyalty_points)
