products = {}

while True:
    product_info = input()

    if product_info == 'buy':
        break

    product_info = product_info.split()
    name = product_info[0]
    price = float(product_info[1])
    quantity = int(product_info[2])

    single_product = {
        'price': price,
        'quantity': quantity
    }

    if name not in products:
        products[name] = single_product
    else:
        products[name]['price'] = price
        products[name]['quantity'] += quantity

for key, values in products.items():
    total_price = f"{values['price'] * values['quantity']:.2f}"
    print(key, '->', total_price)