"""
Example 13 from Chapter 11: Building Systems - Object-Oriented Programming
Python Programming Fundamentals by Rajesh Aadi

Version 110
"""

# Bookish Corner - Object-Oriented E-Commerce System
# Version 11.0

from datetime import datetime
import random

class Product:
    """Represents a product in the catalog"""

    def __init__(self, product_id, title, price, stock=0, category=""):
        self.product_id = product_id
        self.title = title
        self._price = 0
        self.price = price
        self.stock = stock
        self.category = category

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = round(value, 2)

    def is_available(self):
        """Check if product is in stock"""
        return self.stock > 0

    def reduce_stock(self, quantity):
        """Reduce stock by quantity"""
        if quantity > self.stock:
            raise ValueError(f"Only {self.stock} available")
        self.stock -= quantity

    def add_stock(self, quantity):
        """Add stock"""
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        self.stock += quantity

    def __str__(self):
        return f"{self.title} - ${self.price} ({self.stock} in stock)"

    def __repr__(self):
        return f"Product({self.product_id}, '{self.title}', {self.price}, {self.stock})"


class Person:
    """Base class for people in the system"""

    def __init__(self, name, email):
        self.name = name
        self.email = self._validate_email(email)

    def _validate_email(self, email):
        """Validate email format"""
        email = email.strip().lower()
        if "@" not in email or "." not in email:
            raise ValueError(f"Invalid email: {email}")
        return email

    def send_email(self, subject, message):
        """Send email"""
        print(f"\nEmail to: {self.email}")
        print(f"Subject: {subject}")
        print(f"Message: {message}")
        return True


class Customer(Person):
    """Represents a customer"""

    def __init__(self, name, email, member_type="regular"):
        super().__init__(name, email)
        self.member_type = member_type
        self.points = 0
        self.orders = []
        self.join_date = datetime.now()

    def add_points(self, amount):
        """Add loyalty points"""
        if amount < 0:
            raise ValueError("Points cannot be negative")
        self.points += amount

    def use_points(self, amount):
        """Use loyalty points"""
        if amount > self.points:
            raise ValueError("Insufficient points")
        self.points -= amount

    def get_discount_rate(self):
        """Get discount rate based on member type"""
        rates = {
            "regular": 0.0,
            "member": 0.10,
            "premium": 0.15
        }
        return rates.get(self.member_type, 0.0)

    def add_order(self, order):
        """Add order to history"""
        self.orders.append(order)

    def __str__(self):
        return f"{self.name} ({self.member_type}) - {self.points} points"


class OrderItem:
    """Represents an item in an order"""

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
        self.price_at_purchase = product.price

    def get_subtotal(self):
        """Calculate item subtotal"""
        return self.price_at_purchase * self.quantity

    def __str__(self):
        return f"{self.quantity}x {self.product.title} @ ${self.price_at_purchase}"


class Order:
    """Represents a customer order"""

    order_counter = 10000  # Class attribute for order IDs

    def __init__(self, customer):
        Order.order_counter += 1
        self.order_id = f"ORD-{Order.order_counter}"
        self.customer = customer
        self.items = []
        self.status = "pending"
        self.created_at = datetime.now()
        self._subtotal = 0
        self._discount = 0
        self._tax = 0
        self._total = 0

    def add_item(self, product, quantity):
        """Add item to order"""
        if not product.is_available():
            raise ValueError(f"{product.title} is out of stock")

        if quantity > product.stock:
            raise ValueError(f"Only {product.stock} of {product.title} available")

        item = OrderItem(product, quantity)
        self.items.append(item)

    def calculate_totals(self):
        """Calculate order totals"""
        # Subtotal
        self._subtotal = sum(item.get_subtotal() for item in self.items)

        # Discount
        discount_rate = self.customer.get_discount_rate()
        self._discount = self._subtotal * discount_rate

        # Tax (on discounted amount)
        taxable_amount = self._subtotal - self._discount
        self._tax = taxable_amount * 0.08

        # Total
        self._total = self._subtotal - self._discount + self._tax

    def process(self):
        """Process the order"""
        if not self.items:
            raise ValueError("Order has no items")

        # Calculate totals
        self.calculate_totals()

        # Reduce stock for each item
        for item in self.items:
            item.product.reduce_stock(item.quantity)

        # Add points to customer
        points_earned = int(self._total)
        if self.customer.member_type == "premium":
            points_earned *= 2

        self.customer.add_points(points_earned)

        # Add to customer's order history
        self.customer.add_order(self)

        # Update status
        self.status = "processed"

        # Send confirmation email
        self.send_confirmation()

        return True

    def send_confirmation(self):
        """Send order confirmation email"""
        message = f"""
Order Confirmation

Order ID: {self.order_id}
Date: {self.created_at.strftime('%Y-%m-%d %H:%M')}

Items:
{self._format_items()}

Subtotal: ${self._subtotal:.2f}
Discount: ${self._discount:.2f}
Tax: ${self._tax:.2f}
Total: ${self._total:.2f}

Points earned: {int(self._total)}

Thank you for your order!
        """
        self.customer.send_email("Order Confirmation", message)

    def _format_items(self):
        """Format items for display"""
        lines = []
        for item in self.items:
            lines.append(f"  - {item}")
        return "\n".join(lines)

    def get_summary(self):
        """Get order summary"""
        return {
            "order_id": self.order_id,
            "customer": self.customer.name,
            "items": len(self.items),
            "subtotal": self._subtotal,
            "discount": self._discount,
            "tax": self._tax,
            "total": self._total,
            "status": self.status
        }

    def __str__(self):
        return f"Order {self.order_id} - {self.customer.name} - ${self._total:.2f}"


