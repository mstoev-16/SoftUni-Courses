m, n = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(m)]


def valid_coordinates(r1, c1, r2, c2, m , n):
    return 0 <= r1 < m and 0 <= c1 <= n and 0 <= r2 < m and 0 <= c2 < n


while True:
    command = input()
    if command == 'END':
        break

    action, coordinates = command.split(' ', 1)
    coordinates = coordinates.split()
    if len(coordinates) != 4:
        print('Invalid input!')
        continue

    r1, c1, r2, c2 = [int(x) for x in coordinates]
    if action != 'swap' or not valid_coordinates(r1, c1, r2, c2, m, n):
        print('Invalid input!')
        continue

    matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]

    for line in matrix:
        print(*line)



