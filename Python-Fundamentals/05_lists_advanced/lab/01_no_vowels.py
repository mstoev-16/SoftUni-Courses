vowels = 'a o u e i A O  U E  I'

input_str = list(input())
vowelless = [el for el in input_str if el not in vowels]
print(''.join(vowelless))