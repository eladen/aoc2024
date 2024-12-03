with open("day4/input.txt") as f:
    grid = [list(map(int, line.split())) for line in f.readlines()]

total_p1 = 0
total_p2 = 0

print(f"2024 Day 4, Part 1 = {total_p1}") 
print(f"2024 Day 4, Part 2 = {total_p2}")  