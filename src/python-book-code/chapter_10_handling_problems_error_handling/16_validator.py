"""
Example 16 from Chapter 10: Handling Problems - Error Handling and Exceptions
Python Programming Fundamentals by Rajesh Aadi

Validator
"""

class Validator:
    """Data validation utilities"""

    @staticmethod
    def validate_email(email):
        """Validate email format"""
        if not isinstance(email, str):
            raise TypeError("Email must be a string")

        email = email.strip().lower()

        if not email:
            raise ValueError("Email cannot be empty")

        if "@" not in email:
            raise ValueError("Email must contain @")

        if "." not in email.split("@")[1]:
            raise ValueError("Email must have valid domain")

        return email

    @staticmethod
    def validate_price(price):
        """Validate price"""
        try:
            price = float(price)
        except (ValueError, TypeError):
            raise ValueError("Price must be a number")

        if price < 0:
            raise ValueError("Price cannot be negative")

        if price > 10000:
            raise ValueError("Price seems unreasonably high")

        return round(price, 2)

    @staticmethod
    def validate_quantity(quantity):
        """Validate quantity"""
        try:
            quantity = int(quantity)
        except (ValueError, TypeError):
            raise ValueError("Quantity must be an integer")

        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        if quantity > 1000:
            raise ValueError("Quantity exceeds maximum order size")

        return quantity

# Usage
try:
    email = Validator.validate_email("  Alice@Email.com  ")
    price = Validator.validate_price("29.99")
    quantity = Validator.validate_quantity("5")

    print(f"Valid order: {email}, ${price}, qty={quantity}")

except ValueError as e:
    print(f"Validation error: {e}")
