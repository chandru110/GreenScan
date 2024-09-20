from flask import Flask, render_template, request, jsonify, redirect, url_for
import sqlite3

app = Flask(__name__)

# Function to connect to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('canteen.db')
    conn.row_factory = sqlite3.Row
    return conn

# Route for the login page
@app.route('/')
def login():
    return render_template('index.html')

# Route to handle login logic (consumers and retailers)
@app.route('/login', methods=['POST'])
def login_user():
    user_type = request.form.get('user_type')
    user_id = request.form.get('user_id')
    password = request.form.get('password')
    barcode = request.form.get('barcode')

    conn = get_db_connection()

    # Barcode case - if barcode is used, skip password verification
    if barcode == 'true':
        query = f"SELECT * FROM {user_type} WHERE {user_type[:-1]}_id = ?"
        cursor = conn.execute(query, (user_id,))
        user = cursor.fetchone()
        conn.close()
        
        if user:
            return jsonify({"status": "success", "redirect_url": url_for('login_page')})
        else:
            return jsonify({"status": "user_not_found"})

    # Manual entry case
    else:
        query = f"SELECT * FROM {user_type} WHERE {user_type[:-1]}_id = ?"
        cursor = conn.execute(query, (user_id,))
        user = cursor.fetchone()

        if user:
            if user["password"] == password:
                conn.close()
                return jsonify({"status": "success", "redirect_url": url_for('login_page')})
            else:
                conn.close()
                return jsonify({"status": "wrong_password"})
        else:
            conn.close()
            return jsonify({"status": "user_not_found"})

# Route for the redirect after successful login
@app.route('/login-page')
def login_page():
    return render_template('login-page.html')

if __name__ == '__main__':
    app.run(debug=True)
