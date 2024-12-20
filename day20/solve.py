from collections import defaultdict

with open("day20/input.txt") as f:
    grid = [line.strip() for line in f.readlines()]

R = len(grid)
C = len(grid[0])
dirs = [ (1, 0), (0, 1), (-1, 0), (0, -1)]

def cheat_dist(sr, sc, er, ec):
    return abs(sr - er) + abs(sc - ec)

track = set()

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

TRACK_LENGTH = len(track) - 1
REQUIRED_SAVED = 100

all_cheats_p1 = defaultdict(set)
all_cheats_p2 = defaultdict(set)

# find the ordered sequence of the track, as well as distance of each point from START and to END
dist_from_start = dict()
dist_to_end = dict()
track_ordered = [START]
dist_from_start[START] = 0
dist_to_end[START] = TRACK_LENGTH
r, c = START
dist = 0

while (r, c) != END:
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if (nr, nc) in track and (nr, nc) not in track_ordered:
            dist_from_start[(nr, nc)] = dist + 1
            dist_to_end[(nr, nc)] = TRACK_LENGTH - dist - 1
            track_ordered.append((nr, nc))
            r, c = nr, nc
            dist += 1

# find cheats between any pair of points on track
for pos, cheat_start in enumerate(track_ordered):
    for cheat_end in track_ordered[pos + 1 + REQUIRED_SAVED:]:

        cd = cheat_dist(*cheat_start, *cheat_end)

        # for any cheat of valid length, check the total distance START to END. if it's less than track length (cheat was useful), add the saved distance and the cheat to results
        if cd <= 20:
           
            total_dist = dist_from_start[cheat_start] + cd + dist_to_end[cheat_end]
            saved = TRACK_LENGTH - total_dist
            if saved >= REQUIRED_SAVED:
                # Part 2 - add all cheats up to length 20
                all_cheats_p2[saved].add((*cheat_start, *cheat_end))
                if cd == 2:
                    # Part 1 - add only cheats of length 2
                    all_cheats_p1[saved].add((*cheat_start, *cheat_end))


total_p1 = sum([len(cheats) for cheats in all_cheats_p1.values()])
total_p2 = sum([len(cheats) for cheats in all_cheats_p2.values()])

print(f"2024 Day 20, Part 1 = {total_p1}")  
print(f"2024 Day 20, Part 2 = {total_p2}")  