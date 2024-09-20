import sqlite3

def delete_user_entries(user_id):
    """Delete all entries from purchases and holds for a particular user."""
    conn = sqlite3.connect('canteen.db')
    cursor = conn.cursor()

    # Delete all purchases for the user
    cursor.execute('''
        DELETE FROM purchases WHERE user_id = ?
    ''', (user_id,))

    # Delete all hold entries for the user
    cursor.execute('''
        DELETE FROM holds WHERE user_id = ?
    ''', (user_id,))

    conn.commit()
    conn.close()
    print(f"All entries for user {user_id} have been deleted from purchases and holds tables.")

# Example usage
user_id = input("Enter User ID to delete all entries: ")
delete_user_entries(user_id)
