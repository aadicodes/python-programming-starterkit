"""
Example 17 from Chapter 4: Doing Things Repeatedly - Loops
Python Programming Fundamentals by Rajesh Aadi

Process Orders For Multiple Cu
"""

# Process orders for multiple customers
customers = 3
books_per_order = 4

print("Bookish Corner - Bulk Order Processing\n")

grand_total = 0

for customer_num in range(1, customers + 1):
    print(f"Customer #{customer_num} Order:")
    print("-" * 40)

    customer_total = 0

    for book_num in range(1, books_per_order + 1):
        price = float(input(f"  Book {book_num} price: $"))
        customer_total += price

    print(f"  Customer #{customer_num} Total: ${customer_total:.2f}\n")
    grand_total += customer_total

print("=" * 40)
print(f"Grand Total (all customers): ${grand_total:.2f}")
print("=" * 40)
