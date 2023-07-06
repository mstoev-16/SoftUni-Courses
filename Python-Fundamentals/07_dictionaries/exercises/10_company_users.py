company_ids = {}

while True:
    command = input()

    if command == 'End':
        break

    [company, user_id] = command.split(' -> ')

    if company not in company_ids:
        company_ids[company] = [user_id]
    else:
        if user_id not in company_ids[company]:
            company_ids[company].append(user_id)

for company in company_ids.keys():
    print(company)
    for user_id in company_ids[company]:
        print('--', user_id)