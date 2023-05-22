# Newest solution with lists and actually the best one so far
word1 = list(input())
word2 = list(input())

transformed_word = list(word1)

for i in range(len(word1)):
    transformed_word[i] = word2[i]

    if transformed_word != word1:
        print(''.join(transformed_word))
        word1[i] = transformed_word[i]


# Newest solution without lists
a = input()
b = input()

transformed = a

for i in range(len(a)):
    transformed = b[0:i+1]
    transformed += a[i+1:]

    if transformed != a:
        print(transformed)
        a = transformed


# First ever solution
word1 = input()
word2 = input()

transform_list = [word1]
empty_string = ''

for i in range(len(word1)):
    list1 = list(word1)
    list2 = list(word2)

    list1[i] = list2[i]
    word1 = empty_string.join(list1)

    if word1 not in transform_list:
        transform_list.append(word1)
        print(word1)


# Without lists
word1 = input()
word2 = input()

previous_string = word1
current_string = ''

for i in range(len(word1)):
    for j in range(0, i + 1):
        current_string += word2[j]

    for j in range(i + 1, len(word1)):
        current_string += word1[j]

    if current_string != previous_string:
        print(current_string)
        previous_string = current_string
    current_string = ''


# One of the newer solutions
original_string = input()
desired_string = input()

unique_elements = []

list1 = list(original_string)
list2 = list(desired_string)

for i in range(len(original_string)):
    list1[i] = list2[i]
    mutated_word = ''.join(list1)

    if mutated_word not in unique_elements and mutated_word != original_string:
        unique_elements.append(mutated_word)

print('\n'.join(unique_elements))
