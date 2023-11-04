book_name = 'hi'
rented_books = {'George': {'hi': 17}, 'Stefan': {'Chess': 3}}

for current_user, book_data in rented_books.items():
    if book_name in book_data:
        for current_book in book_data.keys():
            if current_book == book_name:
                print(current_book)
        break
else:
    print('Book is no taken')