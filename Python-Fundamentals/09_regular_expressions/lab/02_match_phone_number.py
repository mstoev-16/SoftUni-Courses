import re

data = input()
pattern = r'\+359-2-[0-9]{3}-[0-9]{4}\b|\+359 2 [0-9]{3} [0-9]{4}\b'

valid_phone_numbers = re.findall(pattern, data)
print(', '.join(valid_phone_numbers))


# with iterables
data = input()
pattern = r'(\+359-2-[0-9]{3}-[0-9]{4}\b)|(\+359 2 [0-9]{3} [0-9]{4}\b)'

valid_phone_numbers = re.finditer(pattern, data)
valid_phone_numbers = [phone.group(0) for phone in valid_phone_numbers]
print(', '.join(valid_phone_numbers))
# print(*valid_phone_numbers, sep=', ')


# with groups
data = input()
pattern = r'(^|(?<=\s))(?P<country_code>\+359)(?P<separator>(/|-))(?P<area_code>2)' \
          r'(?P=separator)(?P<second_last_digits>[0-9]{3})(?P=separator)(?P<last_digits>[0-9]{4})($|(?=\s))'

valid_phone_numbers = re.finditer(pattern, data)

for phone in valid_phone_numbers:
    phone = phone.groupdict()
    country_code = phone['country_code']
    separator = phone['separator']
    area_code = phone['area_code']
    second_last_digits = phone['second_last_digits']
    last_digits = phone['last_digits']
    print(f"{country_code}{separator}{area_code}{separator}{second_last_digits}{separator}{last_digits}")