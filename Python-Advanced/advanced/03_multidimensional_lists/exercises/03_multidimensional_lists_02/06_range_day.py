def move_up(row, col, step):
    return row - step, col


def move_down(row, col, step):
    return row + step, col


def move_left(row, col, step):
    return row, col - step


def move_right(row, col, step):
    return row, col + step


def invalid_position(row, col, matrix):
    return row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix)


directions = {
    'up': move_up,
    'down': move_down,
    'left': move_left,
    'right': move_right
}

n = 5
square = [[el for el in input().split()] for _ in range(n)]
targets = 0
targets_shot = 0
target_positions = []

for i in range(n):
    for j in range(n):
        if square[i][j] == 'A':
            x = i
            y = j
        if square[i][j] == 'x':
            targets += 1

for _ in range(int(input())):
    command = input().split()
    action, direction = command[0], command[1]

    if action == 'move':
        steps = int(command[2])
        move = directions[direction]
        current_x, current_y = move(x, y, steps)

        if invalid_position(current_x, current_y, square) or square[current_x][current_y] == 'x':
            continue

        square[x][y] = '.'
        x, y = current_x, current_y
        square[x][y] = 'A'

    elif action == 'shoot':
        current_x, current_y = x, y
        shoot = directions[direction]

        while True:
            current_x, current_y = shoot(current_x, current_y, 1)
            if invalid_position(current_x, current_y, square):
                break

            if square[current_x][current_y] == 'x':
                targets_shot += 1
                square[current_x][current_y] = '.'
                target_positions.append([current_x, current_y])
                break

        if targets == targets_shot:
            break

if targets == targets_shot:
    print(f"Training completed! All {targets} targets hit.")
else:
    print(f"Training not completed! {targets - targets_shot} targets left.")

for line in target_positions:
    print(line)