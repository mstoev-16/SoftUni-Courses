# Shorter appraoch
numbers = [int(x) for x in input().split()]
positives = list(filter(lambda x: x > 0, numbers))
negatives = list(filter(lambda x: x < 0, numbers))
sum_positives = sum(positives)
sum_negatives = sum(negatives)

print(sum_negatives)
print(sum_positives)
if abs(sum_negatives) > abs(sum_positives):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")


# def check_positives_negatives(sequence):
#     sequence = [int(num) for num in sequence.split()]
#     sum_positives = 0
#     sum_negatives = 0
#
#     for num in sequence:
#         if num > 0:
#             sum_positives += num
#         else:
#             sum_negatives += num
#
#     if abs(sum_negatives) > sum_positives:
#         result = "The negatives are stronger than the positives"
#     else:
#         result = "The positives are stronger than the negatives"
#
#     return f"{sum_negatives}\n" \
#            f"{sum_positives}\n" \
#            f"{result}"
#
#
# print(check_positives_negatives(input()))
