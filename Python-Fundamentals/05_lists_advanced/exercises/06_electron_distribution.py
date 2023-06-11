n_electrons = int(input())

filled_shells = []
n = 0

while True:
    if n_electrons == 0:
        break

    n += 1
    possible_electrons = 2 * n ** 2

    if n_electrons > possible_electrons:
        filled_shells.append(possible_electrons)
        n_electrons -= possible_electrons
    else:
        filled_shells. append(n_electrons)
        n_electrons = 0

print(filled_shells)

#
# electrons = int(input())
# distributed = []
# shield = 1
#
# while electrons > 0:
#     el_per_shield = 2 * shield ** 2
#
#     if electrons >= el_per_shield:
#         distributed.append(el_per_shield)
#         electrons -= el_per_shield
#         shield += 1
#     elif 0 < electrons < el_per_shield:
#         distributed.append(electrons)
#         electrons = 0
#
# print(distributed)