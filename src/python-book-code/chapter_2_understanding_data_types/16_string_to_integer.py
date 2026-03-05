"""
Example 16 from Chapter 2: Understanding Data - Types and Operations
Python Programming Fundamentals by Rajesh Aadi

String To Integer
"""

# String to Integer
quantity_text = "5"
quantity = int(quantity_text)
print(quantity + 10)  # 15

# String to Float
price_text = "29.99"
price = float(price_text)
print(price * 2)  # 59.98

# Number to String
order_number = 12345
order_id = "ORD-" + str(order_number)
print(order_id)  # ORD-12345

# Float to Integer (truncates decimal)
price = 29.99
price_whole = int(price)
print(price_whole)  # 29 (not 30!)

# Integer to Float
quantity = 5
price_per_item = 10.00
average = float(quantity) / 2
print(average)  # 2.5
