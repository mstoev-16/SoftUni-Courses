def move_up(row, col):
    return row - 1, col


def move_down(row, col):
    return row + 1, col


def move_left(row, col):
    return row, col - 1


def move_right(row, col):
    return row, col + 1


def leaves_wonderland(row, col, matrix):
    return row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix)


directions = {
    'up': move_up,
    'down': move_down,
    'left': move_left,
    'right': move_right
}


n = int(input())
wonderland = [[el for el in input().split()] for _ in range(n)]
tea_bags = 0

for i in range(n):
    for j in range(n):
        if wonderland[i][j] == 'A':
            alice_x = i
            alice_y = j

while True:
    command = input()

    step = directions[command]
    current_x, current_y = step(alice_x, alice_y)
    wonderland[alice_x][alice_y] = '*'

    if leaves_wonderland(current_x, current_y, wonderland):
        print("Alice didn't make it to the tea party.")
        break
    elif wonderland[current_x][current_y] == 'R':
        wonderland[current_x][current_y] = '*'
        print("Alice didn't make it to the tea party.")
        break

    alice_x, alice_y = current_x, current_y
    if wonderland[current_x][current_y].isdigit():
        tea_bags += int(wonderland[current_x][current_y])

    if tea_bags >= 10:
        wonderland[alice_x][alice_y] = '*'
        print("She did it! She went to the party.")
        break

for line in (wonderland):
    print(*line)
















