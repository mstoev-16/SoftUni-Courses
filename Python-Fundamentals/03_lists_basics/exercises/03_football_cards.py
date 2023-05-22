A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

flag = False

red_cards = input()

cards_list = red_cards.split()

for element in cards_list:

    if len(A) < 7 or len(B) < 7:
        flag = True
        break

    second_list = element.split('-')

    team = second_list[0]
    player = int(second_list[1])

    if team == 'A':
        if player in A:
            A.remove(player)
    elif team == 'B':
        if player in B:
            B.remove(player)

print(f'Team A - {len(A)}; Team B - {len(B)}')
if flag:
    print('Game was terminated')
