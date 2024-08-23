from connection import connect_db

def give_book_back():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        book_id = input("Enter the book ID to return: ")
        user_id = input("Enter the user ID: ")
        return_date = input("Enter the return date (YYYY-MM-DD): ")

        cursor.execute("SELECT id FROM borrowed_books WHERE book_id = %s AND user_id = %s AND return_date IS NULL", (book_id, user_id))
        borrow_id = cursor.fetchone()
        if borrow_id:
            cursor.execute(
                "UPDATE borrowed_books SET return_date = %s WHERE id = %s",
                (return_date, borrow_id[0])
            )
            cursor.execute("UPDATE books SET availability = 1 WHERE id = %s", (book_id,))
            conn.commit()
            print("Book returned successfully.")
        else:
            print("No record of this book being borrowed.")
        conn.close()
    else:
        print("Failed to connect to the database.")
