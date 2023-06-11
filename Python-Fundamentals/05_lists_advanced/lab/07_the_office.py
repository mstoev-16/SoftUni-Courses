# employees = input().split()
# happiness_factor = int(input())
#
# calc_employees = list(map(lambda x: int(x) * happiness_factor, employees))
# happy = list(filter(lambda x: x >= sum(calc_employees) / len(employees), calc_employees))
#
# if len(happy) >= len(employees) / 2:
#     print(f'Score {len(happy)}/{len(employees)}. Employees are happy')
# else:
#     print(f'Score {len(happy)}/{len(employees)}. Employees are not happy')

# Sigh
# employees = input().split()
# improvement_factor = int(input())
#
# # calculated_happiness = [int(num) * improvement_factor for num in employees]
# calculated_happiness = list(map(lambda x: int(x) * improvement_factor, employees))
#
# filtered = list(filter(lambda x: x >= sum(calculated_happiness)/len(calculated_happiness), calculated_happiness))
#
# if len(filtered) >= len(calculated_happiness) / 2:
#     print(f'Score: {len(filtered)}/{len(calculated_happiness)}. Employees are happy!')
# else:
#     print(f'Score: {len(filtered)}/{len(calculated_happiness)}. Employees are not happy!')
