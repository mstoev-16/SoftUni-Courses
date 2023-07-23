import re

total_price = 0
furniture = []
pattern = r'(^|(?<=\s))>>(?P<product>[a-zA-Z]+)<<(?P<price>([0]|[1-9][0-9]*)(\.\d+)?)\!(?P<quantity>\d+)+$'

while True:
    data = input()
    if data == 'Purchase':
        break

    furniture_info = re.finditer(pattern, data)
    if furniture_info:
        for el in furniture_info:
            el = el.groupdict()
            product = el['product']
            price = float(el['price'])
            quantity = int(el['quantity'])

            furniture.append(product)
            total_price += price * quantity

print('Bought furniture:')
for item in furniture:
    print(item)
print(f"Total money spend: {total_price:.2f}")