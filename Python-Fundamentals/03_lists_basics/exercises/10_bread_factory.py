# First time solving
events = input().split('|')
coins = 100
energy = 100
gained_energy = 0

for event in events:
    task, task_value = event.split('-')
    task_value = int(task_value)

    if task == 'rest':
        if task_value + energy > 100:
            gained_energy = 100 - energy
        else:
            gained_energy = task_value

        energy += gained_energy
        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {energy}.')

    elif task == 'order':
        if energy < 30:
            energy += 50
            print('You had to rest!')
        else:
            energy -= 30
            coins += task_value
            print(f'You earned {task_value} coins.')

    else:
        if coins >= task_value:
            coins -= task_value
            print(f'You bought {task}.')
        else:
            print(f'Closed! Cannot afford {task}.')
            break
else:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')


# Two months later...
daily_events = input().split('|')
coins = 100
energy = 100

for data in daily_events:
    temp = data.split('-')
    event = temp[0]
    event_value = int(temp[1])

    if event == 'rest':
        if energy == 100:
            gained_energy = 0
        elif energy + event_value > 100:
            gained_energy = 100 - energy
        else:
            gained_energy = event_value

        energy += gained_energy
        print(f'You gained {gained_energy} energy.\n'
              f'Current energy: {energy}.')

    elif event == 'order':
        if energy >= 30:
            energy -= 30
            coins += event_value
            result = f'You earned {event_value} coins.'
        else:
            energy += 50
            result = 'You had to rest!'
        print(result)

    else:
        if coins >= event_value:
            coins -= event_value
            print(f'You bought {event}.')
        else:
            print(f'Closed! Cannot afford {event}.')
            break

else:
    print(f'Day completed!\n'
          f'Coins: {coins}\n'
          f'Energy: {energy}')

