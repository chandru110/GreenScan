import sqlite3

def create_connection():
    """Create a connection to the database."""
    return sqlite3.connect('canteen.db')

def get_user_id():
    """Simulate scanning the User ID."""
    return input("Scan User ID: ")

def display_table_header():
    """Display a header for the table."""
    print("\n+----------------------+----------+")
    print("| Product Name         | Quantity |")
    print("+----------------------+----------+")

def display_table_row(product_name, quantity):
    """Display a row in the table."""
    print(f"| {product_name:<20} | {quantity:^8} |")

def display_table_footer():
    """Display a footer for the table."""
    print("+----------------------+----------+")

def display_hold_table_header():
    """Display a header for the hold table."""
    print("\n+----------------------+------------+")
    print("| Product Name         | Hold Amount|")
    print("+----------------------+------------+")

def display_hold_table_row(product_name, hold_amount):
    """Display a row in the hold table."""
    print(f"| {product_name:<20} | {hold_amount:^10.2f} |")

def display_hold_table_footer():
    """Display a footer for the hold table."""
    print("+----------------------+------------+")

def display_user_purchases(user_id):
    """Display the user's purchases and hold values, along with totals."""
    conn = create_connection()
    cursor = conn.cursor()

    # Fetch purchases (product name and quantity) for the specific user
    cursor.execute('SELECT product_name, quantity FROM purchases WHERE user_id = ?', (user_id,))
    purchases = cursor.fetchall()

    # Fetch hold values for the specific user
    cursor.execute('SELECT product_name, hold_amount FROM holds WHERE user_id = ?', (user_id,))
    holds = cursor.fetchall()

    # Calculate total products purchased by summing quantities
    total_products = sum(purchase[1] for purchase in purchases)  # Sum the quantities
    total_hold = sum(hold[1] for hold in holds)

    if total_products > 0:
        # Display purchases
        print(f"\nUser ID: {user_id}")
        display_table_header()
        for purchase in purchases:
            display_table_row(purchase[0], purchase[1])
        display_table_footer()

        # Display holds
        display_hold_table_header()
        for hold in holds:
            display_hold_table_row(hold[0], hold[1])
        display_hold_table_footer()

        # Display totals
        print(f"\nTotal Products Purchased: {total_products}")
        print(f"Total Hold Amount: {total_hold:.2f}")
    else:
        print(f"No purchases found for User ID: {user_id}")

    conn.close()

def display_user_data():
    """Main function to scan user ID and display purchased products and hold values."""
    user_id = get_user_id()
    display_user_purchases(user_id)

if __name__ == "__main__":
    display_user_data()
