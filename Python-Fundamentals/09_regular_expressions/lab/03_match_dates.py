import re

# with findall
data = input()
pattern = r'(\d{2})([\/\.-])([A-Z][a-z]{2})\2(\d{4})'
dates = re.findall(pattern, data)

for match in dates:
    day = match[0]
    month = match[2]
    year = match[3]
    print(f"Day: {day}, Month: {month}, Year: {year}")

# with finditer
data = input()
pattern = r'(\d{2})([\/\.-])([A-Z][a-z]{2})\2(\d{4})'
dates = re.finditer(pattern, data)

for date in dates:  # dates are a class
    day = date.group(1)
    month = date.group(3)
    year = date.group(4)
    print(f"Day: {day}, Month: {month}, Year: {year}")


# with named groups
data = input()
pattern = r'(?P<day>\d{2})(?P<separator>[\./-])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})'
dates = re.finditer(pattern, data)

for date in dates:
    date = date.groupdict()
    print(f"Day: {date['day']}, Month: {date['month']}, Year: {date['year']}")
