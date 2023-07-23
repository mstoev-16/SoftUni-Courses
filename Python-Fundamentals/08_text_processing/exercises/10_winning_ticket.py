def check_ticket(ticket):
    if len(ticket) != 20:
        return 'invalid ticket'

    symbols = ['@', '#', '$', '^']
    left_side = ticket[0:10]
    right_side = ticket[10:]

    for symbol in symbols:
        for repetitions in range(10, 5, -1):
            uninterrupted_symbols = symbol * repetitions
            if uninterrupted_symbols in left_side and uninterrupted_symbols in right_side:
                if repetitions == 10:
                    return f'ticket "{ticket}" - {len(uninterrupted_symbols)}{symbol} Jackpot!'
                else:
                    return f'ticket "{ticket}" - {len(uninterrupted_symbols)}{symbol}'
    return f'ticket "{ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(', ')]
for ticket in tickets:
    print(check_ticket(ticket))