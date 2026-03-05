"""
Example 7 from Chapter 7: Powerful Data Structures - Dictionaries and Sets
Python Programming Fundamentals by Rajesh Aadi

Customer Database With Nested 
"""

# Customer database with nested dictionaries
customers = {
    "alice@email.com": {
        "name": "Alice Johnson",
        "member_type": "premium",
        "points": 1250,
        "address": {
            "street": "123 Main St",
            "city": "Boston",
            "state": "MA",
            "zip": "02101"
        },
        "order_history": [
            {"order_id": 1001, "total": 89.99, "date": "2026-01-15"},
            {"order_id": 1045, "total": 124.50, "date": "2026-02-01"}
        ]
    },
    "bob@email.com": {
        "name": "Bob Smith",
        "member_type": "member",
        "points": 450,
        "address": {
            "street": "456 Oak Ave",
            "city": "Cambridge",
            "state": "MA",
            "zip": "02139"
        },
        "order_history": []
    }
}

# Access nested data
alice = customers["alice@email.com"]
print(alice["name"])                    # Alice Johnson
print(alice["address"]["city"])         # Boston
print(alice["order_history"][0]["total"])  # 89.99

# Update nested data
customers["alice@email.com"]["points"] = 1300
customers["bob@email.com"]["address"]["city"] = "Somerville"
