n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]


def valid_coordinates(row, col, size):
    return 0 <= row and row < size and 0 <= col and col < size


while True:
    command = input()
    if command == 'END':
        break

    action, temp = command.split(' ', 1)
    x, y, value = [int(x) for x in temp.split()]

    if not valid_coordinates(x, y, n):
        print('Invalid coordinates')
        continue

    if action == 'Add':
        matrix[x][y] += value
    elif action == 'Subtract':
        matrix[x][y] -= value

for line in matrix:
    print(*line)


