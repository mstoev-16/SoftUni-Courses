def items(item, quantity):
    if item == 'coffee':
        price = 1.50 * quantity
    elif item == 'water':
        price = 1.00 * quantity
    elif item == 'coke':
        price = 1.40 * quantity
    elif item == 'snacks':
        price = 2.00 * quantity

    print(f'{price:.2f}')


input_item = input()
input_quantity = int(input())

items(input_item, input_quantity)