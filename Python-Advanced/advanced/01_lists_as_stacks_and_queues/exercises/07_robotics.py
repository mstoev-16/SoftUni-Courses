from collections import deque


def convert_str_to_seconds(string):
    hours, minutes, seconds = [int(x) for x in string.split(':')]
    return (hours * 3600) + (minutes * 60) + seconds


def convert_sec_to_str(seconds):
    seconds %= 24 * 3600
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return f"[{hours:02d}:{minutes:02d}:{seconds:02d}]"


robots_data = {}
robots_occupied_data = {}
robots = input().split(';')

for data in robots:
    name, process_time = data.split('-')
    robots_data[name] = int(process_time)
    robots_occupied_data[name] = -1

start_time = input()
items = deque()
time = convert_str_to_seconds(start_time)

while True:
    item = input()
    if item == 'End':
        break
    else:
        items.append(item)

while True:
    time += 1
    current_item = items.popleft()

    for name, process_time in robots_occupied_data.items():
        if process_time <= time:
            robots_occupied_data[name] = time + robots_data[name]
            print(f"{name} - {current_item} {convert_sec_to_str(time)}")
            break
    else:
        items.append(current_item)

    if not items:
        break