import os

def delete_database():
    """Delete the SQLite database file if it exists."""
    db_file = 'canteen.db'
    
    if os.path.exists(db_file):
        os.remove(db_file)
        print(f"Database '{db_file}' deleted successfully.")
    else:
        print(f"Database '{db_file}' not found.")

# Call the function to delete the database
delete_database()
