"""
Example 11 from Chapter 10: Handling Problems - Error Handling and Exceptions
Python Programming Fundamentals by Rajesh Aadi

Process Order
"""

import traceback

def process_order(order_data):
    """Process order with detailed error logging"""
    try:
        # Process order
        quantity = int(order_data["quantity"])
        price = float(order_data["price"])
        total = quantity * price

        return total

    except KeyError as e:
        print(f"Missing required field: {e}")
        traceback.print_exc()  # Print full traceback
        return None

    except ValueError as e:
        print(f"Invalid value: {e}")
        return None

    except Exception as e:
        print(f"Unexpected error: {e}")
        traceback.print_exc()
        return None

# Test
order = {"quantity": "abc", "price": "29.99"}
process_order(order)
