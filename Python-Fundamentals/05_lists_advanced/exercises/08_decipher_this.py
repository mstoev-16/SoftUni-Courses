# secret_message = input().split()
#
# deciphered = []
# temp_el = ''
# for el in secret_message:
#     for i in range(len(el)):
#         if (el[i]).isdigit():
#             temp_el += el[i]
#         else:
#             break
#     temp_el = chr(int(temp_el))
#
#     for i in range(len(el)):
#         if not (el[i]).isdigit():
#             temp_el += el[i]
#
#     temp_el = list(temp_el)
#     temp_el[1], temp_el[-1] = temp_el[-1], temp_el[1]
#     deciphered.append(''.join(temp_el))
#     temp_el = ''
# print(' '.join(deciphered))


# Improved Version
# encoded_message = input().split()
# deciphered = []
# for word in encoded_message:
#     digits = ''
#     letters = ''
#
#     digits = ''.join(list(filter(lambda x: x.isdigit(), word)))
#     letters = list(filter(lambda x: x.isalpha(), word))
#
#     letters.insert(0, chr(int(digits)))
#     letters[1], letters[-1] = letters[-1], letters[1]
#     deciphered.append(''.join(letters))
#
# print(' '.join(deciphered))

