from collections import defaultdict, deque
from pprint import pprint
with open("day12/input.txt") as f:
    grid = [line.strip() for line in f.readlines()]

R = len(grid)
C = len(grid[0])
dirs = [ (1, 0), (0, 1), (-1, 0), (0, -1)]

marked = set()
regions = []
all_fence_lengths = []
all_fence_sides = []

# Mark points into regions
for r, row in enumerate(grid):
    for c, col in enumerate(row):

        if (r, c) not in marked:

            q = deque()
            q.append((r, c))
            seen = set()
            seen.add((r, c))
            marked.add((r, c))

            while q:

                rr, cc = q.popleft()
                
                for dr, dc in dirs:
                    nr = rr + dr
                    nc = cc + dc
                    if 0 <= nr < R and 0 <= nc < C and ((nr, nc) not in seen) and grid[r][c] == grid[nr][nc]:
                        seen.add((nr, nc))
                        marked.add((nr, nc))
                        q.append((nr, nc))

            regions.append(seen)

for region in regions:
    region_fence_length = 0

    sides_up = defaultdict(list)
    sides_left = defaultdict(list)
    sides_down = defaultdict(list)
    sides_right = defaultdict(list)
    
    for r, c in region:
        for dr, dc in dirs:
            nr = r + dr
            nc = c + dc
            if (nr, nc) not in region:
                
                # Part 1 - total length of fence per region
                region_fence_length += 1

                # For Part 2 - list of fences for each direction, by position
                # fence from below
                if nr > r:
                    sides_down[nr].append(nc)

                # fence from above
                if nr < r:
                    sides_up[nr + 1].append(nc)
                
                # fence from right
                if nc > c:
                    sides_right[nc].append(nr)

                # fence from left
                if nc < c:
                    sides_left[nc + 1].append(nr)

    # Count gaps in each side to increase side count
    sides_count = 0

    # UP
    for fence_positions in sides_up.values():
        sides_count += sum([x != y - 1 for x, y in zip(sorted(fence_positions), sorted(fence_positions)[1:])]) + 1
    
    # DOWN
    for fence_positions in sides_down.values():
        sides_count += sum([x != y - 1 for x, y in zip(sorted(fence_positions), sorted(fence_positions)[1:])]) + 1

    # LEFT
    for fence_positions in sides_left.values():
        sides_count += sum([x != y - 1 for x, y in zip(sorted(fence_positions), sorted(fence_positions)[1:])]) + 1

    # RIGHT
    for fence_positions in sides_right.values():
        sides_count += sum([x != y - 1 for x, y in zip(sorted(fence_positions), sorted(fence_positions)[1:])]) + 1
    
    all_fence_lengths.append(region_fence_length)
    all_fence_sides.append(sides_count)


total_p1 = 0
total_p2 = 0

for region, fence_length, fence_sides in zip(regions, all_fence_lengths, all_fence_sides):
    total_p1 += len(region) * fence_length
    total_p2 += len(region) * fence_sides

print(f"2024 Day 12, Part 1 = {total_p1}") 
print(f"2024 Day 12, Part 2 = {total_p2}")  