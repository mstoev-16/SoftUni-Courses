class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username_entry):
        if 4 > len(username_entry) or len(username_entry) > 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = username_entry

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password_entry):
        valid_length = len(password_entry) >= 8
        valid_uppercase = any([letter.isupper() for letter in password_entry])
        valid_digit = any([el.isdigit() for el in password_entry])

        if valid_length and valid_digit and valid_uppercase:
            self.__password = password_entry
            return
        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self):
        return f"You have a profile with username: \"{self.username}\" and password: {'*' * len(self.password)}"
