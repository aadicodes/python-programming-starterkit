"""
Example 18 from Chapter 10: Handling Problems - Error Handling and Exceptions
Python Programming Fundamentals by Rajesh Aadi

Bookish Corner Robust Order P
"""

# Bookish Corner - Robust Order Processing System
# Version 10.0

import json
from datetime import datetime

# Custom Exceptions
class OrderError(Exception):
    """Base exception for order processing"""
    pass

class InvalidOrderDataError(OrderError):
    """Invalid order data"""
    pass

class InsufficientStockError(OrderError):
    """Not enough stock"""
    pass

class PaymentError(OrderError):
    """Payment processing failed"""
    pass

def print_header(title):
    """Print formatted header"""
    print("\n" + "=" * 70)
    print(title.center(70))
    print("=" * 70)

class OrderValidator:
    """Validates order data"""

    @staticmethod
    def validate_customer_email(email):
        """Validate customer email"""
        if not isinstance(email, str):
            raise InvalidOrderDataError("Email must be a string")

        email = email.strip().lower()

        if not email:
            raise InvalidOrderDataError("Email cannot be empty")

        if "@" not in email or "." not in email:
            raise InvalidOrderDataError(f"Invalid email format: {email}")

        return email

    @staticmethod
    def validate_item(item):
        """Validate order item"""
        required_fields = ["name", "price", "quantity"]

        for field in required_fields:
            if field not in item:
                raise InvalidOrderDataError(f"Missing required field: {field}")

        # Validate price
        try:
            price = float(item["price"])
            if price <= 0:
                raise InvalidOrderDataError(f"Price must be positive: {price}")
        except (ValueError, TypeError):
            raise InvalidOrderDataError(f"Invalid price: {item['price']}")

        # Validate quantity
        try:
            quantity = int(item["quantity"])
            if quantity <= 0:
                raise InvalidOrderDataError(f"Quantity must be positive: {quantity}")
        except (ValueError, TypeError):
            raise InvalidOrderDataError(f"Invalid quantity: {item['quantity']}")

        return {
            "name": str(item["name"]).strip(),
            "price": round(price, 2),
            "quantity": quantity
        }

    @staticmethod
    def validate_order(order_data):
        """Validate complete order"""
        if not isinstance(order_data, dict):
            raise InvalidOrderDataError("Order must be a dictionary")

        # Validate customer email
        if "customer_email" not in order_data:
            raise InvalidOrderDataError("Missing customer email")

        email = OrderValidator.validate_customer_email(order_data["customer_email"])

        # Validate items
        if "items" not in order_data:
            raise InvalidOrderDataError("Order must contain items")

        if not isinstance(order_data["items"], list):
            raise InvalidOrderDataError("Items must be a list")

        if len(order_data["items"]) == 0:
            raise InvalidOrderDataError("Order must contain at least one item")

        validated_items = []
        for i, item in enumerate(order_data["items"]):
            try:
                validated_item = OrderValidator.validate_item(item)
                validated_items.append(validated_item)
            except InvalidOrderDataError as e:
                raise InvalidOrderDataError(f"Item {i+1}: {e}")

        return {
            "customer_email": email,
            "items": validated_items
        }

