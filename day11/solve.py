from collections import defaultdict
from copy import copy

with open("day11/input.txt") as f:
    rocks = [int(ch) for ch in f.read().split(" ")]

# set up dict of rocks and their counts
rock_map = defaultdict(int)
for rock in rocks:
    rock_map[rock] += 1

def blink(rock_map, rep):
    for _ in range(rep):
        new_rock_map = copy(rock_map)
        for rock, count in rock_map.items():
            if rock == 0:
                new_rock_map[rock] -= count
                new_rock_map[1] += count
            elif len(str(rock)) % 2 == 0:
                r1 = int(str(rock)[:len(str(rock)) // 2])
                r2 = int(str(rock)[len(str(rock)) // 2:])
                new_rock_map[r1] += count
                new_rock_map[r2] += count
                new_rock_map[rock] -= count
            else:
                new_rock_map[rock] -= count
                new_rock_map[rock * 2024] += count
        rock_map = copy(new_rock_map)
    return rock_map
    
total_p1 = sum(blink(rock_map, 25).values())
total_p2 = sum(blink(rock_map, 75).values())

print(f"2024 Day 11, Part 1 = {total_p1}") 
print(f"2024 Day 11, Part 2 = {total_p2}")  