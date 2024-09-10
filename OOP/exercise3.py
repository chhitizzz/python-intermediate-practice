# Create a class Library that holds a list of books. Implement methods to add, remove, and search for books. Also, implement a method to display all books in the library.

class Library: 
    def __init__(self):
        self.books = []

    def add_books(self, book):
        self.books.append(book)
        print(f"'{book}' has been added to the library.")

    def remove_books(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"'{book}' has been removed.")
        else: 
            print(f"'{book}' is not found in the library.")
    
    def search_books(self, book):
        if book in self.books:
            print(f"'{book}' is in the library.")
        else:
            print(f"'{book}' is not available in the library.")