"""
Example 16 from Chapter 3: Making Decisions - Conditional Statements
Python Programming Fundamentals by Rajesh Aadi

Bookish Corner Customer Eligi
"""

# Bookish Corner - Customer Eligibility Checker
# Version 3.0

print("=" * 60)
print(" " * 15 + "BOOKISH CORNER")
print(" " * 12 + "Eligibility Checker")
print("=" * 60)

# Customer Information
print("\nCUSTOMER INFORMATION")
print("-" * 60)

customer_name = input("Customer name: ")
membership_type = input("Membership type (regular/member/premium): ").lower()

# Validate membership type
if membership_type not in ["regular", "member", "premium"]:
    print("Invalid membership type. Defaulting to 'regular'")
    membership_type = "regular"

is_first_order = input("Is this their first order? (yes/no): ").lower()
is_first_order = is_first_order in ["yes", "y"]

# Order Information
print("\nORDER INFORMATION")
print("-" * 60)

order_total_str = input("Order total: $")
if order_total_str.replace(".", "").isdigit():
    order_total = float(order_total_str)
else:
    print("Invalid amount. Setting to $0")
    order_total = 0

books_quantity_str = input("Number of books: ")
if books_quantity_str.isdigit():
    books_quantity = int(books_quantity_str)
else:
    print("Invalid quantity. Setting to 0")
    books_quantity = 0

# Location for shipping
location = input("Shipping location (local/regional/remote): ").lower()
if location not in ["local", "regional", "remote"]:
    print("Invalid location. Defaulting to 'regional'")
    location = "regional"

# Calculate Benefits
print("\n" + "=" * 60)
print(" " * 18 + "ELIGIBILITY RESULTS")
print("=" * 60)
print(f"Customer: {customer_name}")
print(f"Membership: {membership_type.title()}")
print(f"Order Total: ${order_total:.2f}")
print(f"Books Ordered: {books_quantity}")
print("-" * 60)

# Determine discount
discount_rate = 0
discount_reason = ""

if membership_type == "premium":
    discount_rate = 0.15
    discount_reason = "Premium membership"
elif membership_type == "member":
    discount_rate = 0.10
    discount_reason = "Standard membership"
elif order_total >= 150:
    discount_rate = 0.05
    discount_reason = "Large order bonus"

# Bulk order bonus
if books_quantity >= 10:
    discount_rate += 0.05
    if discount_reason:
        discount_reason += " + Bulk order"
    else:
        discount_reason = "Bulk order bonus"

# First-time customer bonus
if is_first_order and discount_rate < 0.10:
    discount_rate = 0.10
    discount_reason = "First-time customer welcome"

# Calculate discount amount
discount_amount = order_total * discount_rate
subtotal_after_discount = order_total - discount_amount

# Display discount info
if discount_rate > 0:
    print(f"✓ DISCOUNT ELIGIBLE: {discount_reason}")
    print(f"  Rate: {discount_rate * 100:.0f}%")
    print(f"  Amount: ${discount_amount:.2f}")
else:
    print("✗ No discount available")

# Determine shipping
print()
shipping_cost = 0
free_shipping = False

if is_first_order:
    free_shipping = True
    shipping_reason = "First-time customer"
elif membership_type in ["member", "premium"] and order_total >= 50:
    free_shipping = True
    shipping_reason = "Member benefit"
elif order_total >= 75:
    free_shipping = True
    shipping_reason = "Minimum order met"

if free_shipping:
    shipping_cost = 0
    print(f"✓ FREE SHIPPING: {shipping_reason}")
else:
    if location == "local":
        shipping_cost = 5.99
    elif location == "regional":
        shipping_cost = 8.99
    else:  # remote
        shipping_cost = 12.99
    print(f"✗ Shipping cost: ${shipping_cost:.2f} ({location})")

# Same-day delivery eligibility
print()
if membership_type == "premium" and location == "local" and order_total >= 50:
    print("✓ SAME-DAY DELIVERY AVAILABLE")
elif location == "local" and order_total >= 100:
    print("✓ SAME-DAY DELIVERY AVAILABLE")
else:
    print("✗ Same-day delivery not available")

# Gift wrapping
print()
if order_total >= 30:
    print("✓ FREE GIFT WRAPPING AVAILABLE")
else:
    print("✗ Gift wrapping ($4.99) - Not included")

# Loyalty points
print()
points_earned = 0
if membership_type == "premium":
    points_earned = int(subtotal_after_discount * 2)  # 2 points per dollar
elif membership_type == "member":
    points_earned = int(subtotal_after_discount)  # 1 point per dollar

if points_earned > 0:
    print(f"✓ LOYALTY POINTS: {points_earned} points will be added")
else:
    print("✗ Not enrolled in loyalty program")

# Final calculation
tax_rate = 0.08
tax_amount = subtotal_after_discount * tax_rate
final_total = subtotal_after_discount + tax_amount + shipping_cost

# Summary
print("\n" + "=" * 60)
print(" " * 20 + "ORDER SUMMARY")
print("=" * 60)
print(f"{'Subtotal:':<30} ${order_total:>10.2f}")

if discount_amount > 0:
    print(f"{'Discount:':<30} -${discount_amount:>9.2f}")
    print(f"{'Subtotal after discount:':<30} ${subtotal_after_discount:>10.2f}")

print(f"{'Tax (8%):':<30} ${tax_amount:>10.2f}")
print(f"{'Shipping:':<30} ${shipping_cost:>10.2f}")
print("=" * 60)
print(f"{'FINAL TOTAL:':<30} ${final_total:>10.2f}")
print("=" * 60)

# Upsell recommendations
print("\n" + "=" * 60)
print(" " * 17 + "RECOMMENDATIONS")
print("=" * 60)

if not is_first_order and membership_type == "regular":
    savings_if_member = order_total * 0.10
    print(f"💡 Become a member and save ${savings_if_member:.2f} on this order!")

if books_quantity >= 5 and books_quantity < 10:
    additional_books = 10 - books_quantity
    additional_discount = order_total * 0.05
    print(f"💡 Add {additional_books} more books for an extra 5% off (${additional_discount:.2f} savings)!")

if not free_shipping and order_total >= 60 and order_total < 75:
    amount_needed = 75 - order_total
    print(f"💡 Add ${amount_needed:.2f} more to your order for free shipping!")

print()
