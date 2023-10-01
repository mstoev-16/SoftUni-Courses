import sys
n = int(input())
field = [[el for el in input().split()] for _ in range(n)]
max_eggs = -sys.maxsize
best_positions = []


def valid_position(row, col, matrix):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix)


def move_up(row, col):
    return row - 1, col


def move_down(row, col):
    return row + 1, col


def move_left(row, col):
    return row, col - 1


def move_right(row, col):
    return row, col + 1


directions = {
    'up': move_up,
    'down': move_down,
    'left': move_left,
    'right': move_right
}

# Determine bunny coordinates
for i in range(n):
    for j in range(n):
        if field[i][j] == 'B':
            x = i
            y = j

    best_direction = None
for direction, step in directions.items():
    temp_eggs = 0

    temp_positions = []
    temp_x, temp_y = x, y

    while True:
        temp_x, temp_y = step(temp_x, temp_y)

        if not valid_position(temp_x, temp_y, field) or field[temp_x][temp_y] == 'X':
            break

        temp_eggs += int(field[temp_x][temp_y])
        temp_positions.append([temp_x, temp_y])

    if temp_eggs > max_eggs and temp_positions:
        max_eggs = temp_eggs
        best_direction = direction
        best_positions = temp_positions

print(best_direction)
print(*best_positions, sep='\n')
print(max_eggs)