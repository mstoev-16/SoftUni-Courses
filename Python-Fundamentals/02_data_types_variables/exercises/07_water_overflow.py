CAPACITY = 255

n = int(input())
liters_filled = 0

for _ in range(n):
    liters = int(input())

    if liters_filled + liters <= 255:
        liters_filled += liters
    else:
        print("Insufficient capacity!")

print(liters_filled)