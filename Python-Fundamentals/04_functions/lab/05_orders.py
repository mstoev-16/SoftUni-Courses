def items(item, quantity):
    price = 0
    if item == 'coffee':
        price = 1.50 * quantity
    elif item == 'water':
        price = 1.00 * quantity
    elif item == 'coke':
        price = 1.40 * quantity
    elif item == 'snacks':
        price = 2.00 * quantity

    print(f'{price:.2f}')


items(input(), int(input()))