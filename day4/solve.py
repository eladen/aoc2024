with open("day4/input.txt") as f:
    grid = [line.strip() for line in f.readlines()]

R = len(grid)
C = len(grid[0])
deltas = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
deltas_p2 = [ (1, 1), (1, -1), (-1, -1), (-1, 1)]

def check_direction(r, c, dr, dc):

    if r + dr * 3 >= R or r + dr * 3 < 0 or c + dc * 3 >= C or c + dc * 3 < 0:
        return 0
    
    m = grid[r + dr][c + dc] 
    a = grid[r + dr * 2][c + dc * 2]
    s = grid[r + dr * 3][c + dc * 3]

    return m == "M" and a == "A" and s == "S"

def check_direction_p2(r, c):
    
    if r < 1 or r >= R - 1 or c < 1 or c >= C - 1:
        return 0
    
    count = 0
    for dr, dc in deltas_p2:
        
        m =  grid[r + dr][c + dc]
        s =  grid[r - dr][c - dc]

        if m == "M" and s == "S": 
            count += 1

    return count == 2

total_p1 = 0
total_p2 = 0
for r in range(R):
    for c in range(C):
        if grid[r][c] == "A":
            total_p2 += check_direction_p2(r, c)
        for dr, dc in deltas:
            if grid[r][c] == "X":
                total_p1 += check_direction(r, c, dr, dc) 

print(f"2024 Day 4, Part 1 = {total_p1}") 
print(f"2024 Day 4, Part 2 = {total_p2}")  