from collections import deque

circle = deque()
n = int(input())
idx = 0
tour_started = False

for _ in range(n):
    circle.append(input().split())

while True:
    tank = 0
    if tour_started:
        break
    for i in range(n):
        petrol, distance = [int(x) for x in circle[i]]
        tank += petrol
        if tank - distance < 0:
            circle.rotate(-1)
            idx += 1
            break
        else:
            tank -= distance
    else:
        tour_started = True

print(idx)