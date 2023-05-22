orders = int(input())
total_cost = 0

for i in range(orders):

    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if 0.01 <= price_per_capsule <= 100 and 1 <= days <= 31 and 1 <= capsules_per_day <= 2000:
        order_cost = price_per_capsule * days * capsules_per_day
        print(f'The price for the coffee is: ${order_cost:.2f}')
        total_cost += order_cost

print(f'Total: ${total_cost:.2f}')