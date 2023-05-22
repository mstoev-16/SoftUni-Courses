n = int(input())

for _ in range(n):
    entered_string = input()

    if '.' in entered_string or ',' in entered_string or '_' in entered_string:
        result = f'{entered_string} is not pure!'
    else:
        result = f'{entered_string} is pure.'

    print(result)


# Alternative way (better than above code if more char restrictions apply)
# n = int(input())
# impure_elements = ',._'
# for _ in range(n):
#     a_string = input()
#
#     for i in range(len(a_string)):
#         if a_string[i] in impure_elements:
#             result = f"{a_string} is not pure!"
#             break
#     else:
#         result = f"{a_string} is pure."
# #
# #     print(result)