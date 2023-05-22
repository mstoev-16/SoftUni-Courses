tasks = 'dog cat coding movie'
coffees = 0
while True:
    task = input()

    if task == 'END':
        break

    if task.lower() in tasks:
        if task.isupper():
            coffees += 2
        elif task.islower():
            coffees += 1

if coffees <= 5:
    print(coffees)
else:
    print('You need extra sleep')