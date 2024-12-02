left = []
right = []
with open("day2/input.txt") as f:
    grid = [list(map(int, line.split())) for line in f.readlines()]

total_p1 = 0
total_p2 = 0
for report in grid:

    # part 1
    deltas = [y - x for x, y in zip(report, report[1:])]
    deltas_rev = [-x for x in deltas]
    if (all(x >=1 for x in deltas) and all(x <=3 for x in deltas)) or (all(x >=1 for x in deltas_rev) and all(x <=3 for x in deltas_rev)):
        total_p1 += 1
    
    # part 2 
    is_safe = False
    for i in range(len(report)):
        alt_report = list(report)
        alt_report.pop(i)
        deltas = [y - x for x, y in zip(alt_report, alt_report[1:])]
        deltas_rev = [-x for x in deltas]
        if (all(x >=1 for x in deltas) and all(x <=3 for x in deltas)) or (all(x >=1 for x in deltas_rev) and all(x <=3 for x in deltas_rev)):
            is_safe = True
    if is_safe:
        total_p2 += 1

print(f"Day 2, Part 1 = {total_p1}") 
print(f"Day 2, Part 2 = {total_p2}")  