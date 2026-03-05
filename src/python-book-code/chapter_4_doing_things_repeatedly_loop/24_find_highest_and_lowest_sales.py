"""
Example 24 from Chapter 4: Doing Things Repeatedly - Loops
Python Programming Fundamentals by Rajesh Aadi

Find Highest And Lowest Sales
"""

# Find highest and lowest sales
print("Enter daily sales for the week:")

max_sales = 0
min_sales = float('inf')  # Start with infinity
best_day = ""
worst_day = ""

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for day in days:
    sales = float(input(f"{day}: $"))

    if sales > max_sales:
        max_sales = sales
        best_day = day

    if sales < min_sales:
        min_sales = sales
        worst_day = day

print(f"\nBest day: {best_day} (${max_sales:.2f})")
print(f"Worst day: {worst_day} (${min_sales:.2f})")
