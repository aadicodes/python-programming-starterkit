"""
Example 7 from Chapter 4: Doing Things Repeatedly - Loops
Python Programming Fundamentals by Rajesh Aadi

Example 07: For loop with formatted output
"""

print("Generating invoices...\n")

num_invoices = 5

for invoice_num in range(1, num_invoices + 1):
    invoice_id = f"{invoice_num:04d}"
    print(f"Invoice #{invoice_id} created")

print(f"\nAll {num_invoices} invoices generated!")
