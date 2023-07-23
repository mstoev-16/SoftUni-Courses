banned_words = input().split(', ')
string = input()

for banned_word in banned_words:
    while banned_word in string:
        string = string.replace(banned_word, '*' * len(banned_word))

print(string)