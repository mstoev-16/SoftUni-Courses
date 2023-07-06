force_users = {}
force_sides = {}

while True:
    command = input()

    if command == "Lumpawaroo":
        break

    if ' | ' in command:
        [force_side, force_user] = command.split(' | ')
        if force_user not in force_users and force_side not in force_sides:
            force_users[force_user] = force_side
            force_sides[force_side] = [force_user]
        elif force_user not in force_users and force_side in force_sides:
            force_sides[force_side].append(force_user)
            force_users[force_user] = force_side

    elif ' -> ' in command:
        [force_user, force_side] = command.split(' -> ')
        if force_user not in force_users and force_side not in force_sides:
            force_users[force_user] = force_side
            force_sides[force_side] = [force_user]
        elif force_user not in force_users and force_side in force_sides:
            force_users[force_user] = force_side
            force_sides[force_side].append(force_user)
        elif force_user in force_users and force_side in force_sides:
            removed_side = force_users[force_user]
            del force_users[force_user]
            force_sides[removed_side].remove(force_user)
            force_users[force_user] = force_side
            force_sides[force_side].append(force_user)

            if not force_sides[removed_side]:
                force_sides.pop(removed_side)

        print(f"{force_user} joins the {force_side} side!")

for force_side in force_sides.keys():
    print(f"Side: {force_side}, Members: {len(force_sides[force_side])}")
    for force_user in force_sides[force_side]:
        print('!', force_user)
