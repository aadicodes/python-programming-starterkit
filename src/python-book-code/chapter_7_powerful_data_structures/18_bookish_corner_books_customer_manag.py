"""
Example 18 from Chapter 7: Powerful Data Structures - Dictionaries and Sets
Python Programming Fundamentals by Rajesh Aadi

Bookish Corner Customer Manag
"""

# Bookish Corner - Customer Management System
# Version 7.0

import random
from datetime import datetime, timedelta

def print_header(title):
    """Print formatted header"""
    print("\n" + "=" * 70)
    print(title.center(70))
    print("=" * 70)

def create_customer(name, email, member_type="regular"):
    """Create a new customer dictionary"""
    return {
        "name": name,
        "email": email,
        "member_type": member_type,
        "points": 0,
        "join_date": datetime.now().strftime("%Y-%m-%d"),
        "orders": [],
        "total_spent": 0.0,
        "preferences": {
            "newsletter": True,
            "notifications": True,
            "categories": set()
        },
        "address": {}
    }

def add_customer(database):
    """Add a new customer to the database"""
    print_header("ADD NEW CUSTOMER")

    name = input("Customer name: ")

    # Validate email
    while True:
        email = input("Email address: ").lower().strip()
        if "@" in email and "." in email:
            if email in database:
                print("Email already exists in database!")
                continue
            break
        print("Invalid email format")

    # Member type
    print("\nMember Types:")
    print("  1. Regular (no fee)")
    print("  2. Member ($50/year - 10% discount)")
    print("  3. Premium ($100/year - 15% discount)")

    member_choice = input("Select type (1-3): ")
    member_types = {"1": "regular", "2": "member", "3": "premium"}
    member_type = member_types.get(member_choice, "regular")

    # Create customer
    customer = create_customer(name, email, member_type)

    # Optional address
    if input("Add address? (yes/no): ").lower() in ["yes", "y"]:
        customer["address"] = {
            "street": input("  Street: "),
            "city": input("  City: "),
            "state": input("  State: "),
            "zip": input("  ZIP: ")
        }

    # Add to database
    database[email] = customer
    print(f"\n✓ Customer '{name}' added successfully!")
    return email

def display_customer(customer, email):
    """Display customer details"""
    print("\n" + "-" * 70)
    print(f"Name: {customer['name']}")
    print(f"Email: {email}")
    print(f"Member Type: {customer['member_type'].title()}")
    print(f"Points: {customer['points']:,}")
    print(f"Total Spent: ${customer['total_spent']:,.2f}")
    print(f"Member Since: {customer['join_date']}")
    print(f"Total Orders: {len(customer['orders'])}")

    if customer['address']:
        addr = customer['address']
        print(f"Address: {addr.get('street', '')}, {addr.get('city', '')} "
              f"{addr.get('state', '')} {addr.get('zip', '')}")

    if customer['preferences']['categories']:
        cats = ', '.join(customer['preferences']['categories'])
        print(f"Favorite Categories: {cats}")

    print("-" * 70)

def search_customers(database):
    """Search for customers"""
    print_header("SEARCH CUSTOMERS")

    query = input("Search by name or email: ").lower()

    results = []
    for email, customer in database.items():
        if (query in customer['name'].lower() or
            query in email.lower()):
            results.append((email, customer))

    if results:
        print(f"\nFound {len(results)} customer(s):")
        for email, customer in results:
            display_customer(customer, email)
    else:
        print(f"\nNo customers found matching '{query}'")

def add_order(database):
    """Add an order to a customer"""
    print_header("ADD ORDER")

    email = input("Customer email: ").lower().strip()

    if email not in database:
        print("Customer not found!")
        return

    customer = database[email]
    print(f"\nCustomer: {customer['name']}")

    # Get order details
    while True:
        try:
            amount = float(input("Order amount: $"))
            if amount > 0:
                break
        except ValueError:
            pass
        print("Invalid amount")

    # Create order
    order = {
        "order_id": random.randint(10000, 99999),
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "amount": amount,
        "items": []
    }

    # Add items
    print("\nAdd order items (or 'done' to finish):")
    while True:
        item = input("  Item name: ")
        if item.lower() == 'done':
            if len(order['items']) == 0:
                print("  Add at least one item")
                continue
            break

        category = input("  Category: ")
        order['items'].append({"name": item, "category": category})

        # Track customer preferences
        customer['preferences']['categories'].add(category)

    # Calculate points
    points_earned = int(amount)
    if customer['member_type'] == "premium":
        points_earned *= 2

    # Update customer
    customer['orders'].append(order)
    customer['total_spent'] += amount
    customer['points'] += points_earned

    print(f"\n✓ Order #{order['order_id']} added successfully!")
    print(f"  Points earned: {points_earned}")
    print(f"  Total points: {customer['points']}")

