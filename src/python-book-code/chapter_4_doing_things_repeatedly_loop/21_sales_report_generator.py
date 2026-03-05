"""
Example 21 from Chapter 4: Doing Things Repeatedly - Loops
Python Programming Fundamentals by Rajesh Aadi

Example 21: Complex loop with nested conditionals and calculations
"""

from datetime import datetime

print("=" * 70)
print("                    BOOKISH CORNER")
print("                 Daily Sales Report Generator")
print("=" * 70)

current_date = "February 09, 2026"
num_orders = 3

print(f"\nReport Date: {current_date}")
print(f"Number of orders to process: {num_orders}\n")

print("=" * 70)
print("ENTERING ORDER DATA")
print("=" * 70)

orders = []
total_revenue = 0
total_tax = 0
total_shipping = 0
member_count = 0
large_orders = 0

for order_num in range(1, num_orders + 1):
    print(f"\nOrder #{order_num}")
    print("-" * 70)
    
    # Simulated order data
    if order_num == 1:
        subtotal, books, is_member = 85.50, 4, True
    elif order_num == 2:
        subtotal, books, is_member = 45.00, 2, False
    else:
        subtotal, books, is_member = 120.00, 6, True
    
    print(f"  Subtotal: ${subtotal:.2f}")
    print(f"  Number of books: {books}")
    print(f"  Member? (y/n): {'yes' if is_member else 'no'}")
    
    # Calculate order total
    tax = subtotal * 0.08
    shipping = 0 if subtotal >= 75 else 8.99
    
    if is_member:
        discount = subtotal * 0.10
        order_total = subtotal - discount + tax + shipping
        member_count += 1
    else:
        order_total = subtotal + tax + shipping
    
    if subtotal >= 100:
        large_orders += 1
    
    print(f"  ✓ Order total: ${order_total:.2f}")
    
    orders.append({
        'num': order_num,
        'subtotal': subtotal,
        'books': books,
        'member': is_member,
        'total': order_total,
        'tax': tax,
        'shipping': shipping
    })
    
    total_revenue += order_total
    total_tax += tax
    total_shipping += shipping

print("\n" + "=" * 70)
print("                         SALES REPORT")
print("=" * 70)
print(f"Date: {current_date}")
print(f"Orders Processed: {num_orders}")
print("-" * 70)

print("\nREVENUE SUMMARY:")
print(f"  Total Revenue:          ${total_revenue:>10.2f}")
print(f"  Total Tax Collected:    ${total_tax:>10.2f}")
print(f"  Total Shipping:         ${total_shipping:>10.2f}")

average_order = total_revenue / num_orders
total_books = sum(o['books'] for o in orders)
average_books = total_books / num_orders

print("\nAVERAGES:")
print(f"  Average Order Value:    ${average_order:>10.2f}")
print(f"  Average Books/Order:    {average_books:>10.1f}")

print("\nCUSTOMER INSIGHTS:")
print(f"  Total Books Sold:                  {total_books}")
member_pct = (member_count / num_orders) * 100
large_pct = (large_orders / num_orders) * 100
print(f"  Member Orders:                     {member_count} ({member_pct:.1f}%)")
print(f"  Large Orders ($100+):              {large_orders} ({large_pct:.1f}%)")

print("\n" + "=" * 70)
print("                       ORDER BREAKDOWN")
print("=" * 70)
print("Order    Books    Member     Subtotal     Total")
print("-" * 70)
for order in orders:
    member_str = "Yes" if order['member'] else "No"
    print(f"#{order['num']:<7} {order['books']:<7} {member_str:<10} ${order['subtotal']:<9.2f} ${order['total']:.2f}")

print("\n" + "=" * 70)
print("                      PERFORMANCE METRICS")
print("=" * 70)
revenue_goal = 1000.00
shortfall = revenue_goal - total_revenue
shortfall_pct = (shortfall / revenue_goal) * 100
print(f"✗ Goal not met. ${shortfall:.2f} short of ${revenue_goal:.2f} goal ({shortfall_pct:.1f}%)")

free_shipping_count = sum(1 for o in orders if o['shipping'] == 0)
free_shipping_pct = (free_shipping_count / num_orders) * 100
print(f"\nShipping Analysis:")
print(f"  Orders with free shipping: {free_shipping_count}/{num_orders} ({free_shipping_pct:.1f}%)")

print("\n" + "=" * 70)
print("                        RECOMMENDATIONS")
print("=" * 70)
print("📊 Member orders are low. Consider promoting membership benefits!")

print("\n" + "=" * 70)
print("                      END OF REPORT")
print("=" * 70)
