phonebook ={}

while True:
    phone_info = input()

    if phone_info.isnumeric():
        phone_info = int(phone_info)
        break

    [name, phone] = phone_info.split('-')

    if name not in phonebook:
        phonebook[name] = phone
    else:
        phonebook[name] = phone

for _ in range(phone_info):
    name = input()

    if name in phonebook:
        print(name, '->', phonebook[name])
    else:
        print(f'Contact {name} does not exist.')