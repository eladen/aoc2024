with open("day6/input.txt") as f:
    grid = [list(line.strip()) for line in f.readlines()]

R = len(grid)
C = len(grid[0])
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
seen = set()

for r, row in enumerate(grid):
    for c in range(r):
        if grid[r][c] == "^":
            direction = 0
            guard_orig = guard = (r, c)
            seen.add((r, c))

def next_move(r, c, dr, dc):
    if r + dr < 0 or r + dr >= R or c + dc < 0 or c + dc >= C:
        return "out"
    if grid[r + dr][c + dc] == "#" or grid[r + dr][c + dc] == "O":
        return "blocked"
    return "free"

# Part 1
while True:
    dr, dc = dirs[direction]
    r, c = guard
    nm = next_move(r, c, dr, dc)

    if nm == "out":
        break
    if nm == "free":
        r += dr
        c += dc
        guard = (r, c)
        seen.add(guard)
    if nm == "blocked":
        direction = (direction + 1) % 4

total_p1 = len(seen)

# Part 2
total_p2 = 0
for rr, cc in seen:

    if (rr, cc) == guard_orig: continue
    seen_p2 = set()
    direction = 0
    guard = guard_orig
    seen_p2.add((guard[0], guard[1], direction))
    grid[rr][cc] = "O"

    while True:
        dr, dc = dirs[direction]
        r, c = guard
        nm = next_move(r, c, dr, dc)

        if nm == "out":
            break
        if nm == "free":
            r += dr
            c += dc
            guard = (r, c)

            if (r, c, direction) in seen_p2:
                total_p2 += 1
                break
            seen_p2.add((r, c, direction))
        if nm == "blocked":
            direction = (direction + 1) % 4

    grid[rr][cc] = "."

print(f"2024 Day 6, Part 1 = {total_p1}") 
print(f"2024 Day 6, Part 2 = {total_p2}")  