import re
pattern1 = r'(^|(?<=\s))www.[a-zA-Z0-9]+[-]?[a-z0-9]+\.[a-z]+((\.[a-z]+)*)?($|(?=[\s\.\!\?\,\-]))'
pattern2 = r'(^|(?<=\s))(?!.*\.\d+$)www\.[a-zA-Z0-9]+[-]?[a-z0-9]+\.[a-z]+((\.[a-z]+)*)?($|(?=[\s.,!?-]))'
pattern3 = r'(www.[a-zA-Z0-9-\.]+\.[a-z]+(\.[a-z]+)?)'
data = input()
while True:
    if data:
        domain = re.finditer(pattern3, data)
        for el in domain:
            print(el.group())
    else:
        break

    data = input()
