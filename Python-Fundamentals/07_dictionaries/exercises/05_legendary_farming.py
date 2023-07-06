weapons = {'shards': 'Shadowmourne',
           'fragments': 'Valanyr',
           'motes': 'Dragonwrath'}

key_materials = {
    'shards': 0,
    'fragments': 0,
    'motes': 0
}

junk_materials = {}
is_obtained = False

while True:
    materials = input().split()

    for i in range(0, len(materials), 2):
        quantity = int(materials[i])
        material = materials[i + 1].lower()
        if material in key_materials:
            key_materials[material] += quantity
        else:
            if material in junk_materials:
                junk_materials[material] += quantity
            else:
                junk_materials[material] = quantity

        for material, quantity in key_materials.items():
            if key_materials[material] >= 250:
                print(f"{weapons[material]} obtained!")
                key_materials[material] -= 250
                is_obtained = True
                break
        if is_obtained:
            break
    if is_obtained:
        break

for material, quantity in key_materials.items():
    print(f"{material}: {quantity}")
for material, quantity in junk_materials.items():
    print(f"{material}: {quantity}")