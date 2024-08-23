from connection import connect_db

def show_author():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        name = input("Enter the author's name to view: ")
        cursor.execute("SELECT * FROM authors WHERE name = %s", (name,))
        author = cursor.fetchone()
        if author:
            print(author)
        else:
            print("Author not found.")
        conn.close()
    else:
        print("Failed to connect to the database.")
