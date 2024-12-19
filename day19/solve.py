with open("day19/input.txt") as f:
    patterns, designs = f.read().split("\n\n")
    patterns = patterns.split(", ")
    designs = designs.strip().split("\n")

memo = {}
def check_design(design):
    
    # memory check
    if design in memo:
        return memo[design]
    
    # base case - if design is complete, return 1
    if design == "":
        return 1
    
    num_designs_possible = 0
    for pattern in patterns:
        if design.startswith(pattern):
            num_designs_possible += check_design(design[len(pattern): ])

    memo[design] = num_designs_possible
    return num_designs_possible

total_p1 = 0
total_p2 = 0
for design in designs:
    count = check_design(design)
    total_p1 += count > 0
    total_p2 += count

print(f"2024 Day 19, Part 1 = {total_p1}")
print(f"2024 Day 19, Part 2 = {total_p2}")