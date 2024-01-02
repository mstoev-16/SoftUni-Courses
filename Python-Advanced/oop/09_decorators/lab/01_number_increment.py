def number_increment(numbers):
    def increase():
        incremented_numbers = [num + 1 for num in numbers]
        return incremented_numbers

    return increase()
