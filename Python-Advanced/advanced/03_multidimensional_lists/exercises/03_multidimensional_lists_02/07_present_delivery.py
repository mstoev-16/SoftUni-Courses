def go_up(row, col):
    return row - 1 , col


def go_down(row, col):
    return row + 1, col


def go_left(row, col):
    return row, col - 1


def go_right(row, col):
    return row, col + 1


def is_outside(row, col, matrix):
    return row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix)


directions = {
    'up': go_up,
    'down': go_down,
    'left': go_left,
    'right': go_right
}

presents = int(input())
size = int(input())
neighborhood = []
nice_kids = 0

for i in range(size):
    current_row = input().split()
    neighborhood.append(current_row)

    for j in range(len(current_row)):
        if current_row[j] == 'S':
            santa_x, santa_y = i, j
        if current_row[j] == 'V':
            nice_kids += 1

nice_kids_left = nice_kids

while True:
    command = input()
    if command == 'Christmas morning':
        break

    step = directions[command]
    current_x, current_y = step(santa_x, santa_y)

    if is_outside(current_x, current_y, neighborhood):
        continue

    neighborhood[santa_x][santa_y] = '-'
    santa_x, santa_y = current_x, current_y

    if neighborhood[santa_x][santa_y] == 'V':
        nice_kids_left -= 1
        presents -= 1
    elif neighborhood[santa_x][santa_y] == 'C':
        for step in directions.values():
            current_x, current_y = step(santa_x, santa_y)
            if neighborhood[current_x][current_y] != 'V' and neighborhood[current_x][current_y] != 'X':
                continue
            if neighborhood[current_x][current_y] == 'V':
                nice_kids_left -= 1
            presents -= 1
            neighborhood[current_x][current_y] = '-'

    neighborhood[santa_x][santa_y] = 'S'

    if presents == 0 or nice_kids_left == 0:
        break

if presents == 0 and nice_kids_left > 0:
    print("Santa ran out of presents!")
for current_row in neighborhood:
    print(*current_row, sep=' ')
if nice_kids_left == 0:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_left} nice kid/s.")