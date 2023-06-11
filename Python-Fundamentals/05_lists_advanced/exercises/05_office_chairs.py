rooms = int(input())

free_chair = 0
flag = True

for room in range(1, rooms + 1):
    data = input().split()
    chairs = len(data[0])
    people = int(data[1])

    if chairs > people:
        free_chair += chairs - people
    elif people > chairs:
        flag = False
        print(f'{people - chairs} more chairs needed in room {room}')

if flag:
    print(f'Game On, {free_chair} free chairs left')


# n = int(input())
# flag = True
# free_chairs = 0
#
# for i in range(n):
#     data = input().split()
#
#     chairs = len(data[0])
#     needed_charis = int(data[1])
#
#     if chairs < needed_charis:
#         flag = False
#         print(f"{needed_charis - chairs} more chairs needed in room {i + 1}")
#     else:
#         free_chairs += chairs - needed_charis
#
# if flag:
#     print(f'Game On, {free_chairs} free chairs left')