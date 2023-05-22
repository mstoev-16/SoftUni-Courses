year = int(input())

while True:

    year += 1

    number = str(year)
    if len(set(number)) == len(str(year)):
        print(year)
        break
