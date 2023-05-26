def return_chars(char1, char2):
    start = ord(char1)
    end = ord(char2)

    characters = [chr(char) for char in range(start + 1, end)]
    return ' '.join(characters)


print(return_chars(input(), input()))