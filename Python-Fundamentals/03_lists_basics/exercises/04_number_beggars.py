money = input().split(', ')
beggars = int(input()) * [0]

beggar = 0
for cash in money:
    if beggar == len(beggars):
        beggar = 0

    beggars[beggar] += int(cash)
    beggar += 1

print(beggars)
