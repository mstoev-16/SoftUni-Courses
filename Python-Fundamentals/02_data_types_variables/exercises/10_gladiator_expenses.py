lost_fights = int(input())
helmet_price, sword_price, shield_price, armor_price = float(input()), float(input()), float(input()), float(input())

broken_helmet = 0
broken_sword = 0
broken_shield = 0
broken_armor = 0
repair_costs = 0
temp_broken_shield = 0

for lost_fight in range(1, lost_fights + 1):
    if lost_fight % 2 == 0:
        broken_helmet += 1
    if lost_fight % 3 == 0:
        broken_sword += 1
    if lost_fight % 6 == 0:
        broken_shield += 1
        temp_broken_shield += 1

    if broken_shield % 2 == 0 and broken_shield != 0:
        broken_shield = 0
        broken_armor += 1

broken_shield = temp_broken_shield

repair_costs = broken_helmet * helmet_price + broken_sword * sword_price \
               + broken_shield * shield_price + broken_armor * armor_price

print(f'Gladiator expenses: {repair_costs:.2f} aureus')