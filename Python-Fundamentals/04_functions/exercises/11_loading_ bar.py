# def loading_bar(percent):
#     times = percent // 10
#     progress = '%'
#     remaining = '.'
#
#     if percent != 100:
#         return f'{percent}% [{progress * times}{remaining * (10 - times)}]\n' \
#                f'Still loading...'
#     return f'100% Complete!\n' \
#            f'[{progress * times}]'
#
#
# input_percent = int(input())
# print(loading_bar(input_percent))


def make_loading_bar(number):
    loading_bar = f"[{'%' * (number // 10)}{'.' * ((100 - number) // 10)}]"

    if number == 100:
        return f'{number}% Complete!\n' \
               f'{loading_bar}'
    return f'{number}% {loading_bar}\n' \
           f'Still loading...'


print(make_loading_bar(int(input())))