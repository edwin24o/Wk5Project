from connection import connect_db

def search_for_book():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        title = input("Enter the book title to search for: ")
        cursor.execute("SELECT * FROM books WHERE title LIKE %s", ('%' + title + '%',))
        books = cursor.fetchall()
        if books:
            for book in books:
                print(book)
        else:
            print("No books found.")
        conn.close()
    else:
        print("Failed to connect to the database.")
