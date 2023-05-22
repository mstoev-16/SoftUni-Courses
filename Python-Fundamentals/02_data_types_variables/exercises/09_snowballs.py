import sys
best_value = -sys.maxsize

n = int(input())

for _ in range(n):
    snowball_weight, snowball_time, snowball_quality = int(input()), int(input()), int(input())

    snowball_value = (snowball_weight / snowball_time) ** snowball_quality

    if snowball_value > best_value:
        best_value = snowball_value
        best_weight = snowball_weight
        best_time = snowball_time
        best_quality = snowball_quality

print(f'{best_weight} : {best_time} = {best_value:.0f} ({best_quality})')




