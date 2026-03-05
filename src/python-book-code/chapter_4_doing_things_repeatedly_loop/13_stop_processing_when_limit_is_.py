"""
Example 13 from Chapter 4: Doing Things Repeatedly - Loops
Python Programming Fundamentals by Rajesh Aadi

Stop Processing When Limit Is 
"""

# Stop processing when limit is reached
print("Processing orders until daily limit...\n")

daily_limit = 1000.00
total_processed = 0
order_num = 0

while True:
    order_num += 1
    amount = float(input(f"Order #{order_num} amount (or 0 to finish): $"))

    if amount == 0:
        print("No more orders.")
        break

    if total_processed + amount > daily_limit:
        print(f"\n⚠️  Daily limit would be exceeded!")
        print(f"Cannot process order #{order_num}")
        break

    total_processed += amount
    remaining = daily_limit - total_processed
    print(f"✓ Order processed. Remaining capacity: ${remaining:.2f}\n")

print(f"\nTotal processed: ${total_processed:.2f}")
