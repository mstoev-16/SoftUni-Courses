# First way
n = int(input())
key_word = input()

word_list = []

for _ in range(n):
    current_word = input()

    word_list.append(current_word)

print(word_list)

for i in range(len(word_list) - 1, -1, -1):
    element = word_list[i]

    if key_word not in element:
        word_list.remove(element)

print(word_list)


# Better way
n = int(input())
key_word = input()

initial_list = []
filtered_list = []

for i in range(n):
    word = input()
    initial_list.append(word)

    if key_word in word:
        filtered_list.append(word)

print(initial_list)
print(filtered_list)
