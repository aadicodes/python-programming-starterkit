"""
Example 7 from Chapter 12: Scaling Up - Modules and Packages
Python Programming Fundamentals by Rajesh Aadi

Practice Exercises - Working Examples
"""

# Exercise 1: Reorganize Project
print("=" * 50)
print("Exercise 1: Using Organized Modules")
print("=" * 50)

# Simulating organized module structure
class CustomerModel:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class ProductModel:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class OrderService:
    def __init__(self):
        self.orders = []
    
    def create_order(self, customer, product):
        order = {
            'customer': customer.name,
            'product': product.name,
            'price': product.price
        }
        self.orders.append(order)
        return order

# Using the organized modules
customer = CustomerModel("Alice", "alice@example.com")
product = ProductModel("Python Book", 29.99)
service = OrderService()
order = service.create_order(customer, product)
print(f"Order created: {order}")

# Exercise 2: Build CLI Tool
print("\n" + "=" * 50)
print("Exercise 2: Simple CLI Tool Example")
print("=" * 50)

def process_command(command):
    commands = {
        'help': 'Shows help',
        'list': 'Lists items',
        'add': 'Adds an item'
    }
    if command in commands:
        print(f"Command '{command}': {commands[command]}")
        return True
    else:
        print(f"Unknown command: {command}")
        return False

# Simulating CLI usage
process_command('help')
process_command('list')
process_command('unknown')

# Exercise 3: Library Package
print("\n" + "=" * 50)
print("Exercise 3: Reusable Library Functions")
print("=" * 50)

class MathLibrary:
    """A reusable math library"""
    
    @staticmethod
    def add(a, b):
        """Add two numbers"""
        return a + b
    
    @staticmethod
    def multiply(a, b):
        """Multiply two numbers"""
        return a * b
    
    @staticmethod
    def square(n):
        """Return square of a number"""
        return n * n

math_lib = MathLibrary()
print(f"5 + 3 = {math_lib.add(5, 3)}")
print(f"5 * 3 = {math_lib.multiply(5, 3)}")
print(f"5² = {math_lib.square(5)}")

# Exercise 4: Complete Application
print("\n" + "=" * 50)
print("Exercise 4: Application with Proper Structure")
print("=" * 50)

class Application:
    def __init__(self):
        self.data = []
        self.running = False
    
    def start(self):
        self.running = True
        print("Application started")
    
    def stop(self):
        self.running = False
        print("Application stopped")
    
    def add_data(self, item):
        if self.running:
            self.data.append(item)
            print(f"Added: {item}")
    
    def show_data(self):
        print(f"Current data: {self.data}")

app = Application()
app.start()
app.add_data("item1")
app.add_data("item2")
app.show_data()
app.stop()

print("\nAll exercises completed!")
