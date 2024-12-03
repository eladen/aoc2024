with open("day2/input.txt") as f:
    grid = [list(map(int, line.split())) for line in f.readlines()]

total_p1 = 0
total_p2 = 0

def is_report_safe(report):
    deltas = [y - x for x, y in zip(report, report[1:])]
    return (all(x >= 1 for x in deltas) and all(x <= 3 for x in deltas)) or (all(x >= -3 for x in deltas) and all(x <= -1 for x in deltas))

for report in grid:

    # part 1
    if is_report_safe(report):
        total_p1 += 1
    
    # part 2 
    if any(is_report_safe(report[:i] + report[i+1:]) for i in range(len(report))):
        total_p2 += 1

print(f"2024 Day 2, Part 1 = {total_p1}") 
print(f"2024 Day 2, Part 2 = {total_p2}")  