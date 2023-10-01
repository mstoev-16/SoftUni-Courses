# Not working properly

# from collections import deque
#
# car_queue = deque()
# green_light_cycle = int(input())
# free_window = int(input())
# cars_passed = 0
# crash = False
#
# while True:
#     command = input()
#     if command == 'END':
#         break
#
#     elif command != 'green':
#         car_queue.appendleft(deque(command))
#     else:
#         current_car = car_queue[-1].copy()
#         for _ in range(green_light_cycle):
#             car_in_passing = True
#             if car_queue[-1]:
#                 car_queue[-1].popleft()
#             else:
#                 car_in_passing = False
#                 car_queue.pop()
#                 cars_passed += 1
#                 if car_queue:
#                     current_car = car_queue[-1].copy()
#                 else:
#                     break
#
#         for _ in range(free_window):
#             if car_in_passing:
#                 car_queue[-1].popleft()
#                 if not car_queue[-1]:
#                     car_queue.pop()
#                     cars_passed += 1
#             else:
#                 crash = True
#                 break
#
# if crash:
#     print("A crash happened!")
#     print(f"{current_car} was hit at {car_queue[-1][0]}")
# else:
#     print(f"{cars_passed} total cars passed the crossroads.")