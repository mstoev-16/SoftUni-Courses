from project.library import Library
from project.user import User


class Registration:
    def __init__(self):
        pass

    def add_user(self, user: User, library: Library):
        for library_user in library.user_records:
            if library_user.username == user.username:
                return f"User with id = {user.user_id} already registered in the library!"
        library.user_records.append(user)

    def remove_user(self, user: User, library: Library):
        for library_user in library.user_records:
            if library_user.username == user.username:
                return library.user_records.remove(library_user)
        return "We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library: Library):
        for library_user in library.user_records:
            if library_user.user_id == user_id:
                if new_username != library_user.username:
                    library_user.username = new_username
                    return f"Username successfully changed to: {new_username} for user id: {library_user.user_id}"
                return "Please check again the provided username - " \
                       "it should be different than the username used so far!"
        return f"There is no user with id = {user_id}!"


# user = User(12, 'Peter')
# user_2 = User(13, 'Sonny')
# library = Library()
# registration = Registration()
# registration.add_user(user, library)
# registration.add_user(user_2, library)
# library.books_available.update({'J.K.Rowling': ['The Chamber of Secrets',
# 'The Prisoner of Azkaban',
# 'The Goblet of Fire',
# 'The Order of the Phoenix',
# 'The Half-Blood Prince',
# 'The Deathly Hallows']})
# print(library.get_book('J.K.Rowling', 'The Deathly Hallows', 10, user))
# print(library.get_book('J.K.Rowling', 'The Deathly Hallows', 10, user))
# print(library.get_book('J.K.Rowling', 'The Deathly Hallows', 13, user_2))
# print(user)