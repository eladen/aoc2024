from collections import defaultdict
with open("day8/input.txt") as f:
    grid = [list(line.strip()) for line in f.readlines()]

R = len(grid)
C = len(grid[0])

antennas = defaultdict(list)
antinodes = set()
antinodes_p2 = set()

for r, row in enumerate(grid):
    for c, col in enumerate(row):
        if grid[r][c].isalnum():
            antennas[grid[r][c]].append((r, c))

for antenna in antennas:
    for pos1 in antennas[antenna]:
        for pos2 in antennas[antenna]:

            if pos1 == pos2:
                continue

            dr = pos2[0] - pos1[0]
            dc = pos2[1] - pos1[1]
            r = pos2[0]
            c = pos2[1]
            
            # Part 1
            if r + dr >= 0 and r + dr < R and c + dc >= 0 and c + dc < C:
                antinodes.add((r + dr, c + dc))
            
            # Part 2
            while r >= 0 and r < R and c >= 0 and c < C:
                antinodes_p2.add((r, c))
                r = r + dr
                c = c + dc

total_p1 = len(antinodes)
total_p2 = len(antinodes_p2)


print(f"2024 Day 8, Part 1 = {total_p1}") 
print(f"2024 Day 8, Part 2 = {total_p2}")  