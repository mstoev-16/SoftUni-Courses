word = input()

length = len(word)

for i in range(length - 1, -1, -1):
    print(word[i], end='')

# Alternative way - simpler
# print(word[::-1])
