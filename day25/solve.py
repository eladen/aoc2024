with open("day25/input.txt") as f:
    grids = f.read().split("\n\n")

locks = []
keys = []

for grid in grids:
    grid = grid.splitlines()

    grid = list(map(list, zip(*grid)))
    seq = [row.count("#") - 1 for row in grid]
    
    if grid[0][0] == "#":
        locks.append(seq)
    else:
        keys.append(seq)

LOCK_HEIGHT = 5

total_p1 = 0
for lock in locks:
    for key in keys:
        total_p1 += all(x + y <= LOCK_HEIGHT for x, y in zip(lock, key))

print(f"2024 Day 25, Part 1 = {total_p1}") 