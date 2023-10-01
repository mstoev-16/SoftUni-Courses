sequence1 = {int(x) for x in input().split()}
sequence2 = {int(x) for x in input().split()}

for _ in range(int(input())):
    command = input()

    if command == 'Check Subset':
        if sequence1.issubset(sequence2) or sequence2.issubset(sequence1):
            print(True)
        else:
            print(False)
        continue

    action, object, sequence = command.split(' ', 2)
    sequence = {int(x) for x in sequence.split()}

    if action == 'Add':
        if object == 'First':
            sequence1 = sequence1.union(sequence)
        elif object == 'Second':
            sequence2 = sequence2.union(sequence)
    elif action == 'Remove':
        if object == 'First':
            sequence1 -= sequence
        elif object == 'Second':
            sequence2 -= sequence

print(*sorted(sequence1), sep=', ')
print(*sorted(sequence2), sep=', ')

