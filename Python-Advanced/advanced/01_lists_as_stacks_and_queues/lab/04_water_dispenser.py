from collections import deque

water_queue = deque()
water = int(input())
start = False

while True:
    name = input()
    if name == 'End':
        break

    if name == 'Start':
        start = True
        continue

    if not start:
        water_queue.appendleft(name)
        continue

    if name.startswith('refill '):
        name = name.split()
        refilled = int(name[1])
        water += refilled
    elif name.isdigit():
        quantity = int(name)
        if quantity > water:
            print(f"{water_queue.pop()} must wait")
        else:
            print(f"{water_queue.pop()} got water")
            water -= quantity

print(f"{water} liters left")