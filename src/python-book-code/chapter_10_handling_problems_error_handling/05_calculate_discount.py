"""
Example 5 from Chapter 10: Handling Problems - Error Handling and Exceptions
Python Programming Fundamentals by Rajesh Aadi

Calculate Discount
"""

def calculate_discount(price, discount_percent):
    """Calculate discounted price"""
    try:
        # Convert to numbers
        price = float(price)
        discount_percent = float(discount_percent)

        # Calculate
        discount = price * (discount_percent / 100)
        final_price = price - discount

        return final_price

    except ValueError:
        print("Error: Please enter valid numbers")
        return None

    except ZeroDivisionError:
        print("Error: Division by zero")
        return None

    except TypeError:
        print("Error: Invalid data type")
        return None

# Test
print(calculate_discount("100", "10"))    # Works: 90.0
print(calculate_discount("abc", "10"))    # Catches ValueError
print(calculate_discount(100, "abc"))     # Catches ValueError
