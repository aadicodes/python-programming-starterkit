"""
Example 21 from Chapter 5: Organizing Code - Functions
Python Programming Fundamentals by Rajesh Aadi

Version 50 Using Functions
"""

# Bookish Corner - Complete Order Processing System
# Version 5.0 - Using Functions

def get_customer_info():
    """Collect customer information"""
    print_header("CUSTOMER INFORMATION")

    name = input("Customer name: ")
    email = ""

    while True:
        email = input("Email address: ")
        if validate_email(email):
            break
        print("Invalid email. Please try again.")

    is_member = get_yes_no("Is customer a member?")

    customer_type = "regular"
    if is_member:
        customer_type = input("Member type (member/premium): ").lower()
        if customer_type not in ["member", "premium"]:
            customer_type = "member"

    return {
        'name': name,
        'email': email,
        'is_member': is_member,
        'type': customer_type
    }

def get_order_items():
    """Collect order items"""
    print_header("ORDER ITEMS")

    items = []
    subtotal = 0

    while True:
        print(f"\nItem #{len(items) + 1}")
        book_title = input("Book title (or 'done' to finish): ")

        if book_title.lower() == 'done':
            if len(items) == 0:
                print("You must add at least one item.")
                continue
            break

        quantity = int(get_validated_number("Quantity: ", 1))
        price = get_validated_number("Price per book: $", 0.01)

        item_total = quantity * price
        subtotal += item_total

        items.append({
            'title': book_title,
            'quantity': quantity,
            'price': price,
            'total': item_total
        })

        print(f"Added: {quantity}x {book_title} = {format_currency(item_total)}")

    return items, subtotal

def print_detailed_receipt(customer, items, order_details):
    """Print a complete receipt"""
    import random
    from datetime import datetime

    order_number = random.randint(10000, 99999)
    order_date = datetime.now().strftime("%B %d, %Y %I:%M %p")

    print("\n" + "=" * 60)
    print(" " * 23 + "BOOKISH CORNER")
    print(" " * 18 + "www.bookishcorner.com")
    print(" " * 21 + "ORDER RECEIPT")
    print("=" * 60)

    print(f"\nOrder #: {order_number}")
    print(f"Date: {order_date}")
    print(f"Customer: {customer['name']}")
    print(f"Email: {customer['email']}")
    print(f"Status: {customer['type'].title()}")

    print("\n" + "-" * 60)
    print(f"{'ITEM':<30} {'QTY':>5} {'PRICE':>10} {'TOTAL':>12}")
    print("-" * 60)

    for item in items:
        title = item['title'][:28]  # Truncate if too long
        print(f"{title:<30} {item['quantity']:>5} "
              f"{format_currency(item['price']):>10} "
              f"{format_currency(item['total']):>12}")

    print("-" * 60)
    print(f"{'Subtotal:':<48} {format_currency(order_details['subtotal']):>12}")

    if order_details['discount'] > 0:
        discount_pct = (order_details['discount'] / order_details['subtotal'] * 100)
        print(f"{'Discount (' + f'{discount_pct:.0f}%' + '):':<48} "
              f"-{format_currency(order_details['discount']):>11}")

    print(f"{'Tax (8%):':<48} {format_currency(order_details['tax']):>12}")

    if order_details['shipping'] == 0:
        print(f"{'Shipping:':<48} {'FREE':>12}")
    else:
        print(f"{'Shipping:':<48} {format_currency(order_details['shipping']):>12}")

    print("=" * 60)
    print(f"{'TOTAL:':<48} {format_currency(order_details['total']):>12}")
    print("=" * 60)

    # Loyalty points
    if customer['type'] != "regular":
        points = calculate_loyalty_points(
            order_details['amount_after_discount'],
            customer['type']
        )
        print(f"\n🎁 You earned {points} loyalty points!")

    print("\n" + " " * 15 + "Thank you for your business!")
    print(" " * 12 + "Please visit us again soon!\n")

def calculate_loyalty_points(amount, customer_type):
    """Calculate loyalty points for the purchase"""
    if customer_type == "premium":
        return int(amount * 2)
    elif customer_type == "member":
        return int(amount)
    else:
        return 0

def main():
    """Main program function"""
    print_header("BOOKISH CORNER - ORDER PROCESSING")

    # Get customer information
    customer = get_customer_info()

    # Get order items
    items, subtotal = get_order_items()

    # Get shipping location
    print()
    location = input("Shipping location (local/regional/remote): ").lower()
    if location not in ["local", "regional", "remote"]:
        location = "regional"

    # Calculate order totals
    order_details = calculate_order_total(
        subtotal,
        customer['type'],
        customer['is_member'],
        location
    )

    # Print receipt
    print_detailed_receipt(customer, items, order_details)

    # Ask if customer wants another order
    if get_yes_no("\nProcess another order?"):
        main()  # Recursive call to start over
    else:
        print("\nGoodbye!")

# Run the program
if __name__ == "__main__":
    main()
