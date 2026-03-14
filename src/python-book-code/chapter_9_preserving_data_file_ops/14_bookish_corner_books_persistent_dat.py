"""
Example 14 from Chapter 9: Preserving Data - File Operations
Python Programming Fundamentals by Rajesh Aadi

Bookish Corner Persistent Dat
"""

# Bookish Corner - Persistent Data System
# Version 9.0

import json
import csv
import os
from datetime import datetime

class DataManager:
    """Manages persistent data storage"""

    def __init__(self, data_dir="data"):
        """Initialize data manager"""
        self.data_dir = data_dir
        self.customers_file = os.path.join(data_dir, "customers.json")
        self.orders_file = os.path.join(data_dir, "orders.json")
        self.products_file = os.path.join(data_dir, "products.json")

        # Create data directory if it doesn't exist
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
            print(f"Created data directory: {data_dir}")

    def load_customers(self):
        """Load customers from JSON file"""
        try:
            with open(self.customers_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print("No customer file found, starting fresh")
            return {}
        except json.JSONDecodeError:
            print("Error reading customers file, starting fresh")
            return {}

    def save_customers(self, customers):
        """Save customers to JSON file"""
        try:
            with open(self.customers_file, "w") as file:
                json.dump(customers, file, indent=2)
            return True
        except Exception as e:
            print(f"Error saving customers: {e}")
            return False

    def load_orders(self):
        """Load orders from JSON file"""
        try:
            with open(self.orders_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("Error reading orders file")
            return []

    def save_orders(self, orders):
        """Save orders to JSON file"""
        try:
            with open(self.orders_file, "w") as file:
                json.dump(orders, file, indent=2)
            return True
        except Exception as e:
            print(f"Error saving orders: {e}")
            return False

    def export_customers_csv(self, filename="customers_export.csv"):
        """Export customers to CSV"""
        customers = self.load_customers()

        if not customers:
            print("No customers to export")
            return False

        try:
            filepath = os.path.join(self.data_dir, filename)
            with open(filepath, "w", newline="") as file:
                fieldnames = ["email", "name", "member_type", "points", "total_spent"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)

                writer.writeheader()

                for email, customer in customers.items():
                    writer.writerow({
                        "email": email,
                        "name": customer.get("name", ""),
                        "member_type": customer.get("member_type", "regular"),
                        "points": customer.get("points", 0),
                        "total_spent": customer.get("total_spent", 0.0)
                    })

            print(f"✓ Exported {len(customers)} customers to {filepath}")
            return True

        except Exception as e:
            print(f"Error exporting customers: {e}")
            return False

    def import_customers_csv(self, filename):
        """Import customers from CSV"""
        try:
            filepath = os.path.join(self.data_dir, filename)

            if not os.path.exists(filepath):
                print(f"File not found: {filepath}")
                return False

            customers = self.load_customers()

            with open(filepath, "r") as file:
                reader = csv.DictReader(file)

                count = 0
                for row in reader:
                    email = row.get("email")
                    if email and email not in customers:
                        customers[email] = {
                            "name": row.get("name", ""),
                            "member_type": row.get("member_type", "regular"),
                            "points": int(row.get("points", 0)),
                            "total_spent": float(row.get("total_spent", 0.0)),
                            "orders": [],
                            "join_date": datetime.now().strftime("%Y-%m-%d")
                        }
                        count += 1

            self.save_customers(customers)
            print(f"✓ Imported {count} new customers")
            return True

        except Exception as e:
            print(f"Error importing customers: {e}")
            return False

    def backup_data(self):
        """Create backup of all data files"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_dir = os.path.join(self.data_dir, f"backup_{timestamp}")

        try:
            os.makedirs(backup_dir)

            # Backup each file
            files = [self.customers_file, self.orders_file, self.products_file]
            backed_up = 0

            for file_path in files:
                if os.path.exists(file_path):
                    filename = os.path.basename(file_path)
                    backup_path = os.path.join(backup_dir, filename)

                    # Copy file
                    with open(file_path, "r") as src:
                        content = src.read()
                    with open(backup_path, "w") as dst:
                        dst.write(content)

                    backed_up += 1

            print(f"✓ Backed up {backed_up} files to {backup_dir}")
            return True

        except Exception as e:
            print(f"Error creating backup: {e}")
            return False

    def get_database_stats(self):
        """Get statistics about stored data"""
        stats = {
            "customers": 0,
            "orders": 0,
            "total_revenue": 0.0,
            "data_dir": self.data_dir
        }

        # Customer stats
        customers = self.load_customers()
        stats["customers"] = len(customers)

        for customer in customers.values():
            stats["total_revenue"] += customer.get("total_spent", 0.0)

        # Order stats
        orders = self.load_orders()
        stats["orders"] = len(orders)

        # File sizes
        if os.path.exists(self.customers_file):
            stats["customers_file_size"] = os.path.getsize(self.customers_file)

        if os.path.exists(self.orders_file):
            stats["orders_file_size"] = os.path.getsize(self.orders_file)

        return stats

def print_header(title):
    """Print formatted header"""
    print("\n" + "=" * 70)
    print(title.center(70))
    print("=" * 70)

def add_customer_demo(dm):
    """Demo: Add a customer"""
    print_header("ADD CUSTOMER")

    customers = dm.load_customers()

    name = input("Customer name: ")
    email = input("Email: ").lower().strip()

    if email in customers:
        print("Customer already exists!")
        return

    member_type = input("Member type (regular/member/premium): ").lower()
    if member_type not in ["regular", "member", "premium"]:
        member_type = "regular"

    customers[email] = {
        "name": name,
        "email": email,
        "member_type": member_type,
        "points": 0,
        "total_spent": 0.0,
        "orders": [],
        "join_date": datetime.now().strftime("%Y-%m-%d")
    }

    if dm.save_customers(customers):
        print(f"✓ Customer '{name}' added and saved!")
    else:
        print("✗ Error saving customer")

def list_customers_demo(dm):
    """Demo: List all customers"""
    print_header("CUSTOMER LIST")

    customers = dm.load_customers()

    if not customers:
        print("No customers found")
        return

    print(f"\n{'Email':<30} {'Name':<25} {'Type':<10} {'Points':<8}")
    print("-" * 70)

    for email, customer in customers.items():
        print(f"{email:<30} {customer['name']:<25} "
              f"{customer['member_type']:<10} {customer['points']:<8}")

    print(f"\nTotal customers: {len(customers)}")

def main():
    """Main program"""
    dm = DataManager()

    # Initialize with sample data if empty
    customers = dm.load_customers()
    if not customers:
        print("Initializing with sample data...")
        sample_customers = {
            "alice@email.com": {
                "name": "Alice Johnson",
                "email": "alice@email.com",
                "member_type": "premium",
                "points": 1250,
                "total_spent": 1250.00,
                "orders": [],
                "join_date": "2025-06-15"
            },
            "bob@email.com": {
                "name": "Bob Smith",
                "email": "bob@email.com",
                "member_type": "member",
                "points": 450,
                "total_spent": 450.00,
                "orders": [],
                "join_date": "2025-09-20"
            }
        }
        dm.save_customers(sample_customers)

    while True:
        print_header("BOOKISH CORNER - DATA MANAGEMENT")
        print("\n1. Add Customer")
        print("2. List Customers")
        print("3. Export Customers to CSV")
        print("4. Import Customers from CSV")
        print("5. Database Statistics")
        print("6. Backup Data")
        print("7. Exit")

        choice = input("\nSelect option (1-7): ")

        if choice == "1":
            add_customer_demo(dm)

        elif choice == "2":
            list_customers_demo(dm)

        elif choice == "3":
            filename = input("Export filename (default: customers_export.csv): ")
            if not filename:
                filename = "customers_export.csv"
            dm.export_customers_csv(filename)

        elif choice == "4":
            filename = input("Import filename: ")
            dm.import_customers_csv(filename)

        elif choice == "5":
            print_header("DATABASE STATISTICS")
            stats = dm.get_database_stats()

            print(f"\nData Directory: {stats['data_dir']}")
            print(f"Total Customers: {stats['customers']}")
            print(f"Total Orders: {stats['orders']}")
            print(f"Total Revenue: ${stats['total_revenue']:,.2f}")

            if "customers_file_size" in stats:
                size_kb = stats["customers_file_size"] / 1024
                print(f"Customers File Size: {size_kb:.2f} KB")

        elif choice == "6":
            dm.backup_data()

        elif choice == "7":
            print("\nData saved. Goodbye!")
            break

        else:
            print("\nInvalid option")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
