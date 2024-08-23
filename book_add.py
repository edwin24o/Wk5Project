from connection import connect_db

def add_book():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        title = input("Enter the book title: ")
        author_name = input("Enter the author's name: ")
        isbn = input("Enter the ISBN number: ")
        publication_date = input("Enter the publication date (YYYY-MM-DD): ")

        cursor.execute("SELECT id FROM authors WHERE name = %s", (author_name,))
        author_id = cursor.fetchone()
        if author_id:
            author_id = author_id[0]
        else:
            print("Author not found. Please add the author first.")
            conn.close()
            return

        cursor.execute(
            "INSERT INTO books (title, author_id, isbn, publication_date) VALUES (%s, %s, %s, %s)",
            (title, author_id, isbn, publication_date)
        )
        conn.commit()
        print("Book added successfully.")
        conn.close()
    else:
        print("Failed to connect to the database.")
