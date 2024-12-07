eqs = {}
with open("day7/input.txt") as f:
    for line in f.readlines():
        total, nums = line.rstrip().split(": ")
        total = int(total)
        nums = tuple(map(int, nums.split()))
        eqs[total] = nums

def check_total(current, remaining, total, part2=False):

    # above expected total already
    if current > total:
        return False

    # current value is matching expected total with no remaining operations
    if current == total and remaining == ():
        return True
    
    # no remaining operations, current value not matching expected total
    if remaining == ():
        return False
    
    return (
        check_total(current + remaining[0], remaining[1:], total, part2) or
        check_total(current * remaining[0], remaining[1:], total, part2) or
        (part2 and check_total(current * (10**len(str(remaining[0]))) + remaining[0], remaining[1:], total, part2))
    )

total_p1 = 0
total_p2 = 0

for total, nums in eqs.items():

    # Part 1
    if check_total(nums[0], nums[1:], total):
        total_p1 += total

    # Part 2
    if check_total(nums[0], nums[1:], total, part2=True):
        total_p2 += total
    
print(f"2024 Day 7, Part 1 = {total_p1}") 
print(f"2024 Day 7, Part 2 = {total_p2}")  