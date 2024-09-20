import sqlite3

def create_connection():
    """Create a connection to the database."""
    return sqlite3.connect('canteen.db')

def get_user_id():
    """Simulate scanning the User ID."""
    return input("Scan User ID: ")

def get_product_id():
    """Simulate scanning the product barcode."""
    return input("Scan Product Barcode (Product ID): ")

def get_product_info(product_id):
    """Fetch product details from the products database."""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute('SELECT product_name, price FROM products WHERE product_id = ?', (product_id,))
    product = cursor.fetchone()
    
    conn.close()
    return product  # Returns None if product not found, otherwise (product_name, price)

def add_purchase(user_id, product_name, quantity, price):
    """Add the product to the purchases table and update the hold."""
    conn = create_connection()
    cursor = conn.cursor()

    # Check if user exists in consumers table
    cursor.execute('SELECT * FROM consumers WHERE user_id = ?', (user_id,))
    user = cursor.fetchone()

    if not user:
        print(f"User with ID {user_id} not found.")
        conn.close()
        return

    # Calculate the total price and hold amount based on quantity
    total_price = price * quantity
    hold_amount = total_price * 0.3

    # Add to purchases table
    cursor.execute(''' 
        INSERT INTO purchases (user_id, product_name, quantity, price) VALUES (?, ?, ?, ?)
    ''', (user_id, product_name, quantity, total_price))

    # Add to holds table (30% hold of the total price)
    cursor.execute(''' 
        INSERT INTO holds (user_id, product_name, hold_amount) VALUES (?, ?, ?)
    ''', (user_id, product_name, hold_amount))

    conn.commit()
    print(f"Product {product_name} (Quantity: {quantity}) added to purchases and 30% hold applied.")
    conn.close()

def scan_and_bill_user():
    """Main function to scan user ID and product barcodes, then bill products."""
    user_id = get_user_id()

    while True:
        product_id = get_product_id()

        if product_id.lower() == 'stop':
            print("Stopping the product scan.")
            break

        product = get_product_info(product_id)

        if product:
            product_name, price = product

            # Get quantity from the user
            quantity = int(input(f"Enter quantity for {product_name}: "))

            # Add the purchase and apply hold
            add_purchase(user_id, product_name, quantity, price)
        else:
            print(f"Product with ID {product_id} not found in the database.")

if __name__ == "__main__":
    scan_and_bill_user()
