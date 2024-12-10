from collections import defaultdict, deque
with open("day10/input.txt") as f:
    grid = [list(map(int, line.strip())) for line in f.readlines()]

R = len(grid)
C = len(grid[0])
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


# Part 1
all_trails = defaultdict(int)

for r, row in enumerate(grid):
    for c, col in enumerate(row):
        if grid[r][c] == 0:

            q = deque()
            q.append((r, c))

            while q:

                rr, cc = q.popleft()
                
                if grid[rr][cc] == 9:
                    all_trails[(r, c)] += 1
                
                for dr, dc in dirs:
                    if 0 <= rr + dr < R and 0 <= cc + dc <  C and grid[rr + dr][cc + dc] == grid[rr][cc] + 1 and ((rr + dr, cc + dc) not in q):
                        q.append((rr + dr, cc + dc))


total_p1 = sum(all_trails.values())

# Part 2
all_ratings = defaultdict(int)

for r, row in enumerate(grid):
    for c, col in enumerate(row):
        if grid[r][c] == 0:

            q = deque()
            q.append([(r, c)])

            while q:

                trail = q.popleft()
                rr, cc = trail[-1]
                
                if grid[rr][cc] == 9:
                    all_ratings[(r, c)] += 1
                
                for dr, dc in dirs:
                    new_trail = trail + [(rr + dr, cc + dc)]
                    if 0 <= rr + dr < R and 0 <= cc + dc <  C and grid[rr + dr][cc + dc] == grid[rr][cc] + 1 and new_trail not in q:
                        q.append(new_trail)


total_p1 = sum(all_trails.values())
total_p2 = sum(all_ratings.values())

print(f"2024 Day 10, Part 1 = {total_p1}") 
print(f"2024 Day 10, Part 2 = {total_p2}")  