# First way
MAX_PRICE_CLOTHES = 50.00
MAX_PRICE_SHOES = 35.00
MAX_PRICE_ACCESSORIES = 20.50
NEEDED_MONEY = 150

items_data = input().split('|')
budget = float(input())
new_prices = []
total_new_price = 0
money_spent = 0

for item in items_data:
    item_type, price = item.split('->')
    price = float(price)

    if item_type == 'Clothes' and price > MAX_PRICE_CLOTHES:
        continue
    elif item_type == 'Shoes' and price > MAX_PRICE_SHOES:
        continue
    elif item_type == 'Accessories' and price > MAX_PRICE_ACCESSORIES:
        continue

    if budget >= price:
        budget -= price
        money_spent += price
        new_price = 1.40 * price
        total_new_price += new_price
        new_prices.append(f'{new_price:.2f}')

budget += total_new_price

print(' '.join(new_prices))
print(f'Profit: {total_new_price - money_spent:.2f}')
if budget >= NEEDED_MONEY:
    print('Hello, France!')
else:
    print('Not enough money.')


# Slightly better way
item_collection = input().split('|')
budget = int(input())

MAX_CLOTHES_PRICE = 50.00
MAX_SHOES_PRICE = 35.00
MAX_ACCESSORIES_PRICE = 20.50
new_prices = []
selling_income = 0

for data in item_collection:
    temp = data.split('->')

    item_type = temp[0]
    item_price = float(temp[1])

    if item_type == 'Clothes' and item_price > MAX_CLOTHES_PRICE \
        or item_type == 'Shoes' and item_price > MAX_SHOES_PRICE \
            or item_type == 'Accessories' and item_price > MAX_ACCESSORIES_PRICE:
        continue

    if budget >= item_price:
        budget -= item_price
        new_prices.append(f'{1.4 * item_price:.2f}')

selling_income = sum([float(price) for price in new_prices])

print(' '.join(new_prices))
print(f'Profit: {selling_income - selling_income / 1.4:.2f}')
if selling_income + budget >= 150:
    result = 'Hello, France!'
else:
    result = 'Not enough money.'

print(result)






