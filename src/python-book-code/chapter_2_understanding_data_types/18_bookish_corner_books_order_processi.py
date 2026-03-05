"""
Example 18 from Chapter 2: Understanding Data - Types and Operations
Python Programming Fundamentals by Rajesh Aadi

Bookish Corner Order Processi
"""

# Bookish Corner - Order Processing System
# Version 2.0

print("=" * 60)
print(" " * 15 + "BOOKISH CORNER")
print(" " * 12 + "Order Processing System")
print("=" * 60)

# Customer Information
customer_name = input("\nCustomer Name: ")
is_member = input("Is customer a member? (yes/no): ").lower() == "yes"

# Order Details
print("\n" + "-" * 60)
print("ORDER DETAILS")
print("-" * 60)

# Book 1
book1_title = input("Book 1 Title: ")
book1_qty = int(input("Quantity: "))
book1_price = float(input("Price per book: $"))

# Book 2
book2_title = input("\nBook 2 Title: ")
book2_qty = int(input("Quantity: "))
book2_price = float(input("Price per book: $"))

# Calculations
subtotal_book1 = book1_qty * book1_price
subtotal_book2 = book2_qty * book2_price
subtotal = subtotal_book1 + subtotal_book2

# Discount for members
discount_rate = 0.10 if is_member else 0.00
discount_amount = subtotal * discount_rate

# Tax calculation
tax_rate = 0.08
subtotal_after_discount = subtotal - discount_amount
tax_amount = subtotal_after_discount * tax_rate

# Final total
total = subtotal_after_discount + tax_amount

# Generate Order Number
import random
order_number = random.randint(10000, 99999)

# Display Receipt
print("\n" + "=" * 60)
print(" " * 20 + "ORDER RECEIPT")
print("=" * 60)
print(f"Order Number: #{order_number:05d}")
print(f"Customer: {customer_name}")
print(f"Member: {'Yes' if is_member else 'No'}")
print("-" * 60)

# Item details
print(f"{book1_title[:30]:<30} x{book1_qty:>3}   ${subtotal_book1:>8.2f}")
print(f"{book2_title[:30]:<30} x{book2_qty:>3}   ${subtotal_book2:>8.2f}")

print("-" * 60)
print(f"{'Subtotal:':<40} ${subtotal:>10.2f}")

if discount_amount > 0:
    print(f"{'Member Discount (10%):':<40} -${discount_amount:>9.2f}")
    print(f"{'Subtotal after discount:':<40} ${subtotal_after_discount:>10.2f}")

print(f"{'Sales Tax (8%):':<40} ${tax_amount:>10.2f}")
print("=" * 60)
print(f"{'TOTAL:':<40} ${total:>10.2f}")
print("=" * 60)

print(f"\n{'Thank you for shopping at Bookish Corner!':^60}")
print(f"{'Visit us at www.bookishcorner.com':^60}\n")
