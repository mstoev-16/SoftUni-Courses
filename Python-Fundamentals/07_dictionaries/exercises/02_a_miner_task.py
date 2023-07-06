metal_data = {}

while True:
    metal = input()

    if metal == 'stop':
        break

    metal_quantity = int(input())
    if metal not in metal_data:
        metal_data[metal] = metal_quantity
    metal_data[metal] += metal_quantity

for metal, quantity in metal_data.items():
    print(metal, '->', quantity)