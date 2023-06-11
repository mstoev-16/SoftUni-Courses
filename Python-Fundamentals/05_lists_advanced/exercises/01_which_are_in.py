substrings = input().split(', ')
strings = input().split(', ')

result = [sub for sub in substrings for str in strings if sub in str]

print(sorted(set(result), key = result.index))


# Another way
# substrings = input().split(', ')
# strings = input().split(', ')
# occurring_substrings = []
#
# for substring in substrings:
#     for string in strings:
#         if substring in string and substring not in occurring_substrings:
#             occurring_substrings.append(substring)
#
# print(occurring_substrings)
