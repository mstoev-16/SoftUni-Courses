while True:
    word = input()
    if word == 'end':
        break

    print(word, '=', word[::-1])