"""
Example 20 from Chapter 4: Doing Things Repeatedly - Loops
Python Programming Fundamentals by Rajesh Aadi

Bookish Corner Daily Sales Re
"""

# Bookish Corner - Daily Sales Report Generator
# Version 4.0

import random
from datetime import date

print("=" * 70)
print(" " * 20 + "BOOKISH CORNER")
print(" " * 17 + "Daily Sales Report Generator")
print("=" * 70)

# Get reporting date
today = date.today()
report_date = today.strftime("%B %d, %Y")

print(f"\nReport Date: {report_date}")

# Get number of orders to process
while True:
    num_orders_str = input("Number of orders to process: ")
    if num_orders_str.isdigit() and int(num_orders_str) > 0:
        num_orders = int(num_orders_str)
        break
    else:
        print("Please enter a valid positive number.")

print("\n" + "=" * 70)
print("ENTERING ORDER DATA")
print("=" * 70)

# Initialize counters
total_revenue = 0
total_books_sold = 0
total_shipping = 0
total_tax = 0
member_orders = 0
large_orders = 0  # Orders over $100

# Store order details for summary
order_details = []

# Process each order
for order_num in range(1, num_orders + 1):
    print(f"\nOrder #{order_num}")
    print("-" * 70)

    # Get order information
    while True:
        subtotal_str = input("  Subtotal: $")
        if subtotal_str.replace(".", "").isdigit():
            subtotal = float(subtotal_str)
            if subtotal > 0:
                break
        print("  Invalid amount. Please enter a positive number.")

    while True:
        books_str = input("  Number of books: ")
        if books_str.isdigit() and int(books_str) > 0:
            books = int(books_str)
            break
        print("  Invalid quantity.")

    is_member = input("  Member? (y/n): ").lower() in ['y', 'yes']

    # Calculate discounts
    discount = 0
    if is_member:
        discount = subtotal * 0.10
        member_orders += 1

    subtotal_after_discount = subtotal - discount

    # Calculate shipping
    if is_member and subtotal >= 50:
        shipping = 0
    elif subtotal >= 75:
        shipping = 0
    else:
        shipping = 8.99

    # Calculate tax
    tax = subtotal_after_discount * 0.08

    # Calculate total
    order_total = subtotal_after_discount + tax + shipping

    # Track large orders
    if subtotal >= 100:
        large_orders += 1

    # Update totals
    total_revenue += order_total
    total_books_sold += books
    total_shipping += shipping
    total_tax += tax

    # Store for detailed report
    order_details.append({
        'number': order_num,
        'subtotal': subtotal,
        'books': books,
        'member': is_member,
        'discount': discount,
        'shipping': shipping,
        'tax': tax,
        'total': order_total
    })

    # Show order confirmation
    print(f"  ✓ Order total: ${order_total:.2f}")

# Generate report
print("\n" + "=" * 70)
print(" " * 25 + "SALES REPORT")
print("=" * 70)
print(f"Date: {report_date}")
print(f"Orders Processed: {num_orders}")
print("-" * 70)

# Summary statistics
print("\nREVENUE SUMMARY:")
print(f"  Total Revenue:          ${total_revenue:>12.2f}")
print(f"  Total Tax Collected:    ${total_tax:>12.2f}")
print(f"  Total Shipping:         ${total_shipping:>12.2f}")

# Calculate averages
avg_order_value = total_revenue / num_orders if num_orders > 0 else 0
avg_books_per_order = total_books_sold / num_orders if num_orders > 0 else 0

print(f"\nAVERAGES:")
print(f"  Average Order Value:    ${avg_order_value:>12.2f}")
print(f"  Average Books/Order:    {avg_books_per_order:>12.1f}")

# Customer insights
member_percentage = (member_orders / num_orders * 100) if num_orders > 0 else 0
large_order_percentage = (large_orders / num_orders * 100) if num_orders > 0 else 0

print(f"\nCUSTOMER INSIGHTS:")
print(f"  Total Books Sold:       {total_books_sold:>12}")
print(f"  Member Orders:          {member_orders:>12} ({member_percentage:.1f}%)")
print(f"  Large Orders ($100+):   {large_orders:>12} ({large_order_percentage:.1f}%)")

# Detailed order breakdown
print("\n" + "=" * 70)
print(" " * 23 + "ORDER BREAKDOWN")
print("=" * 70)
print(f"{'Order':<8} {'Books':<8} {'Member':<10} {'Subtotal':<12} {'Total':<12}")
print("-" * 70)

for order in order_details:
    member_status = "Yes" if order['member'] else "No"
    print(f"#{order['number']:<7} {order['books']:<8} {member_status:<10} "
          f"${order['subtotal']:<11.2f} ${order['total']:<11.2f}")

# Performance metrics
print("\n" + "=" * 70)
print(" " * 22 + "PERFORMANCE METRICS")
print("=" * 70)

# Calculate revenue goals
daily_goal = 1000.00
goal_percentage = (total_revenue / daily_goal * 100) if daily_goal > 0 else 0

if total_revenue >= daily_goal:
    print(f"✓ DAILY GOAL MET! ({goal_percentage:.1f}% of ${daily_goal:.2f} goal)")
else:
    shortfall = daily_goal - total_revenue
    print(f"✗ Goal not met. ${shortfall:.2f} short of ${daily_goal:.2f} goal ({goal_percentage:.1f}%)")

# Shipping efficiency
free_shipping_orders = sum(1 for order in order_details if order['shipping'] == 0)
free_shipping_rate = (free_shipping_orders / num_orders * 100) if num_orders > 0 else 0
print(f"\nShipping Analysis:")
print(f"  Orders with free shipping: {free_shipping_orders}/{num_orders} ({free_shipping_rate:.1f}%)")

# Recommendations
print("\n" + "=" * 70)
print(" " * 24 + "RECOMMENDATIONS")
print("=" * 70)

if member_percentage < 30:
    print("📊 Member orders are low. Consider promoting membership benefits!")

if avg_order_value < 50:
    print("📊 Average order value is below target. Consider upselling strategies!")

if large_order_percentage > 30:
    print("📊 High percentage of large orders! Consider bulk purchase incentives!")

if free_shipping_rate < 50:
    print("📊 Many orders paying shipping. Review free shipping threshold!")

print("\n" + "=" * 70)
print(" " * 22 + "END OF REPORT")
print("=" * 70)
