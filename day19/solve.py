with open("day19/input.txt") as f:
    patterns, designs = f.read().split("\n\n")
    patterns = patterns.split(", ")
    designs = designs.strip().split("\n")


memo_p1 = {}
def check_design(design):

    # memory check
    if design in memo_p1:
        return memo_p1[design]
    
    # base case - if design is complete, return true
    if len(design) == 0:
        memo_p1[design] = True
        return True
    
    design_possible = False
    for pattern in patterns:
        if design.startswith(pattern):
            design_possible = design_possible or check_design(design[len(pattern): ])

    memo_p1[design] = design_possible
    return design_possible

memo_p2 = {}
def check_design_p2(design):
    
    # memory check
    if design in memo_p2:
        return memo_p2[design]
    
    # base case - if design is complete, return 1
    if len(design) == 0:
        memo_p2[design] = 1
        return 1
    
    num_designs_possible = 0
    for pattern in patterns:
        if design.startswith(pattern):
            num_designs_possible += check_design_p2(design[len(pattern): ])

    memo_p2[design] = num_designs_possible
    return num_designs_possible


total_p1 = 0
total_p2 = 0
for design in designs:
    total_p1 += check_design(design)
    total_p2 += check_design_p2(design)

print(f"2024 Day 19, Part 1 = {total_p1}") 
print(f"2024 Day 19, Part 2 = {total_p2}")  