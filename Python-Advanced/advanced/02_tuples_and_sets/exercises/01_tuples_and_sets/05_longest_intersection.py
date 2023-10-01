n = int(input())
intersection = []

for _ in range(n):
    current_intersection = None
    set1 = set()
    set2 = set()
    f_range, s_range = input().split('-')
    f_start, f_end = [int(x) for x in f_range.split(',')]
    s_start, s_end = [int(x) for x in s_range.split(',')]

    set1 = set(range(f_start, f_end + 1))
    set2 = set(range(s_start, s_end + 1))
    current_intersection = set1.intersection(set2)

    if len(current_intersection) > len(intersection):
        intersection = current_intersection

print(f"Longest intersection is {list(intersection)} with length {len(intersection)}")