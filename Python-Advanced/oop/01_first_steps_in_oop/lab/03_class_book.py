class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages


book_1 = Book("The Complete Works of H.P. Lovecraft", "H.P. Lovecraft", 1004)
print(book_1.name)
print(book_1.author)
print(book_1.pages)