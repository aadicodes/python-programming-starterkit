"""
Example 16 from Chapter 7: Powerful Data Structures - Dictionaries and Sets
Python Programming Fundamentals by Rajesh Aadi

Track Daily Visitors
"""

# Track daily visitors
visitors_monday = {"alice@email.com", "bob@email.com", "charlie@email.com"}
visitors_tuesday = {"bob@email.com", "david@email.com", "alice@email.com"}

# Total unique visitors this week
all_visitors = visitors_monday | visitors_tuesday
print(f"Unique visitors: {len(all_visitors)}")  # 4

# Returning customers
returning = visitors_monday & visitors_tuesday
print(f"Returning customers: {len(returning)}")  # 2 (alice, bob)

# New customers on Tuesday
new_tuesday = visitors_tuesday - visitors_monday
print(f"New on Tuesday: {new_tuesday}")  # {'david@email.com'}
