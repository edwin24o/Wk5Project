from connection import connect_db

def add_user():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        name = input("Enter the user's name: ")
        library_id = input("Enter the library ID: ")

        cursor.execute(
            "INSERT INTO users (name, library_id) VALUES (%s, %s)",
            (name, library_id)
        )
        conn.commit()
        print("User added successfully.")
        conn.close()
    else:
        print("Failed to connect to the database.")
