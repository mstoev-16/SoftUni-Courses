def is_prime(num):
    if num <= 1:
        return False
    for current_num in range(2, num):
        if num % current_num == 0:
            return False
    return True


def get_primes(numbers):
    for num in numbers:
        if is_prime(num):
            yield num


sequence = get_primes([1, 2, 3, 4, 2, 4, 15, 51, 2, 17])
for num in sequence:
    print(num)