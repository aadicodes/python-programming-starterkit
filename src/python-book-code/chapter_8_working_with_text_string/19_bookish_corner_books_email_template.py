"""
Example 19 from Chapter 8: Working with Text - String Manipulation
Python Programming Fundamentals by Rajesh Aadi

Bookish Corner Email Template
"""

# Bookish Corner - Email Template System
# Version 8.0

from datetime import datetime
import re

def print_header(title):
    """Print formatted header"""
    print("\n" + "=" * 70)
    print(title.center(70))
    print("=" * 70)

class EmailTemplate:
    """Email template manager"""

    TEMPLATES = {
        "welcome": """
Dear {customer_name},

Welcome to Bookish Corner! We're thrilled to have you as a {member_type} member.

Your account details:
- Email: {email}
- Member Since: {join_date}
- Current Points: {points}

{member_benefits}

Start browsing our catalog of over 500 books at:
https://bookishcorner.com

Happy reading!

Best regards,
The Bookish Corner Team
""",

        "order_confirmation": """
Dear {customer_name},

Thank you for your order!

ORDER DETAILS
{order_details}

Order Total: ${total:.2f}
Points Earned: {points_earned}
Current Point Balance: {total_points}

{shipping_info}

You can track your order at:
https://bookishcorner.com/orders/{order_id}

Thank you for choosing Bookish Corner!

Best regards,
The Bookish Corner Team
""",

        "newsletter": """
Dear {customer_name},

{newsletter_title}

{content}

This month's featured categories:
{featured_categories}

{special_offer}

Visit us at: https://bookishcorner.com

Best regards,
The Bookish Corner Team

---
Unsubscribe: https://bookishcorner.com/unsubscribe/{email}
""",

        "password_reset": """
Dear {customer_name},

We received a request to reset your password for {email}.

If you made this request, click the link below:
https://bookishcorner.com/reset/{reset_token}

This link expires in 24 hours.

If you didn't request this, please ignore this email.

Best regards,
The Bookish Corner Team
""",

        "low_stock_alert": """
INVENTORY ALERT

The following products are running low on stock:

{products_list}

Please review and reorder as necessary.

---
Bookish Corner Inventory System
"""
    }

    @staticmethod
    def get_member_benefits(member_type):
        """Get benefits text based on member type"""
        benefits = {
            "regular": "As a regular customer, enjoy:\n- Access to our full catalog\n- Standard shipping rates",
            "member": "As a member, enjoy:\n- 10% discount on all orders\n- Free shipping on orders over $50\n- Earn 1 point per dollar spent",
            "premium": "As a premium member, enjoy:\n- 15% discount on all orders\n- Free shipping on all orders\n- Earn 2 points per dollar spent\n- Priority customer support"
        }
        return benefits.get(member_type, benefits["regular"])

    @staticmethod
    def format_order_details(items):
        """Format order items for email"""
        if not items:
            return "No items"

        lines = []
        lines.append("-" * 60)
        lines.append(f"{'Item':<40} {'Qty':>5} {'Price':>12}")
        lines.append("-" * 60)

        for item in items:
            lines.append(f"{item['name']:<40} {item['qty']:>5} ${item['price']:>10.2f}")

        lines.append("-" * 60)
        return "\n".join(lines)

    @classmethod
    def generate_welcome_email(cls, customer):
        """Generate welcome email"""
        template = cls.TEMPLATES["welcome"]

        return template.format(
            customer_name=customer['name'],
            member_type=customer['member_type'].title(),
            email=customer['email'],
            join_date=customer.get('join_date', datetime.now().strftime("%Y-%m-%d")),
            points=customer.get('points', 0),
            member_benefits=cls.get_member_benefits(customer['member_type'])
        )

    @classmethod
    def generate_order_confirmation(cls, customer, order):
        """Generate order confirmation email"""
        template = cls.TEMPLATES["order_confirmation"]

        order_details = cls.format_order_details(order.get('items', []))

        shipping_info = "Standard shipping: 3-5 business days"
        if customer.get('member_type') in ['member', 'premium']:
            shipping_info = "Free shipping! Estimated delivery: 3-5 business days"

        return template.format(
            customer_name=customer['name'],
            order_details=order_details,
            total=order['total'],
            points_earned=order.get('points_earned', 0),
            total_points=customer.get('points', 0),
            shipping_info=shipping_info,
            order_id=order['order_id']
        )

    @classmethod
    def generate_newsletter(cls, customer, title, content, featured_categories):
        """Generate newsletter email"""
        template = cls.TEMPLATES["newsletter"]

        # Format categories
        categories_text = "\n".join([f"  • {cat}" for cat in featured_categories])

        # Special offer based on member type
        special_offers = {
            "regular": "🎁 Become a member today and save 10% on all orders!",
            "member": "🎁 Upgrade to premium and get 15% off + free shipping!",
            "premium": "🎁 Thank you for being a premium member! Enjoy your benefits!"
        }

        special_offer = special_offers.get(customer.get('member_type', 'regular'))

        return template.format(
            customer_name=customer['name'],
            newsletter_title=title,
            content=content,
            featured_categories=categories_text,
            special_offer=special_offer,
            email=customer['email']
        )

