from connection import connect_db

def show_all_authors():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors")
        authors = cursor.fetchall()
        if authors:
            for author in authors:
                print(author)
        else:
            print("No authors found.")
        conn.close()
    else:
        print("Failed to connect to the database.")
