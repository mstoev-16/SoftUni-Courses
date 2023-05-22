# Smart way
divisor = int(input())
limit = int(input())

for i in range(limit, 0, -1):
    if i % divisor == 0:
        print(i)
        break


# Longer way...
# import sys
#
# max_number = -sys.maxsize
# divisor = int(input())
# boundary = int(input())
#
# for i in range(1, boundary + 1):
#     if i % divisor == 0 and boundary >= i > max_number:
#         max_number = i
#
# print(max_number)