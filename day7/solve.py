eqs = {}
with open("day7/input.txt") as f:
    for line in f.readlines():
        total, nums = line.rstrip().split(": ")
        total = int(total)
        nums = list(map(int, nums.split()))
        eqs[total] = nums

def check_total(current, remaining, total, ops=None, part2=False):

    # initialize operations if none
    if ops == None:
        ops = []

    # above expected total already
    if current > total:
        return 0, ops

    # current value is matching expected total with no remaining operations
    if current == total and remaining == []:
        return 1, ops
    
    # no remaining operations, current value not matching expected total
    if remaining == []:
        return 0, ops
    
    # try all possible operations with the remaining numbers
    op1, ops1 = check_total(current + remaining[0], remaining[1:], total, ops + ["A"], part2)
    op2, ops2 = check_total(current * remaining[0], remaining[1:], total, ops + ["M"], part2)
    if part2:
        op3, ops3 = check_total(current * (10**len(str(remaining[0]))) + remaining[0], remaining[1:], total, ops + ["||"], part2)

    if op1 == 1:
        return op1, ops1
    elif op2 == 1:
        return op2, ops2
    elif part2 and op3 == 1:
        return op3, ops3
    return 0, ops


total_p1 = 0
total_p2 = 0

for total, nums in eqs.items():

    # Part 1
    res1, ops1 = check_total(nums[0], nums[1:], total, part2=False)
    if res1 == 1:
        total_p1 += total

    # Part 2
    res2, ops2 = check_total(nums[0], nums[1:], total, part2=True)
    if res2 == 1:
        total_p2 += total
    

print(f"2024 Day 7, Part 1 = {total_p1}") 
print(f"2024 Day 7, Part 2 = {total_p2}")  