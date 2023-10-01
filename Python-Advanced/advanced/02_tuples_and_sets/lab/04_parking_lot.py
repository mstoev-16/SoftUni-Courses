parking_lot = set()

for _ in range(int(input())):
    command, plate = input().split(', ')

    if command == 'IN':
        parking_lot.add(plate)
    elif command == 'OUT':
        parking_lot.discard(plate)

if parking_lot:
    print(*parking_lot, sep='\n')
else:
    print('Parking Lot is Empty')