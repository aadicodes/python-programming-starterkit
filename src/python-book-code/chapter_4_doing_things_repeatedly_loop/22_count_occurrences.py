"""
Example 22 from Chapter 4: Doing Things Repeatedly - Loops
Python Programming Fundamentals by Rajesh Aadi

Count Occurrences
"""

# Count occurrences
defective_books = 0
total_books = 100

for book in range(total_books):
    # Simulate quality check (random for demo)
    if random.random() < 0.05:  # 5% defect rate
        defective_books += 1

defect_rate = (defective_books / total_books) * 100
print(f"Defective books: {defective_books} ({defect_rate:.1f}%)")
