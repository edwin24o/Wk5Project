from connection import connect_db

def fetch_all_users():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        if users:
            for user in users:
                print(user)
        else:
            print("No users found.")
        conn.close()
    else:
        print("Failed to connect to the database.")