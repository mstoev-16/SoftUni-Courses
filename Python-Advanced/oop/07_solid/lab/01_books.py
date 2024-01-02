class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __repr__(self):
        return f"Title: {self.title}, Author: {self.author}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        if book not in self.books:
            self.books.append(book)
            return f"{book.title} by {book.author} is added to the library."
        return f"{book.title} by {book.author} is already in the library."

    def find_book(self, title):
        try:
            return [repr(book) for book in self.books if title == book.title][0]
        except IndexError:
            return 'Book not found.'


book1 = Book('Solaris', 'Stanislav Lem')
book2 = Book('1984', 'George Orwell')
library = Library()
print(library.add_book(book1))
print(library.add_book(book1))
print(library.add_book(book2))
print(library.add_book(book2))
print(library.find_book('1984'))
print(library.find_book('Solaris'))
print(library.find_book('Solais'))
