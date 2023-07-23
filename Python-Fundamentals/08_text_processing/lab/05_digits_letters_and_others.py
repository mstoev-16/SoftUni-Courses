string = input()
digits = ''
letters = ''
chars = ''

for i in range(len(string)):
    el = string[i]
    if el.isnumeric():
        digits += el
    elif el.isalpha():
        letters += el
    else:
        chars += el
print(f'{digits}\n{letters}\n{chars}')