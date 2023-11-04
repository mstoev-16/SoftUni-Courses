from project.user import User


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if book_name in self.books_available[author]:
            user_dict = {book_name: days_to_return}
            user.books.append(book_name)
            self.books_available[author].remove(book_name)
            self.rented_books[user.username] = user_dict
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        for current_user, book_data in self.rented_books.items():
            if book_name not in book_data:
                continue
            for current_book in book_data.keys():
                if current_book == book_name:
                    return f"The book \"{book_name}\" is already rented and will be available in " \
                           f"{self.rented_books[current_user][book_name]} days!"

    def return_book(self, author: str, book_name: str, user: User):
        if book_name in user.books:
            user.books.remove(book_name)
            self.rented_books[user.username] = {}
            self.books_available[author].append(book_name)
        else:
            return f"{user.username} doesn't have this book in his/her records!"
