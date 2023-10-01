from collections import deque

cups = deque([int(cup) for cup in input().split()])
bottles = deque([int(bottle) for bottle in input().split()])
wasted_water = 0

while cups and bottles:
    current_bottle = bottles.pop()

    if current_bottle < cups[0]:
        cups[0] -= current_bottle
    else:
        wasted_water += (current_bottle - cups[0])
        cups.popleft()

if bottles:
    print('Bottles:', end=' ')
    while bottles:
        bottle = bottles.popleft()
        if bottles:
            print(bottle, end=' ')
        else:
            print(bottle)
else:
    print('Cups:', end=' ')
    while cups:
        cup = cups.popleft()
        if cups:
            print(cup, end=' ')
        else:
            print(cup)

print(f"Wasted litters of water: {wasted_water}")