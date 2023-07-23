sequence = input().split()
total_sum = 0

for el in sequence:
    starting_letter = el[0]
    closing_letter = el[-1]
    number = int(el[1:len(el) - 1])

    if starting_letter.isupper():
        number /= ord(starting_letter) - 64
    elif starting_letter.islower():
        number *= ord(starting_letter) - 96

    if closing_letter.isupper():
        number -= ord(closing_letter) - 64
    elif closing_letter.islower():
        number += ord(closing_letter) - 96

    total_sum += number

print(f'{total_sum:.2f}')