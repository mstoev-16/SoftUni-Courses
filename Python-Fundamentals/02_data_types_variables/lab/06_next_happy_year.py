# year = int(input())
#
# while True:
#
#     year += 1
#
#     number = str(year)
#     if len(set(number)) == len(str(year)):
#         print(year)
#         break
#
#

year = int(input())

while True:
    year += 1

    set_year = set(str(year))
    if len(set_year) == len(str(year)):
        break

print(year)