


class Book:
    def __init__(self, title, author_id, isbn, genre, publication_date):
        self.title = title
        self.author_id = author_id
        self.isbn = isbn
        self.genre = genre
        self.publication_date = publication_date
        self._availability = True

    def save_db(self):
        add_new_book(self.title, self.author_id, self.isbn, self.publication_date, self.availability)
        
    def borrow(self):
        if self._availability:
            self._availability = False
            print(f"Book '{self.title}' has been borrowed.")
        else:
            print(f"Book '{self.title}' is currently unavailable.")

    def return_book(self):
        self._availability = True
        print(f"Book '{self.title}' has been returned.")

    def get_details(self):
        availability = "Available" if self._availability else "Not Available"
        return f"Title: {self.title}, Author: {self.author_id}, Genre: {self.genre}, Published: {self.publication_date}, Availability: {availability}"
    
