key_string = input()
editable_string = input()

while key_string in editable_string:
    editable_string = editable_string.replace(key_string, '')

print(editable_string)