class Store:
    """Represents the entire store"""

    def __init__(self, name):
        self.name = name
        self.products = {}
        self.customers = {}
        self.orders = []

    def add_product(self, product):
        """Add product to catalog"""
        self.products[product.product_id] = product

    def get_product(self, product_id):
        """Get product by ID"""
        return self.products.get(product_id)

    def add_customer(self, customer):
        """Add customer"""
        self.customers[customer.email] = customer

    def get_customer(self, email):
        """Get customer by email"""
        return self.customers.get(email.lower())

    def create_order(self, customer_email):
        """Create new order for customer"""
        customer = self.get_customer(customer_email)
        if not customer:
            raise ValueError("Customer not found")

        order = Order(customer)
        return order

    def process_order(self, order):
        """Process and save order"""
        order.process()
        self.orders.append(order)
        return order

    def get_sales_report(self):
        """Generate sales report"""
        total_revenue = sum(order._total for order in self.orders if order.status == "processed")
        total_orders = len([o for o in self.orders if o.status == "processed"])

        return {
            "total_orders": total_orders,
            "total_revenue": total_revenue,
            "average_order": total_revenue / total_orders if total_orders > 0 else 0,
            "total_customers": len(self.customers),
            "total_products": len(self.products)
        }


def print_header(title):
    """Print formatted header"""
    print("\n" + "=" * 70)
    print(title.center(70))
    print("=" * 70)


def main():
    """Main demonstration"""

    # Create store
    store = Store("Bookish Corner")

    # Add products
    store.add_product(Product("P001", "Python Programming", 29.99, 25, "Programming"))
    store.add_product(Product("P002", "JavaScript Basics", 24.99, 15, "Programming"))
    store.add_product(Product("P003", "Data Science", 39.99, 8, "Data Science"))

    # Add customers
    store.add_customer(Customer("Alice Johnson", "alice@email.com", "premium"))
    store.add_customer(Customer("Bob Smith", "bob@email.com", "member"))

    print_header("BOOKISH CORNER - OOP DEMO")

    # Demo 1: Create and process order
    print("\n📦 DEMO 1: Create Order")
    print("-" * 70)

    customer = store.get_customer("alice@email.com")
    print(f"Customer: {customer}")

    order = store.create_order("alice@email.com")
    print(f"Created: {order.order_id}")

    # Add items
    order.add_item(store.get_product("P001"), 2)
    order.add_item(store.get_product("P002"), 1)
    print(f"Added {len(order.items)} items")

    # Process order
    store.process_order(order)
    print(f"Status: {order.status}")

    # Show results
    summary = order.get_summary()
    print(f"\nTotal: ${summary['total']:.2f}")
    print(f"Customer points: {customer.points}")

    # Demo 2: Another customer
    print("\n\n📦 DEMO 2: Another Order")
    print("-" * 70)

    customer2 = store.get_customer("bob@email.com")
    print(f"Customer: {customer2}")

    order2 = store.create_order("bob@email.com")
    order2.add_item(store.get_product("P003"), 1)
    store.process_order(order2)

    summary2 = order2.get_summary()
    print(f"Total: ${summary2['total']:.2f}")

    # Demo 3: Sales Report
    print("\n\n📊 SALES REPORT")
    print("-" * 70)

    report = store.get_sales_report()
    print(f"Total Orders: {report['total_orders']}")
    print(f"Total Revenue: ${report['total_revenue']:.2f}")
    print(f"Average Order: ${report['average_order']:.2f}")
    print(f"Total Customers: {report['total_customers']}")
    print(f"Total Products: {report['total_products']}")

    # Demo 4: Show products
    print("\n\n📚 PRODUCT CATALOG")
    print("-" * 70)

    for product in store.products.values():
        print(f"  {product}")

    print("\n")


if __name__ == "__main__":
    main()
