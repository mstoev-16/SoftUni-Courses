class Player:
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign


def choose_board_size():
    while True:
        try:
            size = int(input('Choose board size that is at least 3: '))
            if size < 3:
                print('Number is out of border size range!')
                continue
            break
        except ValueError:
            print('Invalid input! Enter a number that is at least 3.')
    return size


def initialize_players():
    player_one_name = input('Player one name: ')
    player_two_name = input('Player two name: ')

    while True:
        player_one_sign = input(f"{player_one_name}, would you like to play with 'X' or 'O'? ").upper()
        if player_one_sign in available_signs:
            player_two_sign = 'O' if player_one_sign == 'X' else 'X'
            break
        print(f"Invalid sign!")
    return Player(player_one_name, player_one_sign), Player(player_two_name, player_two_sign)


def print_enumerated_board(size):
    enumerated_board = []
    cnt = 0
    for i in range(size):
        temp_line = []
        for j in range(size):
            cnt += 1
            temp_line.append(cnt)
        enumerated_board.append(temp_line)

    for line in enumerated_board:
        print(f"| {' | '.join([str(x) for x in line])} |")


def initial_board(size):
    matrix = []
    for _ in range(size):
        matrix.append([None] * size)
    return matrix


def map_board(size):
    mapped_board = {}
    position = 1

    for i in range(size):
        for j in range(size):
            mapped_board[position] = [i, j]
            position += 1
    return mapped_board


def valid_position(matrix, board_mapping, position, size):
    if position < 1 or position > size * size:
        return False
    row_to_check, col_to_check = board_mapping[position]
    return matrix[row_to_check][col_to_check] is None


def print_board(matrix):
    for i in matrix:
        temp_list = []
        for j in i:
            if not j:
                temp_list.append(' ')
            else:
                temp_list.append(j)
        print(f"| {' | '.join([str(x) for x in temp_list])} |")


def check_for_win(matrix, size, sign):
    # rows
    for row in matrix:
        if all([x == sign for x in row]):
            return True

    # cols
    for row in range(len(matrix)):
        col_win = True
        for col in range(len(matrix)):
            if matrix[row][col] != sign:
                col_win = False
                break
        if col_win:
            return True

    # diagonals
    left_diagonal_win = True
    right_diagonal_win = True
    for i in range(len(matrix)):
        if matrix[i][i] != sign:
            left_diagonal_win = False
        if matrix[i][size - i - 1] != sign:
            right_diagonal_win = False
    return left_diagonal_win or right_diagonal_win


available_signs = ['X', 'O']

board_size = choose_board_size()
player_one, player_two = initialize_players()
print_enumerated_board(board_size)
board = initial_board(board_size)
mapping = map_board(board_size)

print(f'{player_one.name} starts first!')

turn = 1
while True:
    current_player = player_one if turn % 2 != 0 else player_two
    current_position = int(input(f'{current_player.name}, choose a free position [1-{board_size * board_size}]: '))
    if not valid_position(board, mapping, current_position, board_size):
        continue
    chosen_row, chosen_col = mapping[current_position]
    board[chosen_row][chosen_col] = current_player.sign
    print_board(board)

    if check_for_win(board, board_size, current_player.sign):
        print(f'{current_player.name} has won!')
        break
    turn += 1

    if turn > board_size * board_size:
        print("It's a draw!")
        break
