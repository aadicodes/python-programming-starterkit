"""
Example 13 from Chapter 10: Handling Problems - Error Handling and Exceptions
Python Programming Fundamentals by Rajesh Aadi

Process Payment
"""

def process_payment(amount):
    """Process payment with logging"""
    try:
        # Process payment
        if amount <= 0:
            raise ValueError("Amount must be positive")

        # Simulate payment processing
        print(f"Processing ${amount}")

    except ValueError as e:
        print(f"Payment validation failed: {e}")
        raise  # Re-raise the same exception

# Caller must handle
try:
    process_payment(-50)
except ValueError:
    print("Payment failed, notifying user")
