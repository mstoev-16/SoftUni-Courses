from collections import deque

materials = [int(x) for x in input().split()]
magic_levels = deque([int(x) for x in input().split()])

presents = {
    'Doll': 0,
    'Wooden train': 0,
    'Teddy bear': 0,
    'Bicycle': 0
}

present_requirements = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}

while materials and magic_levels:
    box = materials.pop()
    level = magic_levels.popleft()

    if box == 0 and level == 0:
        continue
    if box == 0:
        magic_levels.appendleft(level)
        continue
    if level == 0:
        materials.append(box)
        continue

    result = box * level
    if result in present_requirements:
        present = present_requirements[result]
        presents[present] += 1
    elif result < 0:
        materials.append(box + level)
    else:
        materials.append(box + 15)

if presents['Doll'] and presents['Wooden train'] or presents['Teddy bear'] and presents['Bicycle']:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(material) for material in materials[::-1]])}")
if magic_levels:
    print(f"Magic left: {', '.join([str(level) for level in magic_levels])}")

for present, amount in sorted(presents.items()):
    if amount > 0:
        print(f'{present}: {amount}')