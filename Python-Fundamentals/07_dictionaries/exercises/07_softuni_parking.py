parking_data = {}

for _ in range(int(input())):
    command = input()

    command = command.split()
    name = command[1]

    if command[0] == 'register':
        license_plate = command[2]
        if name not in parking_data:
            parking_data[name] = license_plate
            result = f"{name} registered {license_plate} successfully"
        else:
            result = f"ERROR: already registered with plate number {license_plate}"
    elif command[0] == 'unregister':
        if name not in parking_data:
            result = f"ERROR: user {name} not found"
        else:
            result = f"{name} unregistered successfully"
            parking_data.pop(name)

    print(result)

for name, license_plate in parking_data.items():
    print(name, '=>', license_plate)