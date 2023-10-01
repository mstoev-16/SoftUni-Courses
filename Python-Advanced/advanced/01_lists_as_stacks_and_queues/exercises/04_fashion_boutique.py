clothes_stack = [int(x) for x in input().split()]
rack_capacity = int(input())
clothes_sum = 0
racks_used = 1

while clothes_stack:
    current_clothe = clothes_stack.pop()

    if clothes_sum + current_clothe <= rack_capacity:
        clothes_sum += current_clothe
    else:
        clothes_sum = current_clothe
        racks_used += 1

print(racks_used)