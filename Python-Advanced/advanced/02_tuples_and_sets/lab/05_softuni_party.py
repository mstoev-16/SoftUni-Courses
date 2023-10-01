guests = set()

for _ in range(int(input())):
    number = input()
    if len(number) == 8:
        guests.add(number)

while True:
    number = input()

    if number == 'END':
        break

    if len(number) == 8:
        guests.discard(number)

print(len(guests))
print(*sorted(guests), sep='\n')