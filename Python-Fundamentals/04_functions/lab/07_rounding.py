def rounding(numbers):
    rounded_nums = [round(float(num)) for num in numbers]

    return rounded_nums


print(rounding(input().split()))
