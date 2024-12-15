with open("day15/input.txt") as f:
    map, moves = f.read().split("\n\n")
    moves = moves.replace("\n", "")
    grid = [list(row) for row in map.splitlines()]
    grid_p2 = [list(row.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")) for row in map.splitlines()]

dirs = {
    "<": (0, -1),
    ">": (0, 1),
    "v": (1, 0),
    "^": (-1, 0)
}

def print_grid():
    for r in grid:
        print("".join(r))

def move_robot(r, c, dr, dc):

    nr = r + dr
    nc = c + dc
    
    # path blocked
    if grid[nr][nc] == "#":
        return False
    
    # path free - move robot or box
    if grid[nr][nc] == ".":
        grid[nr][nc] = grid[r][c]
        grid[r][c] = "."
        return True

    # move next box if possible
    nxt = move_robot(nr, nc, dr, dc)

    # if we could move the next box, move this one as well
    if nxt:
        grid[nr][nc] = grid[r][c]
        grid[r][c] = "."
        return True

def can_move_vertically(r, c, dr, dc):
    nr = r + dr
    nc = c + dc
    
    # check if position is left or right side of the box
    if grid[r][c] == "[":
        ec = 1 
    elif grid[r][c] == "]":
        ec = -1
    else:
        ec = 0

    # base case - not moving, or next position is free
    if grid[r][c] == "." or (grid[nr][nc] == "." and grid[nr][nc + ec] == "."):
        return True

    # base case - next position is blocked
    if grid[nr][nc] == "#" or grid[nr][nc + ec] == "#":
        return False

    # otherwise check if next position can be moved recursively

    # if robot check only directly above/below
    if grid[r][c] == "@":
        return can_move_vertically(nr, nc, dr, dc)
    
    # otherwise check the other side of the box as well
    return can_move_vertically(nr, nc, dr, dc) and can_move_vertically(nr, nc + ec, dr, dc)


def move_robot_p2(r, c, dr, dc):
    # used to move robot or box vertically

    # base case - no need to move
    if grid[r][c] == ".":
        return True
    
    nr = r + dr
    nc = c + dc
    
    # if moving ROBOT itself, nothing really changes, we move only 1 square
    if grid[r][c] == "@":
        
        if grid[nr][nc] == ".":
            grid[nr][nc] = grid[r][c]
            grid[r][c] = "."
            #print(f"moving robot {(r, c, dr, dc)}")
            return 

        move_robot_p2(nr, nc, dr, dc)

        grid[nr][nc] = grid[r][c]
        grid[r][c] = "."
        return 
        
    # Otherise, we are moving a BOX - we need to move the extra side as well

    # extra column to move
    ec = 1 if grid[r][c] == "[" else -1

    # base case - path free, move the box
    if grid[nr][nc] == "." and grid[nr][nc + ec] == ".":
        grid[nr][nc] = grid[r][c]
        grid[nr][nc + ec] = grid[r][c + ec]
        grid[r][c ] = "."
        grid[r][c + ec] = "."
        return 

    # Otherwise, another box in the way - move it first
    move_robot_p2(nr, nc, dr, dc)
    move_robot_p2(nr, nc + ec, dr, dc)

    # after boxes in the path were moved, we can safely move this one
    grid[nr][nc] = grid[r][c]
    grid[nr][nc + ec] = grid[r][c + ec]
    grid[r][c] = "."
    grid[r][c + ec] = "."


# Part 1
R = len(grid)
C = len(grid[0])

for r in range(R):
    for c in range(C):
        if grid[r][c] == '@':
            robot = (r, c)

for move in moves:
    dr, dc = dirs[move]
    r, c = robot
    move_robot(r, c, dr, dc)
    if grid[r + dr][c + dc] == "@":
        robot = (r + dr, c + dc)

# print_grid()

total_p1 = 0
for r in range(R):
    for c in range(C):
        if grid[r][c] == "O":
            total_p1 += 100 * r + c


# Part 2
grid = grid_p2
R = len(grid)
C = len(grid[0])

for r in range(R):
    for c in range(C):
        if grid[r][c] == '@':
            robot = (r, c)

for move in moves:
    
    dr, dc = dirs[move]
    r, c = robot

    if move in "<>":
        move_robot(r, c, dr, dc)
    elif can_move_vertically(r, c, dr, dc):
        move_robot_p2(r, c, dr, dc)
    if grid[r + dr][c + dc] == "@":
        robot = (r + dr, c + dc)

# print_grid()

total_p2 = 0
for r in range(R):
    for c in range(C):
        if grid[r][c] == "[":
            total_p2 += 100 * r + c

print(f"2024 Day 15, Part 1 = {total_p1}") 
print(f"2024 Day 15, Part 2 = {total_p2}")  