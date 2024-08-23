from connection import connect_db

def lend_a_book():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        book_id = input("Enter the book ID to borrow: ")
        user_id = input("Enter the user ID: ")
        borrow_date = input("Enter the borrow date (YYYY-MM-DD): ")

        cursor.execute("SELECT availability FROM books WHERE id = %s", (book_id,))
        availability = cursor.fetchone()
        if availability and availability[0] == 1:
            cursor.execute(
                "INSERT INTO borrowed_books (user_id, book_id, borrow_date) VALUES (%s, %s, %s)",
                (user_id, book_id, borrow_date)
            )
            cursor.execute("UPDATE books SET availability = 0 WHERE id = %s", (book_id,))
            conn.commit()
            print("Book borrowed successfully.")
        else:
            print("Book is not available or does not exist.")
        conn.close()
    else:
        print("Failed to connect to the database.")

           
    