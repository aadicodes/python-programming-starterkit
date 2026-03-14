"""
Example 8 from Chapter 10: Handling Problems - Error Handling and Exceptions
Python Programming Fundamentals by Rajesh Aadi

Save Customer
"""

def save_customer(customer_data):
    """Save customer with proper cleanup"""
    file = None

    try:
        file = open("customers.json", "w")
        json.dump(customer_data, file)
        print("Customer saved successfully")

    except IOError:
        print("Error saving customer")

    finally:
        # Always close the file, even if error occurred
        if file:
            file.close()
            print("File closed")

# Better approach - with statement handles this automatically
try:
    with open("customers.json", "w") as file:
        json.dump(customer_data, file)
    print("Customer saved successfully")
except IOError:
    print("Error saving customer")
