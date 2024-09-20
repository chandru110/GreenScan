import sqlite3

def create_user_database():
    """Create the SQLite database with the required user tables."""
    conn = sqlite3.connect('canteen.db')
    cursor = conn.cursor()

    # Create a table for Consumers with user_id and password
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS consumers (
            user_id TEXT PRIMARY KEY,  -- Unique identifier for consumers
            password TEXT NOT NULL
        )
    ''')

    # Create a table for Retailers with retailer_id and password
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS retailers (
            retailer_id TEXT PRIMARY KEY,  -- Unique identifier for retailers
            password TEXT NOT NULL
        )
    ''')

    # Create a table for consumer purchases (with quantity and price per product)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS purchases (
            purchase_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            product_name TEXT,
            quantity INTEGER,  -- Quantity of products purchased
            price REAL,        -- Price per product
            FOREIGN KEY(user_id) REFERENCES consumers(user_id)
        )
    ''')

    # Create a table for temporary holds for consumers (with hold_amount and actual_price)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS holds (
            hold_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            product_name TEXT,
            hold_amount REAL,    -- 30% hold on product price
            actual_price REAL,   -- Full price of the product
            FOREIGN KEY(user_id) REFERENCES consumers(user_id)
        )
    ''')

    conn.commit()
    print("User database and tables created successfully.")
    conn.close()

def add_initial_entries():
    """Add some initial data to the consumers and retailers tables."""
    conn = sqlite3.connect('canteen.db')
    cursor = conn.cursor()

    # Pre-defined entries for Consumers with user_id and password
    cursor.execute('DELETE FROM consumers')
    cursor.execute('DELETE FROM retailers')

    cursor.execute('''
        INSERT INTO consumers (user_id, password) VALUES
        ('CH.SC.U4CSE23001', '12345678'),
        ('CH.SC.U4CSE23002', '12345678'),
        ('CH.SC.U4CSE23003', '12345678'),
        ('CH.SC.U4CSE23004', '12345678'),
        ('CH.SC.U4CSE23005', '12345678')
    ''')

    # Pre-defined entries for Retailers with retailer_id and password
    cursor.execute('''
        INSERT INTO retailers (retailer_id, password) VALUES
        ('R1', '12345678'),
        ('R2', '12345678'),
        ('R3', '12345678')
    ''')

    conn.commit()
    print("Initial entries added successfully.")
    conn.close()

if __name__ == "__main__":
    create_user_database()
    add_initial_entries()
