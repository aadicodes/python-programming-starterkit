"""
Example 22 from Chapter 6: Managing Collections - Lists and Tuples
Python Programming Fundamentals by Rajesh Aadi

Bookish Corner Product Catalo
"""

# Bookish Corner - Product Catalog Manager
# Version 6.0

def print_header(title):
    """Print formatted header"""
    print("\n" + "=" * 70)
    print(title.center(70))
    print("=" * 70)

def create_product(title, price, stock, category):
    """Create a product tuple"""
    return (title, price, stock, category)

def add_product(catalog):
    """Add a new product to the catalog"""
    print_header("ADD NEW PRODUCT")

    title = input("Book title: ")

    while True:
        try:
            price = float(input("Price: $"))
            if price > 0:
                break
            print("Price must be positive")
        except ValueError:
            print("Invalid price")

    while True:
        try:
            stock = int(input("Stock quantity: "))
            if stock >= 0:
                break
            print("Stock cannot be negative")
        except ValueError:
            print("Invalid quantity")

    category = input("Category: ")

    product = create_product(title, price, stock, category)
    catalog.append(product)
    print(f"\n✓ Added '{title}' to catalog")

def display_catalog(catalog):
    """Display all products"""
    if not catalog:
        print("\nCatalog is empty!")
        return

    print_header("PRODUCT CATALOG")
    print(f"{'#':<5} {'Title':<30} {'Price':<12} {'Stock':<8} {'Category':<15}")
    print("-" * 70)

    for index, product in enumerate(catalog, 1):
        title, price, stock, category = product
        stock_status = "✓" if stock > 0 else "✗"
        print(f"{index:<5} {title[:28]:<30} ${price:<11.2f} "
              f"{stock:>3} {stock_status}  {category:<15}")

    print("-" * 70)
    print(f"Total products: {len(catalog)}")

def search_catalog(catalog):
    """Search for products"""
    print_header("SEARCH CATALOG")

    query = input("Search term: ").lower()

    results = []
    for product in catalog:
        title, price, stock, category = product
        if (query in title.lower() or
            query in category.lower()):
            results.append(product)

    if results:
        print(f"\nFound {len(results)} result(s):")
        print(f"\n{'Title':<30} {'Price':<12} {'Stock':<8} {'Category':<15}")
        print("-" * 70)
        for product in results:
            title, price, stock, category = product
            print(f"{title[:28]:<30} ${price:<11.2f} {stock:>5}    {category:<15}")
    else:
        print(f"\nNo products found matching '{query}'")

def products_by_category(catalog):
    """Group products by category"""
    print_header("PRODUCTS BY CATEGORY")

    # Get unique categories
    categories = set()
    for product in catalog:
        title, price, stock, category = product
        categories.add(category)

    # Display each category
    for cat in sorted(categories):
        print(f"\n{cat.upper()}")
        print("-" * 40)

        cat_products = [p for p in catalog if p[3] == cat]
        for product in cat_products:
            title, price, stock, category = product
            print(f"  • {title[:35]:<35} ${price:>7.2f} (Stock: {stock})")

        print(f"  Subtotal: {len(cat_products)} products")

def low_stock_report(catalog, threshold=10):
    """Show products with low stock"""
    print_header(f"LOW STOCK REPORT (< {threshold} units)")

    low_stock = [p for p in catalog if p[2] < threshold]

    if low_stock:
        # Sort by stock level (lowest first)
        low_stock.sort(key=lambda p: p[2])

        print(f"{'Title':<30} {'Stock':<8} {'Price':<12} {'Category':<15}")
        print("-" * 70)

        for product in low_stock:
            title, price, stock, category = product
            urgency = "🔴" if stock == 0 else "🟡"
            print(f"{title[:28]:<30} {urgency} {stock:>3}    ${price:<11.2f} {category:<15}")

        print(f"\n⚠️  {len(low_stock)} products need restocking!")
    else:
        print("\n✓ All products have adequate stock")

