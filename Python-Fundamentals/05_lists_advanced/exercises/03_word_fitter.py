fitted = [print(word) for word in input().split() if len(word) % 2 == 0]

even_len = [word for word in input().split() if len(word) % 2 == 0]
print('\n'.join(even_len))