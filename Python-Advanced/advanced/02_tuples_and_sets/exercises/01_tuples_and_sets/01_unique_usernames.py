usernames = set()

for _ in range(int(input())):
    username = input()

    usernames.add(username)

print(*usernames, sep='\n')