def inventory_value_report(catalog):
    """Calculate total inventory value"""
    print_header("INVENTORY VALUE REPORT")

    if not catalog:
        print("\nNo products in catalog")
        return

    total_value = 0
    total_units = 0

    by_category = {}

    for product in catalog:
        title, price, stock, category = product

        product_value = price * stock
        total_value += product_value
        total_units += stock

        if category not in by_category:
            by_category[category] = {'value': 0, 'units': 0, 'products': 0}

        by_category[category]['value'] += product_value
        by_category[category]['units'] += stock
        by_category[category]['products'] += 1

    # Display by category
    print(f"\n{'Category':<20} {'Products':<12} {'Units':<10} {'Value':<15}")
    print("-" * 70)

    for cat in sorted(by_category.keys()):
        info = by_category[cat]
        print(f"{cat:<20} {info['products']:>8}     {info['units']:>6}     "
              f"${info['value']:>12,.2f}")

    print("-" * 70)
    print(f"{'TOTAL':<20} {len(catalog):>8}     {total_units:>6}     "
          f"${total_value:>12,.2f}")

    if len(catalog) > 0:
        avg_value = total_value / len(catalog)
        avg_price = sum(p[1] for p in catalog) / len(catalog)
        print(f"\nAverage product value: ${avg_value:,.2f}")
        print(f"Average price per book: ${avg_price:,.2f}")

def price_adjustment(catalog):
    """Apply price adjustments to products"""
    print_header("PRICE ADJUSTMENT")

    print("1. Apply discount to all products")
    print("2. Apply discount to category")
    print("3. Increase prices (inflation adjustment)")

    choice = input("\nSelect option (1-3): ")

    try:
        percentage = float(input("Percentage (e.g., 10 for 10%): ")) / 100
    except ValueError:
        print("Invalid percentage")
        return

    updated_catalog = []

    for product in catalog:
        title, price, stock, category = product

        update = False

        if choice == "1":
            update = True
        elif choice == "2":
            target_cat = input("Category to adjust: ")
            if category.lower() == target_cat.lower():
                update = True
        elif choice == "3":
            update = True
            percentage = abs(percentage)  # Make sure it's positive

        if update:
            if choice == "3":
                new_price = price * (1 + percentage)
            else:
                new_price = price * (1 - percentage)

            updated_catalog.append((title, new_price, stock, category))
        else:
            updated_catalog.append(product)

    return updated_catalog

def main():
    """Main program"""
    # Sample catalog data
    catalog = [
        create_product("Python Programming", 29.99, 25, "Programming"),
        create_product("JavaScript Basics", 24.99, 15, "Programming"),
        create_product("Data Science Fundamentals", 39.99, 8, "Data Science"),
        create_product("Machine Learning", 44.99, 5, "Data Science"),
        create_product("Business Analytics", 34.99, 20, "Business"),
        create_product("Marketing Strategy", 27.99, 12, "Business"),
        create_product("Financial Accounting", 49.99, 0, "Finance"),
        create_product("Investment Basics", 32.99, 7, "Finance"),
    ]

    while True:
        print_header("BOOKISH CORNER - CATALOG MANAGER")
        print("\n1. Display Catalog")
        print("2. Add Product")
        print("3. Search Catalog")
        print("4. Products by Category")
        print("5. Low Stock Report")
        print("6. Inventory Value Report")
        print("7. Price Adjustment")
        print("8. Exit")

        choice = input("\nSelect option (1-8): ")

        if choice == "1":
            display_catalog(catalog)
        elif choice == "2":
            add_product(catalog)
        elif choice == "3":
            search_catalog(catalog)
        elif choice == "4":
            products_by_category(catalog)
        elif choice == "5":
            threshold = input("Stock threshold (default 10): ")
            threshold = int(threshold) if threshold.isdigit() else 10
            low_stock_report(catalog, threshold)
        elif choice == "6":
            inventory_value_report(catalog)
        elif choice == "7":
            catalog = price_adjustment(catalog)
            print("\n✓ Prices updated")
        elif choice == "8":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid option")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
