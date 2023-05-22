n = int(input())

list_positives = []
list_negatives = []

for _ in range(n):
    number = int(input())

    if number >= 0:
        list_positives.append(number)
    else:
        list_negatives.append(number)

print(list_positives)
print(list_negatives)
print(f'Count of positives: {len(list_positives)}')
print(f'Sum of negatives: {sum(list_negatives)}')

