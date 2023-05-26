# Improved version
def check_password(password):
    result = []
    if not 6 <= len(password) <= 10:
        result.append("Password must be between 6 and 10 characters")

    for el in list(password):
        if not el.isdigit() and not el.isalpha():
            result.append("Password must consist only of letters and digits")
            break

    dig_count = list(filter(lambda x: x.isdigit(), list(password)))

    if len(dig_count) < 2:
        result.append('Password must have at least 2 digits')

    if not result:  # if result == []
        result.append('Password is valid')

    return '\n'.join(result)


print(check_password(input()))


# Longer version
def validate_password(password):
    cnt = 0
    is_valid = True
    if not(6 <= len(password) <= 10):
        print('Password must be between 6 and 10 characters')
        is_valid = False

    for element in password:
        if not element.isdigit() and not element.isalpha():
            print('Password must consist only of letters and digits')
            is_valid = False

        elif element.isdigit():
            cnt += 1

    if cnt < 2:
        print('Password must have at least 2 digits')
        is_valid = False

    if is_valid:
        print('Password is valid')

    return


input_password = input()
validate_password(input_password)