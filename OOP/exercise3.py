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

    def display_books(self):
        if self.books:
            print("The books available in the library are:")
            for book in self.books:
                print(f"- {book}")
        else:
            print("No books are available in the library.")

new_book = Library()
new_book.add_books("The Alchemist")
new_book.add_books("1984")
new_book.add_books("Rich Dad, Poor Dad")
new_book.add_books("Can't Hurt Me")
new_book.add_books("Becoming")

new_book.display_books()