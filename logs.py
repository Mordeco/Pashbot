import mysql.connector

# Replace with your database credentials
db_config = {
    "host": "localhost",
    "user": "your_username",
    "password": "your_password",
    "database": "pash_bank"
}

def connect_to_db():
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to database: {err}")
        return None

def check_balance(user_id):
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT balance FROM users WHERE user_id = %s", (user_id,))
        result = cursor.fetchone()
        connection.close()
        return result[0] if result else 0
    else:
        return None

# ... (similar functions for other functionalities)

def log_command(user_id, command):
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO command_logs (user_id, command) VALUES (%s, %s)", (user_id, command))
        connection.commit()
        connection.close()

# Example usage
user_id = 12345
balance = check_balance(user_id)
print(f"User {user_id} has {balance} Pash Coins.")

log_command(user_id, "!work")
