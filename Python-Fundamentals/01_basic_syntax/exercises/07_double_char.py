while True:
    word = input()

    if word == 'End':
        break
    elif word == 'SoftUni':
        pass
    else:
        for i in range(len(word)):
            print(word[i] * 2, end='')
        print()


# Alternative way (python is dynamic...no need for a separate var here...)
# while True:
#     doubled_string = ''
#     a_string = input()
#
#     if a_string == 'End':
#         break
#     elif a_string == 'SoftUni':
#         pass
#     else:
#         for i in range(len(a_string)):
#             doubled_string += a_string[i] * 2
#         print(doubled_string)
