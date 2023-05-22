# Better way
n = int(input())

initial_list = []
filtered_list = []

for _ in range(n):
    element = int(input())
    initial_list.append(element)

filter_type = input()

for element in initial_list:

    if filter_type == 'even' and element % 2 == 0:
        filtered_list.append(element)
    if filter_type == 'odd' and not element % 2 == 0:
        filtered_list.append(element)
    if filter_type == 'positive' and element >= 0:
        filtered_list.append(element)
    if filter_type == 'negative' and element < 0:
        filtered_list.append(element)

print(filtered_list)


# A bit longer way
n = int(input())

initial_list, even_list, odd_list, positive_list, negative_list = [], [], [], [], []

for _ in range(n):
    element = int(input())
    initial_list.append(element)

    if element % 2 == 0:
        even_list.append(element)
    elif element % 2 != 0:
        odd_list.append(element)
    elif element >= 0:
        positive_list.append(element)
    elif element < 0:
        negative_list.append(element)

filter_type = input()
if filter_type == 'even':
    print(even_list)
elif filter_type == 'odd':
    print(odd_list)
elif filter_type == 'positive':
    print(positive_list)
elif filter_type == 'negative':
    print(negative_list)
