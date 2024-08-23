from connection import connect_db

def all_the_books():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        if books:
            for book in books:
                print(book)
        else:
            print("No books available.")
        conn.close()
    else:
        print("Failed to connect to the database.")
