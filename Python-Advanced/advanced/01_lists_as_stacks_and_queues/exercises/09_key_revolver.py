from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = [int(bullet) for bullet in input().split()]
locks = deque([int(lock) for lock in input().split()])
intelligence = int(input())
mission_ended = False
bullets_used = 0

while True:
    if mission_ended:
        break
    for i in range(gun_barrel_size):
        if bullets:
            current_bullet = bullets.pop()
            if current_bullet > locks[0]:
                bullets_used += 1
                print('Ping!')
            else:
                locks.popleft()
                bullets_used += 1
                print('Bang!')
            if i == gun_barrel_size - 1 and bullets:
                print('Reloading!')
            if not locks:
                mission_ended = True
                break
        else:
            mission_ended = True
            break
if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${intelligence - bullet_price * bullets_used}")