class OrderProcessor:
    """Processes orders with error handling"""

    def __init__(self):
        self.inventory = {
            "Python Programming": {"stock": 25, "price": 29.99},
            "JavaScript Basics": {"stock": 15, "price": 24.99},
            "Data Science": {"stock": 8, "price": 39.99}
        }

    def check_stock(self, item_name, quantity):
        """Check if enough stock available"""
        if item_name not in self.inventory:
            raise InsufficientStockError(f"Product not found: {item_name}")

        available = self.inventory[item_name]["stock"]

        if quantity > available:
            raise InsufficientStockError(
                f"Only {available} units of '{item_name}' available (requested {quantity})"
            )

        return True

    def process_payment(self, amount):
        """Simulate payment processing"""
        if amount <= 0:
            raise PaymentError("Payment amount must be positive")

        if amount > 10000:
            raise PaymentError("Payment amount exceeds limit")

        # Simulate random payment failure (10% chance)
        import random
        if random.random() < 0.1:
            raise PaymentError("Payment gateway timeout")

        return True

    def calculate_total(self, items):
        """Calculate order total"""
        subtotal = 0

        for item in items:
            subtotal += item["price"] * item["quantity"]

        tax = subtotal * 0.08
        total = subtotal + tax

        return {
            "subtotal": round(subtotal, 2),
            "tax": round(tax, 2),
            "total": round(total, 2)
        }

    def update_inventory(self, items):
        """Update inventory after successful order"""
        for item in items:
            name = item["name"]
            quantity = item["quantity"]

            if name in self.inventory:
                self.inventory[name]["stock"] -= quantity

    def process_order(self, order_data):
        """
        Process complete order with comprehensive error handling

        Returns:
            dict: Order result with success status and details
        """
        result = {
            "success": False,
            "order_id": None,
            "total": 0,
            "error": None,
            "timestamp": datetime.now().isoformat()
        }

        try:
            # Step 1: Validate order data
            print("Validating order data...")
            validated_order = OrderValidator.validate_order(order_data)

            # Step 2: Check stock for all items
            print("Checking inventory...")
            for item in validated_order["items"]:
                self.check_stock(item["name"], item["quantity"])

            # Step 3: Calculate total
            print("Calculating total...")
            totals = self.calculate_total(validated_order["items"])
            result["total"] = totals["total"]

            # Step 4: Process payment
            print(f"Processing payment of ${totals['total']:.2f}...")
            self.process_payment(totals["total"])

            # Step 5: Update inventory
            print("Updating inventory...")
            self.update_inventory(validated_order["items"])

            # Step 6: Generate order ID
            import random
            order_id = f"ORD-{random.randint(10000, 99999)}"

            # Success!
            result["success"] = True
            result["order_id"] = order_id
            result["customer_email"] = validated_order["customer_email"]
            result["items"] = validated_order["items"]
            result["totals"] = totals

            print(f"\n✓ Order {order_id} processed successfully!")

        except InvalidOrderDataError as e:
            result["error"] = f"Invalid order data: {e}"
            print(f"\n✗ Order validation failed: {e}")

        except InsufficientStockError as e:
            result["error"] = f"Stock error: {e}"
            print(f"\n✗ Insufficient stock: {e}")

        except PaymentError as e:
            result["error"] = f"Payment failed: {e}"
            print(f"\n✗ Payment error: {e}")

        except Exception as e:
            result["error"] = f"Unexpected error: {e}"
            print(f"\n✗ Unexpected error: {e}")
            import traceback
            traceback.print_exc()

        finally:
            # Always log the attempt
            print(f"\nOrder processing completed at {result['timestamp']}")

        return result

def main():
    """Main program"""
    processor = OrderProcessor()

    while True:
        print_header("BOOKISH CORNER - ORDER PROCESSING")
        print("\n1. Process Valid Order")
        print("2. Process Order with Invalid Data")
        print("3. Process Order with Insufficient Stock")
        print("4. View Inventory")
        print("5. Process Custom Order")
        print("6. Exit")

        choice = input("\nSelect option (1-6): ")

        if choice == "1":
            # Valid order
            order = {
                "customer_email": "alice@email.com",
                "items": [
                    {"name": "Python Programming", "price": 29.99, "quantity": 2},
                    {"name": "JavaScript Basics", "price": 24.99, "quantity": 1}
                ]
            }
            result = processor.process_order(order)

        elif choice == "2":
            # Invalid data
            order = {
                "customer_email": "invalid.email",  # No @
                "items": [
                    {"name": "Python Programming", "price": "invalid", "quantity": 2}
                ]
            }
            result = processor.process_order(order)

        elif choice == "3":
            # Insufficient stock
            order = {
                "customer_email": "alice@email.com",
                "items": [
                    {"name": "Python Programming", "price": 29.99, "quantity": 100}  # Too many
                ]
            }
            result = processor.process_order(order)

        elif choice == "4":
            print_header("CURRENT INVENTORY")
            print(f"\n{'Product':<30} {'Stock':<10} {'Price':<10}")
            print("-" * 50)
            for name, info in processor.inventory.items():
                print(f"{name:<30} {info['stock']:<10} ${info['price']:<9.2f}")

        elif choice == "5":
            # Custom order
            print_header("ENTER CUSTOM ORDER")

            try:
                email = input("Customer email: ")

                items = []
                while True:
                    name = input("\nProduct name (or 'done'): ")
                    if name.lower() == 'done':
                        if items:
                            break
                        print("Add at least one item")
                        continue

                    price = input("Price: $")
                    quantity = input("Quantity: ")

                    items.append({
                        "name": name,
                        "price": price,
                        "quantity": quantity
                    })

                order = {
                    "customer_email": email,
                    "items": items
                }

                result = processor.process_order(order)

            except KeyboardInterrupt:
                print("\n\nOrder cancelled")

        elif choice == "6":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid option")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
