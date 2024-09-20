import sqlite3
import time

def create_connection():
    """Create a connection to the database."""
    return sqlite3.connect('canteen.db')

def get_user_id():
    """Simulate scanning the User ID or entering it manually."""
    start_time = time.time()
    user_id = input("Enter User ID (or scan): ")
    elapsed_time = time.time() - start_time

    # If input time is less than 2 seconds, assume it's a scan
    if elapsed_time < 2:
        return user_id, True  # True indicates it was a scan
    return user_id, False  # False indicates manual entry

def get_password():
    """Simulate entering the password."""
    return input("Enter Password: ")

def check_user_exists(user_id):
    """Check if the user exists in the database."""
    conn = create_connection()
    cursor = conn.cursor()

    # Query to find the user by user_id
    cursor.execute('SELECT * FROM consumers WHERE user_id = ?', (user_id,))
    user = cursor.fetchone()
    
    conn.close()

    if user:
        return True  # User exists
    return False  # User not found

def check_user_credentials(user_id, password):
    """Check if the user exists and the credentials are correct."""
    conn = create_connection()
    cursor = conn.cursor()

    # Query to find the user by user_id
    cursor.execute('SELECT * FROM consumers WHERE user_id = ?', (user_id,))
    user = cursor.fetchone()
    
    conn.close()

    # Check if user exists and password matches
    if user and user[1] == password:  # Assuming the password is the second field
        return user  # Return user details
    return None  # Return None if user not found or password is incorrect

def get_user_details(user_id):
    """Fetch user details, purchases, and holds from the database."""
    conn = create_connection()
    cursor = conn.cursor()

    # Fetch user purchases
    cursor.execute('SELECT * FROM purchases WHERE user_id = ?', (user_id,))
    purchases = cursor.fetchall()

    # Fetch user holds
    cursor.execute('SELECT * FROM holds WHERE user_id = ?', (user_id,))
    holds = cursor.fetchall()

    conn.close()
    return {
        'purchases': purchases,
        'holds': holds
    }

def create_new_user(user_id):
    """Simulate creating a new user."""
    print(f"User {user_id} not found. Create new user.")
    # Here you could add the logic to create a new user in the database

def login_user():
    """Main function to handle user login."""
    user_id, is_scanned = get_user_id()

    # Check if user exists in the database
    user_exists = check_user_exists(user_id)

    if not user_exists:
        # If user doesn't exist, prompt to create a new user
        create_new_user(user_id)
        return

    if is_scanned:
        # If the ID is scanned, skip password check
        return get_user_details(user_id)  # Assuming scanning is trusted

    while True:
        password = get_password()
        
        # Check if user credentials are valid
        user = check_user_credentials(user_id, password)

        if user:
            # User found, fetch details
            user_details = get_user_details(user_id)
            return user_details  # Return user details without printing
        else:
            print("Incorrect Password, Try Again")

if __name__ == "__main__":
    user_info = login_user()
    # You can now use user_info in your application
