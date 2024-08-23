from connection import connect_db

def add_author():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        name = input("Enter the author's name: ")
        biography = input("Enter the biography: ")

        cursor.execute(
            "INSERT INTO authors (name, biography) VALUES (%s, %s)",
            (name, biography)
        )
        conn.commit()
        print("Author added successfully.")
        conn.close()
    else:
        print("Failed to connect to the database.")
