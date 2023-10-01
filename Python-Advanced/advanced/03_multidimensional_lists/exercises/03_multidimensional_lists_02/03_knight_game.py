n = int(input())
board = [[el for el in input()] for _ in range(n)]
removed = 0


def check_in_board(row, col, matrix):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix)


def check_for_knight(row, col, matrix):
    return matrix[row][col] == 'K'


def count_conflicts(row, col, matrix):
    conflicts = 0
    if check_in_board(row + 1, col + 2, matrix) and check_for_knight(row + 1, col + 2, matrix):
        conflicts += 1
    if check_in_board(row + 1, col - 2, matrix) and check_for_knight(row + 1, col - 2, matrix):
        conflicts += 1
    if check_in_board(row - 1, col - 2, matrix) and check_for_knight(row - 1, col - 2, matrix):
        conflicts += 1
    if check_in_board(row - 1, col + 2, matrix) and check_for_knight(row - 1, col + 2, matrix):
        conflicts += 1
    if check_in_board(row + 2, col + 1, matrix) and check_for_knight(row + 2, col + 1, matrix):
        conflicts += 1
    if check_in_board(row + 2, col - 1, matrix) and check_for_knight(row + 2, col - 1, matrix):
        conflicts += 1
    if check_in_board(row - 2, col - 1, matrix) and check_for_knight(row - 2, col - 1, matrix):
        conflicts += 1
    if check_in_board(row - 2, col + 1, matrix) and check_for_knight(row - 2, col + 1, matrix):
        conflicts += 1
    return conflicts


while True:
    knights_pos = {}
    best_knight = None
    max_attacks = 0

    for i in range(n):
        for j in range(n):
            if board[i][j] == '0':
                continue

            knights_pos[(i, j)] = count_conflicts(i, j, board)

    for knight, attacks in knights_pos.items():
        if attacks > max_attacks:
            max_attacks = attacks
            best_knight = knight

    if not best_knight:
        break

    x, y = best_knight
    board[x][y] = '0'
    removed += 1

print(removed)