import sqlite3

def create_products_database():
    """Create the SQLite database for products with ProductID, product name, and price."""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Create a table for products
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            product_id TEXT PRIMARY KEY,  -- Unique identifier for products
            product_name TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')

    # Add some sample products (you can edit these later)
    cursor.execute('''
        INSERT INTO products (product_id, product_name, price) VALUES
        ('P001', 'Lays', 20),
        ('P002', 'Cookies', 50),
        ('P003', 'Orange', 100),
        ('P004', 'Grapes', 200),
        ('P005', 'Milk', 150)
    ''')

    conn.commit()
    conn.close()
    print("Products database created and populated with sample data.")

# Run this function to create the products database
create_products_database()
