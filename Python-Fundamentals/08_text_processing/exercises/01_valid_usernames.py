usernames = input().split(', ')
USERNAME_LENGTH = range(3, 17)


for username in usernames:
    length_check = False
    contents_check = False

    if len(username) in USERNAME_LENGTH:
        length_check = True

    if username.isalpha() or username.isalnum() or '-' in username or '_' in username:
        contents_check = True

    if length_check and contents_check:
        print(username)