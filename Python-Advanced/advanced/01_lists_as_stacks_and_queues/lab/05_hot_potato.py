from collections import deque

circle = deque(input().split())
tosses = int(input())
toss_n = 1

while len(circle) > 1:
    if toss_n == tosses:
        toss_n = 1
        print(f"Removed {circle.popleft()}")
    else:
        circle.rotate(-1)
        toss_n += 1

print(f"Last is {circle[0]}")