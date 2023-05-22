#
n = int(input())
p = int(input())

initial_courses = n // p

if n % p != 0:
    initial_courses += 1

print(initial_courses)


# Am I a joke to you? (I did unnecessary things)
# n = int(input())
# p = int(input())
#
# while True:
#     if n > p:
#         first_trips = n // p
#     else:
#         result = f'All the persons fit inside the elevator.\n' \
#                  f'Only one course is needed.'
#         break
#
#     if first_trips * p < n:
#         remaining_people = n - first_trips * p
#         result = f'{first_trips} courses * {p} people + 1 courses * {remaining_people} persons'
#     else:
#         result = f'{first_trips} courses * {p} people'
#     break
#
# print(result)
