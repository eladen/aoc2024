from collections import defaultdict, deque
from pprint import pprint
with open("day20/input.txt") as f:
    grid = [line.strip() for line in f.readlines()]

R = len(grid)
C = len(grid[0])
dirs = [ (1, 0), (0, 1), (-1, 0), (0, -1)]

track = set()
wall = set()

for r in range(R):
    for c in range(C):
        if grid[r][c] == "S":
            START = (r, c)
            track.add((r, c))
        elif grid[r][c] == "E":
            END = (r, c)
            track.add((r, c))
        elif grid[r][c] == ".":
            track.add((r, c))
        else:
            wall.add((r, c))

TRACK_LENGTH = len(track)
MAX_LENGTH = TRACK_LENGTH - 100



# queue in order: pos r, pos c, cheat_start r, cheat start c, cheat end r, cheat end c, cost
#def find_cheats():
cheats = []
seen = set()
q = deque()

q.append((*START, None, None, None, None, 0))
seen.add((*START, None, None, None, None))

while q:
    r, c, csr, csc, cer, cec, cost = q.popleft()
    #print(r, c, csr, csc, cer, cec, cost)
    
    
    if (r, c) == END:
        # if csr == 1:
        #     print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        #     print(r, c, csr, csc, cer, cec, cost)
        if cost < MAX_LENGTH:
            # if TRACK_LENGTH - cost - 1 > 60:
            #     print(r, c, csr, csc, cer, cec, cost)
            cheats.append((csr, csc, cer,cec, TRACK_LENGTH - cost - 1))
        
    for dr, dc in dirs:
        nr = r + dr
        nc = c + dc

        # cheat already ended
        if cer is not None:
            if (nr, nc) in track and (nr, nc, csr, csc, cer, cec) not in seen and (nr, nc) not in wall and cost < TRACK_LENGTH:
                #print(1)
                seen.add((nr, nc, csr, csc, cer, cec))
                q.append((nr, nc, csr, csc, cer, cec, cost + 1))

        # cheat started and now must continue
        elif csr is not None:
            if (nr, nc) in track and (nr, nc, csr, csc, nr, nc) not in seen and cost < TRACK_LENGTH:
                #print(2)
                seen.add((nr, nc, csr, csc, nr, nc))
                q.append((nr, nc, csr, csc, nr, nc, cost + 1))

        # cheat not started yet - it can either start now or not
        else:
            # non cheating option
            if (nr, nc) in track and (nr, nc, None, None, None, cec) not in seen and (nr, nc) not in wall and cost < TRACK_LENGTH:
                #print(3)
                seen.add((nr, nc, None, None, None, None))
                q.append((nr, nc, None, None, None, None, cost + 1))
            
            # cheating option
            if (nr, nc) in wall and (nr, nc, nr, nc, None, None) not in seen and cost < TRACK_LENGTH:
                #print(4)
                seen.add((nr, nc, nr, nc, None, None))
                q.append((nr, nc, nr, nc, None, None, cost + 1))

    #return cheats

#print(cheats)

total_p1 = len(list(filter(lambda x: x[-1] >= (TRACK_LENGTH - MAX_LENGTH), cheats)))
total_p2 = 0

print(f"2024 Day 20, Part 1 = {total_p1}") 
print(f"2024 Day 20, Part 2 = {total_p2}")  