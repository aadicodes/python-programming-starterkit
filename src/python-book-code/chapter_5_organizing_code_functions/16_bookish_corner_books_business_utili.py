"""
Example 16 from Chapter 5: Organizing Code - Functions
Python Programming Fundamentals by Rajesh Aadi

Bookish Corner Business Utili
"""

# Bookish Corner - Business Utilities Library
# businessutils.py

def format_currency(amount):
    """Format a number as currency with $ and 2 decimal places"""
    return f"${amount:,.2f}"

def validate_email(email):
    """Basic email validation"""
    if "@" not in email:
        return False
    if "." not in email:
        return False
    if email.count("@") != 1:
        return False
    return True

def calculate_discount(subtotal, customer_type):
    """Calculate discount based on customer type"""
    discount_rates = {
        "regular": 0.00,
        "member": 0.10,
        "premium": 0.15
    }

    rate = discount_rates.get(customer_type, 0.00)
    return subtotal * rate

def calculate_shipping(subtotal, is_member, location="regional"):
    """Calculate shipping cost"""
    # Free shipping conditions
    if is_member and subtotal >= 50:
        return 0.00
    if subtotal >= 75:
        return 0.00

    # Standard shipping rates
    shipping_rates = {
        "local": 5.99,
        "regional": 8.99,
        "remote": 12.99
    }

    return shipping_rates.get(location, 8.99)

def calculate_order_total(subtotal, customer_type="regular",
                         is_member=False, location="regional"):
    """Calculate complete order total with all fees"""
    # Calculate discount
    discount = calculate_discount(subtotal, customer_type)
    amount_after_discount = subtotal - discount

    # Calculate tax
    tax = amount_after_discount * 0.08

    # Calculate shipping
    shipping = calculate_shipping(subtotal, is_member, location)

    # Calculate total
    total = amount_after_discount + tax + shipping

    return {
        'subtotal': subtotal,
        'discount': discount,
        'amount_after_discount': amount_after_discount,
        'tax': tax,
        'shipping': shipping,
        'total': total
    }

def print_order_summary(order_details):
    """Print a formatted order summary"""
    print("=" * 50)
    print(" " * 18 + "ORDER SUMMARY")
    print("=" * 50)
    print(f"{'Subtotal:':<30} {format_currency(order_details['subtotal']):>15}")

    if order_details['discount'] > 0:
        print(f"{'Discount:':<30} -{format_currency(order_details['discount']):>14}")
        print(f"{'After discount:':<30} {format_currency(order_details['amount_after_discount']):>15}")

    print(f"{'Tax:':<30} {format_currency(order_details['tax']):>15}")
    print(f"{'Shipping:':<30} {format_currency(order_details['shipping']):>15}")
    print("-" * 50)
    print(f"{'TOTAL:':<30} {format_currency(order_details['total']):>15}")
    print("=" * 50)

def get_validated_number(prompt, min_value=0):
    """Get a validated numeric input from user"""
    while True:
        try:
            value = float(input(prompt))
            if value >= min_value:
                return value
            else:
                print(f"Value must be at least {min_value}")
        except ValueError:
            print("Please enter a valid number")

def get_yes_no(prompt):
    """Get a yes/no response from user"""
    while True:
        response = input(prompt + " (yes/no): ").lower().strip()
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        else:
            print("Please enter 'yes' or 'no'")

def print_header(title):
    """Print a formatted header"""
    width = 60
    print("\n" + "=" * width)
    print(title.center(width))
    print("=" * width + "\n")

def print_separator():
    """Print a separator line"""
    print("-" * 60)

# Example usage
if __name__ == "__main__":
    print_header("BOOKISH CORNER UTILITIES TEST")

    # Test currency formatting
    print("Currency formatting:")
    print(f"  {format_currency(1234.5)}")
    print(f"  {format_currency(1000000)}")

    print_separator()

    # Test email validation
    print("Email validation:")
    print(f"  john@email.com: {validate_email('john@email.com')}")
    print(f"  invalid.email: {validate_email('invalid.email')}")

    print_separator()

    # Test order calculation
    print("Order calculation:")
    order = calculate_order_total(100, "premium", True, "local")
    print_order_summary(order)