def validate_email_format(email):
    """Validate email format using regex"""
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

def extract_customer_info_from_text(text):
    """Extract customer information from text using regex"""
    email_pattern = r"[\w\.-]+@[\w\.-]+\.\w+"
    phone_pattern = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"

    emails = re.findall(email_pattern, text)
    phones = re.findall(phone_pattern, text)

    return {
        "emails": emails,
        "phones": phones
    }

def clean_text_for_display(text):
    """Clean text by removing extra whitespace"""
    # Replace multiple spaces with single space
    text = re.sub(r"\s+", " ", text)

    # Remove leading/trailing whitespace
    text = text.strip()

    return text

def main():
    """Main program"""

    # Sample customer data
    alice = {
        "name": "Alice Johnson",
        "email": "alice@email.com",
        "member_type": "premium",
        "points": 1250,
        "join_date": "2025-06-15"
    }

    bob = {
        "name": "Bob Smith",
        "email": "bob@email.com",
        "member_type": "member",
        "points": 450,
        "join_date": "2025-09-20"
    }

    while True:
        print_header("BOOKISH CORNER - EMAIL SYSTEM")
        print("\n1. Generate Welcome Email")
        print("2. Generate Order Confirmation")
        print("3. Generate Newsletter")
        print("4. Validate Email Address")
        print("5. Extract Contact Info from Text")
        print("6. Test All Templates")
        print("7. Exit")

        choice = input("\nSelect option (1-7): ")

        if choice == "1":
            print_header("WELCOME EMAIL")
            email = EmailTemplate.generate_welcome_email(alice)
            print(email)

        elif choice == "2":
            print_header("ORDER CONFIRMATION")
            order = {
                "order_id": "ORD-12345",
                "total": 89.97,
                "points_earned": 180,
                "items": [
                    {"name": "Python Programming", "qty": 2, "price": 29.99},
                    {"name": "Data Science Basics", "qty": 1, "price": 29.99}
                ]
            }
            email = EmailTemplate.generate_order_confirmation(alice, order)
            print(email)

        elif choice == "3":
            print_header("NEWSLETTER")
            email = EmailTemplate.generate_newsletter(
                alice,
                "📚 February 2026 Newsletter",
                "This month we're featuring our best programming books!\n\n"
                "Check out our new arrivals and special promotions.",
                ["Programming", "Data Science", "Business"]
            )
            print(email)

        elif choice == "4":
            print_header("EMAIL VALIDATION")
            test_email = input("Enter email to validate: ")
            if validate_email_format(test_email):
                print(f"✓ '{test_email}' is a valid email format")
            else:
                print(f"✗ '{test_email}' is NOT a valid email format")

        elif choice == "5":
            print_header("EXTRACT CONTACT INFO")
            print("Enter or paste text (type 'END' on a new line when done):")

            lines = []
            while True:
                line = input()
                if line.strip().upper() == "END":
                    break
                lines.append(line)

            text = "\n".join(lines)
            info = extract_customer_info_from_text(text)

            print("\nExtracted Information:")
            print(f"Emails found: {len(info['emails'])}")
            for email in info['emails']:
                print(f"  - {email}")

            print(f"\nPhones found: {len(info['phones'])}")
            for phone in info['phones']:
                print(f"  - {phone}")

        elif choice == "6":
            print_header("ALL EMAIL TEMPLATES")

            print("\n" + "="*70)
            print("WELCOME EMAIL (Premium Member)")
            print("="*70)
            print(EmailTemplate.generate_welcome_email(alice))

            print("\n" + "="*70)
            print("WELCOME EMAIL (Regular Member)")
            print("="*70)
            print(EmailTemplate.generate_welcome_email(bob))

            print("\n" + "="*70)
            print("ORDER CONFIRMATION")
            print("="*70)
            order = {
                "order_id": "ORD-12345",
                "total": 59.98,
                "points_earned": 60,
                "items": [
                    {"name": "Python Programming", "qty": 2, "price": 29.99}
                ]
            }
            print(EmailTemplate.generate_order_confirmation(bob, order))

            print("\n" + "="*70)
            print("NEWSLETTER")
            print("="*70)
            print(EmailTemplate.generate_newsletter(
                bob,
                "Monthly Tech Book Roundup",
                "Discover the latest in programming and technology!",
                ["Python", "JavaScript", "AI/ML"]
            ))

        elif choice == "7":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid option")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
