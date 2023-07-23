string = list(input())

caesar_encryption = [chr(ord(el) + 3) for el in string]
print(''.join(caesar_encryption))