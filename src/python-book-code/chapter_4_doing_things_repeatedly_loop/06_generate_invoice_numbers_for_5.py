"""
Example 6 from Chapter 4: Doing Things Repeatedly - Loops
Python Programming Fundamentals by Rajesh Aadi

Generate Invoice Numbers For 5
"""

# Generate invoice numbers for 5 orders
print("Generating invoices...\n")

for invoice_num in range(1, 6):  # 1, 2, 3, 4, 5
    print(f"Invoice #{invoice_num:04d} created")

print("\nAll invoices generated!")
