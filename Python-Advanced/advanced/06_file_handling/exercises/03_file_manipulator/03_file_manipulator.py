from os import path, remove


def create_file(file_name):
    open(f'{file_name}', 'w').close()


def add_content(file_name, content):
    with open(f'{file_name}', 'a') as file:
        file.write(f'{content}\n')


def replace_string(file_name, first_string, second_string):
    if path.exists(file_name):
        with open(file_name, 'r+') as old_file:
            new_file = old_file.read().replace(first_string, second_string)
            old_file.seek(0)
            old_file.truncate()
            old_file.write(new_file)
    else:
        print('An error occurred')


def delete_file(file_name):
    if path.exists(f'{file_name}'):
        remove(file_name)
    else:
        print('An error occurred')


while True:
    command = input()
    if command == 'End':
        break

    command_arguments = command.split('-')
    action = command_arguments[0]
    target_file = command_arguments[1]

    if action == 'Create':
        create_file(target_file)
    elif action == 'Add':
        text = command_arguments[2]
        add_content(target_file, text)
    elif action == 'Replace':
        old_string, new_string = command_arguments[2], command_arguments[3]
        replace_string(target_file, old_string, new_string)
    elif action == 'Delete':
        delete_file(target_file)
