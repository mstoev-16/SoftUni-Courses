from collections import deque
bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
symbols = deque([el for el in input().split()])
operators = '+-*/'
honey = 0

while bees and nectar:
    bee = bees.popleft()
    nectar_drop = nectar.pop()

    if bee > nectar_drop:
        bees.appendleft(bee)
        continue

    symbol = symbols.popleft()
    if symbol == '/' and nectar_drop == 0:
        continue

    if symbol == '+':
        honey +=  abs(bee + nectar_drop)
    elif symbol == '-':
        honey +=  abs(bee - nectar_drop)
    elif symbol == '*':
        honey +=  abs(bee * nectar_drop)
    elif symbol == '/':
        honey +=  abs(bee / nectar_drop)

print(f"Total honey made: {honey}")

if bees:
    print('Bees left:', end=' ')
    print(*bees, sep=', ')
if nectar:
    print('Nectar left:', end=' ')
    print(*nectar, sep=', ')