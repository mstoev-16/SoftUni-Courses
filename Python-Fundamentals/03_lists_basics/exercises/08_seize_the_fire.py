HIGH_RANGE = range(81, 126)
MEDIUM_RANGE = range(51, 81)
LOW_RANGE = range(1, 51)

fire_cells = input().split('#')
water_amount = int(input())
effort = 0
total_fire = 0

put_out_fire = []

for fire in fire_cells:
    fire_type, fire_value = fire.split(' = ')
    fire_value = int(fire_value)

    if fire_type == 'High' and fire_value not in HIGH_RANGE:
        continue
    elif fire_type == 'Medium' and fire_value not in MEDIUM_RANGE:
        continue
    elif fire_type == 'Low' and fire_value not in LOW_RANGE:
        continue

    if water_amount >= fire_value:
        water_amount -= fire_value
        effort += 0.25 * fire_value
        total_fire += fire_value

        put_out_fire.append(fire_value)

print('Cells:')

for i in range(len(put_out_fire)):
    print(f' - {put_out_fire[i]}')

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')


# Another way
fire_data = input().split('#')
water_amount = int(input())

LOW_FIRE = range(1, 51)
MEDIUM_FIRE = range(51, 81)
HIGH_FIRE = range(81, 126)

put_out = []
total_fire = 0
effort = 0

for fire in fire_data:
    temp_fire = fire.split(' = ')
    fire_type = temp_fire[0]
    fire_val = int(temp_fire[1])

    if fire_type == 'High' and fire_val not in HIGH_FIRE:
        continue
    elif fire_type == 'Medium' and fire_val not in MEDIUM_FIRE:
        continue
    elif fire_type == 'Low' and fire_val not in LOW_FIRE:
        continue

    if water_amount >= fire_val:
        water_amount -= fire_val
        put_out.append(fire_val)
        total_fire += fire_val
        effort += fire_val * 0.25

print('Cells:')
for fire in put_out:
    print(f' - {fire}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')
