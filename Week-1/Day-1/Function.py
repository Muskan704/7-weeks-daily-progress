"""
Problem 1: Library Management System (Functions-Based)
🧩 Problem Statement

Design a simple Library Management System using functions.

The system should:

Store a list of books
Allow user to:
Add a new book
Remove a book
Search for a book
Display all books
Use functions for each operation

"""

def add_book(library):
    book = input("Enter the Book name: ")
    library.append(book)
    print("Book added Successfully")

def remove_book(library):
    book = input("Enter the book name you want to remove: ")
    if book in library:
        library.remove(book)
        print("Book removed Successfully")
    else:
        print("Book is not found")

def search_book(library):
    book = input("Enter Book Name: ")
    if book in library:
        print("Book is Found")
    else:
        print("Book is not Found")

def display_book(library):
    if not library:
        print("Library is Empty")
    else:
        print("Books are present in the Library")
        for book in library: 
            print("-",book)

def library_System():
    library = []

    while True:
        print("\n 1.Add Book")
        print("2.Remove Book")
        print("3.Search Book")
        print("4.Display Book")
        print("5.Exit")
        
        choice = int(input("Enter your Choice: "))
        if(choice == 1):
            add_book(library)
        elif(choice == 2):
            remove_book(library)
        elif(choice == 3):
            remove_book(library)
        elif(choice == 4):
            display_book(library)
        elif(choice == 5):
            print("Exiting the program")
            break
        else:
            print("Invalid input")

library_System()
    
