"""
Example 14 from Chapter 10: Handling Problems - Error Handling and Exceptions
Python Programming Fundamentals by Rajesh Aadi

Define Custom Exceptions
"""

# Define custom exceptions
class InsufficientStockError(Exception):
    """Raised when product is out of stock"""
    pass

class InvalidEmailError(Exception):
    """Raised when email format is invalid"""
    def __init__(self, email):
        self.email = email
        super().__init__(f"Invalid email format: {email}")

class OrderProcessingError(Exception):
    """Raised when order cannot be processed"""
    def __init__(self, order_id, reason):
        self.order_id = order_id
        self.reason = reason
        super().__init__(f"Order {order_id} failed: {reason}")

# Use custom exceptions
def check_stock(product, quantity):
    """Check if enough stock available"""
    available = 5  # Simulated

    if quantity > available:
        raise InsufficientStockError(
            f"Only {available} units of {product} available, requested {quantity}"
        )

def validate_email(email):
    """Validate email format"""
    if "@" not in email:
        raise InvalidEmailError(email)

# Usage
try:
    check_stock("Python Book", 10)
except InsufficientStockError as e:
    print(f"Stock error: {e}")

try:
    validate_email("invalid.email")
except InvalidEmailError as e:
    print(f"Email error: {e}")
    print(f"Problem email: {e.email}")