def customer_statistics(database):
    """Display customer statistics"""
    print_header("CUSTOMER STATISTICS")

    if not database:
        print("\nNo customers in database")
        return

    total_customers = len(database)
    member_types = {"regular": 0, "member": 0, "premium": 0}
    total_revenue = 0
    total_orders = 0
    all_categories = set()

    for customer in database.values():
        member_types[customer['member_type']] += 1
        total_revenue += customer['total_spent']
        total_orders += len(customer['orders'])
        all_categories.update(customer['preferences']['categories'])

    print(f"\nTotal Customers: {total_customers}")
    print("\nMember Distribution:")
    for mtype, count in member_types.items():
        percentage = (count / total_customers * 100) if total_customers > 0 else 0
        print(f"  {mtype.title()}: {count} ({percentage:.1f}%)")

    print(f"\nRevenue:")
    print(f"  Total Revenue: ${total_revenue:,.2f}")
    print(f"  Average per Customer: ${total_revenue/total_customers:,.2f}")

    print(f"\nOrders:")
    print(f"  Total Orders: {total_orders}")
    if total_customers > 0:
        print(f"  Average per Customer: {total_orders/total_customers:.1f}")

    print(f"\nCategories:")
    print(f"  Unique Categories: {len(all_categories)}")
    if all_categories:
        print(f"  Categories: {', '.join(sorted(all_categories))}")

def top_customers(database, limit=10):
    """Display top customers by spending"""
    print_header(f"TOP {limit} CUSTOMERS BY SPENDING")

    if not database:
        print("\nNo customers in database")
        return

    # Sort customers by total spent
    sorted_customers = sorted(
        database.items(),
        key=lambda x: x[1]['total_spent'],
        reverse=True
    )

    print(f"\n{'Rank':<6} {'Name':<25} {'Email':<30} {'Total Spent':<15}")
    print("-" * 70)

    for rank, (email, customer) in enumerate(sorted_customers[:limit], 1):
        medal = "🥇" if rank == 1 else "🥈" if rank == 2 else "🥉" if rank == 3 else "  "
        print(f"{medal} {rank:<3} {customer['name']:<25} {email:<30} "
              f"${customer['total_spent']:>12,.2f}")

def customers_by_category(database):
    """Show customers grouped by favorite categories"""
    print_header("CUSTOMERS BY CATEGORY")

    category_customers = {}

    for email, customer in database.items():
        for category in customer['preferences']['categories']:
            if category not in category_customers:
                category_customers[category] = []
            category_customers[category].append(customer['name'])

    if not category_customers:
        print("\nNo category data available")
        return

    for category in sorted(category_customers.keys()):
        customers = category_customers[category]
        print(f"\n{category} ({len(customers)} customers):")
        for name in sorted(customers):
            print(f"  • {name}")

def export_emails(database):
    """Export customer emails for marketing"""
    print_header("EXPORT EMAIL LIST")

    # Filter options
    print("\nExport Options:")
    print("  1. All customers")
    print("  2. Newsletter subscribers only")
    print("  3. By member type")
    print("  4. By category interest")

    choice = input("\nSelect option (1-4): ")

    emails = set()

    if choice == "1":
        emails = set(database.keys())

    elif choice == "2":
        emails = {email for email, customer in database.items()
                 if customer['preferences']['newsletter']}

    elif choice == "3":
        member_type = input("Member type (regular/member/premium): ").lower()
        emails = {email for email, customer in database.items()
                 if customer['member_type'] == member_type}

    elif choice == "4":
        category = input("Category: ")
        emails = {email for email, customer in database.items()
                 if category in customer['preferences']['categories']}

    if emails:
        print(f"\n✓ {len(emails)} email(s) exported:")
        for email in sorted(emails):
            print(f"  {email}")
    else:
        print("\nNo emails match criteria")

def main():
    """Main program"""
    # Sample customer database
    database = {
        "alice@email.com": {
            "name": "Alice Johnson",
            "email": "alice@email.com",
            "member_type": "premium",
            "points": 2500,
            "join_date": "2025-06-15",
            "total_spent": 1250.00,
            "orders": [
                {"order_id": 10001, "date": "2025-12-01", "amount": 450.00},
                {"order_id": 10025, "date": "2026-01-15", "amount": 800.00}
            ],
            "preferences": {
                "newsletter": True,
                "notifications": True,
                "categories": {"Programming", "Data Science"}
            },
            "address": {
                "street": "123 Main St",
                "city": "Boston",
                "state": "MA",
                "zip": "02101"
            }
        },
        "bob@email.com": {
            "name": "Bob Smith",
            "email": "bob@email.com",
            "member_type": "member",
            "points": 450,
            "join_date": "2025-09-20",
            "total_spent": 450.00,
            "orders": [
                {"order_id": 10015, "date": "2025-11-20", "amount": 450.00}
            ],
            "preferences": {
                "newsletter": True,
                "notifications": False,
                "categories": {"Business", "Programming"}
            },
            "address": {}
        }
    }

    while True:
        print_header("BOOKISH CORNER - CUSTOMER MANAGEMENT")
        print("\n1. Add Customer")
        print("2. Search Customers")
        print("3. Add Order")
        print("4. Customer Statistics")
        print("5. Top Customers")
        print("6. Customers by Category")
        print("7. Export Email List")
        print("8. Exit")

        choice = input("\nSelect option (1-8): ")

        if choice == "1":
            add_customer(database)
        elif choice == "2":
            search_customers(database)
        elif choice == "3":
            add_order(database)
        elif choice == "4":
            customer_statistics(database)
        elif choice == "5":
            limit = input("How many customers? (default 10): ")
            limit = int(limit) if limit.isdigit() else 10
            top_customers(database, limit)
        elif choice == "6":
            customers_by_category(database)
        elif choice == "7":
            export_emails(database)
        elif choice == "8":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid option")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
