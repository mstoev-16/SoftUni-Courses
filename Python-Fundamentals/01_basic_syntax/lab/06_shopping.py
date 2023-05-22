budget = int(input())

while True:
    command = input()

    if command == 'End':
        result = 'You bought everything needed.'
        break

    price = int(command)

    if budget >= price:
        budget -= price
    else:
        result = 'You went in overdraft!'
        break

print(result)
