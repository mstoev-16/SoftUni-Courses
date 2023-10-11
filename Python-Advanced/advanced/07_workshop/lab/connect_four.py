class ColumnFullError(Exception):
    pass


def valid_column(entered_column, column_limit):
    return 0 <= entered_column < column_limit


def valid_coordiantes(row, col, row_limit, col_limit):
    return 0 <= row < row_limit and 0 <= col < col_limit


def place_player_dot(matrix, selected_col, row_limit, player):
    for row in range(row_limit - 1, -1, -1):
        if matrix[row][selected_col] == 0:
            matrix[row][selected_col] = player
            return row, selected_col
    else:
        raise ColumnFullError


def count_initial_step_dots(matrix, row, col, row_limit, col_limit, step_row, step_col, player):
    dots = 1
    for i in range(1, 4):
        temp_row = row + step_row * i
        temp_col = col + step_col * i
        if not valid_coordiantes(temp_row, temp_col, row_limit, col_limit):
            break
        if matrix[temp_row][temp_col] != player:
            break
        dots += 1
    return dots


def count_opposite_step_dots(matrix, row, col, row_limit, col_limit, step_row, step_col, player):
    dots = 0
    for i in range(1, 4):
        temp_row = row - step_row * i
        temp_col = col - step_col * i
        if not valid_coordiantes(temp_row, temp_col, row_limit, col_limit):
            break
        if matrix[temp_row][temp_col] != player:
            break
        dots += 1
    return dots


def check_for_win(matrix, row, col, row_limit, col_limit, steps, player):
    for step_row, step_col in directions:
        initial_step_dots = count_initial_step_dots(matrix, row, col, row_limit, col_limit, step_row, step_col, player)
        opposite_step_dots = count_opposite_step_dots(matrix, row, col, row_limit, col_limit, step_row, step_col, player)
        if initial_step_dots + opposite_step_dots >= 4:
            return True
    return False


def print_matrix(matrix):
    for row in matrix:
        print(row)


ROWS = 6
COLUMNS = 7
player_n = 1
field = [[0] * COLUMNS for _ in range(ROWS)]

directions = (
    (-1, 0),  # Up
    (0, -1),  # Left
    (-1, -1), # Up-Left
    (1, -1)  # Down-Left
)

while True:
    try:
        chosen_column = int(input(f'Player {player_n}, choose a column.\n'))
        chosen_column -= 1
        if not valid_column(chosen_column, COLUMNS):
            raise ValueError
        current_row, current_col = place_player_dot(field, chosen_column, ROWS, player_n)
    except ValueError:
        print(f'Invalid input! Enter a column number in the range 1-{COLUMNS}.')
        continue
    except ColumnFullError:
        print('Column full! Choose another one.')
        continue
    print_matrix(field)
    if check_for_win(field, current_row, current_col, ROWS, COLUMNS, directions, player_n):
        print(f'Player {player_n} won!')
        break

    if player_n == 1:
        player_n = 2
    else:
        player_n = 1