"""
Example 16 from Chapter 8: Working with Text - String Manipulation
Python Programming Fundamentals by Rajesh Aadi

Parse Csv Line
"""

def parse_csv_line(line):
    """Parse CSV line into fields"""
    return [field.strip() for field in line.split(",")]

# Sample CSV data
csv_data = """Name,Email,Member Type,Points
Alice Johnson,alice@email.com,premium,1250
Bob Smith,bob@email.com,member,450
Charlie Davis,charlie@email.com,regular,0"""

lines = csv_data.split("\n")
header = parse_csv_line(lines[0])

customers = []
for line in lines[1:]:
    fields = parse_csv_line(line)
    customer = dict(zip(header, fields))
    customers.append(customer)

# Display
for customer in customers:
    print(f"{customer['Name']}: {customer['Points']} points")
