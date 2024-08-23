from mysql.connector import Error
from connection import connect_db
from book_add import add_book
from borrow import lend_a_book
from returns import give_book_back
from search import search_for_book
from all_books import all_the_books
from user_add import add_user
from users import search_for_user
from author_add import add_author
from author_search import show_author
from authors_all import show_all_authors
from users_all import fetch_all_users
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    while True:
        clear()
        print("Welcome to the Library Management System with Database Integration!")
        print("Main Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Quit")
        
        action = input("Choose an option: ")
        
        if action == '1':
            book_menu()
        elif action == '2':
            user_menu()
        elif action == '3':
            author_menu()
        elif action == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")

def book_menu():
    while True:
        clear()
        print("Book Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")
        print("6. Back to Main Menu")
        
        action = input("Choose an option: ")
        
        if action == '1':
            add_book()
        elif action == '2':
            lend_a_book()
        elif action == '3':
            give_book_back()
        elif action == '4':
            search_for_book()
        elif action == '5':
            all_the_books()
        elif action == '6':
            break
        else:
            print("Invalid input. Please try again.")

def user_menu():
    while True:
        clear()
        print("User Operations:")
        print("1. Add a new user")
        print("2. View user details")
        print("3. Display all users")
        print("4. Back to Main Menu")
        
        action = input("Choose an option: ")
        
        if action == '1':
            add_user()
        elif action == '2':
            search_for_user()
        elif action == '3':
            fetch_all_users()
        elif action == '4':
            break
        else:
            print("Invalid input. Please try again.")

def author_menu():
    while True:
        clear()
        print("Author Operations:")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all authors")
        print("4. Back to Main Menu")
        
        action = input("Choose an option: ")
        
        if action == '1':
            add_author()
        elif action == '2':
            show_author()
        elif action == '3':
            show_all_authors()
        elif action == '4':
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main_menu()