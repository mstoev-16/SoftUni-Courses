n = int(input())

characters_sum = 0

for char in range(n):
    character = input()
    characters_sum += ord(character)

print(f'The sum equals: {characters_sum}')
