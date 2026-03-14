"""
Example 17 from Chapter 10: Handling Problems - Error Handling and Exceptions
Python Programming Fundamentals by Rajesh Aadi

Calculate Order Total
"""

def calculate_order_total(items, tax_rate=0.08, discount=0):
    """
    Calculate order total with error handling

    Args:
        items: List of (price, quantity) tuples
        tax_rate: Tax rate (default 0.08)
        discount: Discount amount (default 0)

    Returns:
        dict with subtotal, tax, discount, total

    Raises:
        ValueError: If invalid parameters
        TypeError: If wrong type
    """
    # Validate items
    if not items:
        raise ValueError("Order must contain at least one item")

    if not isinstance(items, list):
        raise TypeError("Items must be a list")

    # Validate tax_rate
    try:
        tax_rate = float(tax_rate)
    except (ValueError, TypeError):
        raise ValueError("Tax rate must be a number")

    if not 0 <= tax_rate <= 1:
        raise ValueError("Tax rate must be between 0 and 1")

    # Validate discount
    try:
        discount = float(discount)
    except (ValueError, TypeError):
        raise ValueError("Discount must be a number")

    if discount < 0:
        raise ValueError("Discount cannot be negative")

    # Calculate subtotal
    subtotal = 0
    try:
        for price, quantity in items:
            if price < 0 or quantity < 0:
                raise ValueError("Price and quantity must be non-negative")
            subtotal += price * quantity
    except (ValueError, TypeError) as e:
        raise ValueError(f"Invalid item data: {e}")

    # Validate discount doesn't exceed subtotal
    if discount > subtotal:
        raise ValueError("Discount cannot exceed subtotal")

    # Calculate totals
    subtotal_after_discount = subtotal - discount
    tax = subtotal_after_discount * tax_rate
    total = subtotal_after_discount + tax

    return {
        "subtotal": round(subtotal, 2),
        "discount": round(discount, 2),
        "tax": round(tax, 2),
        "total": round(total, 2)
    }

# Usage
try:
    result = calculate_order_total(
        [(29.99, 2), (19.99, 1)],
        tax_rate=0.08,
        discount=10.00
    )
    print(f"Total: ${result['total']:.2f}")

except (ValueError, TypeError) as e:
    print(f"Error: {e}")
