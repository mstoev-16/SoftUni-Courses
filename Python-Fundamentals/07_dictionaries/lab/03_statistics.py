products = {}

while True:
    command = input()
    if command == 'statistics':
        break
    else:
        command = command.split()
        product = command[0]
        quantity = int(command[1])

        if product not in products:
            products[product] = quantity
        else:
            products[product] += quantity

print(f"Products in stock:")
for product, quantity in products.items():
    print(f"- {product} {quantity}")
print(f"Total Products: {len(products.keys())}\n"
      f"Total Quantity: {sum(products.values())}")