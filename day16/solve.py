from collections import defaultdict, deque
from heapq import heappop, heappush
import math

with open("day16/input.txt") as f:
    grid = [list(line.strip()) for line in f.readlines()]

R = len(grid)
C = len(grid[0])

for r in range(R):
    for c in range(C):
        if grid[r][c] == "S":
            START = (r, c) 
        if grid[r][c] == "E":
            END = (r, c)


def dijkstra(grid, start, end, dr, dc):

    # looking for paths on a graph with nodes r, c, dr, dc - to allow for different directions in each node
    # looking for multiple shortest paths, meaning we are not saving only the first "best" path using the prev dictionary, but instead add and save all paths of equal (minimum) cost
    # also, we are looking for multiple END nodes (4 directions) and each of those can be visited multiple times (on a different shortest path), so we are not stopping dijkstra early

    best_distance = defaultdict(lambda: math.inf)
    prev = defaultdict(list)
    r, c = start
    pq = []
    seen = set()

    heappush(pq, (0, r, c, dr, dc) )
    best_distance[(r, c, dr, dc)] = 0
    seen.add((r, c, dr, dc))

    while pq:

        dist, r, c, dr, dc = heappop(pq)
        seen.add((r, c, dr, dc))

        # check forward, add path if distance is at most the current minumum:
        if (r + dr, c + dc, dr, dc) not in seen and grid[r + dr][c + dc] != '#' and dist + 1 <= best_distance[(r + dr, c + dc, dr, dc)]:
            # note to self - everything works fine without resetting prev[] when new min dist is reached but I don't get why
            if dist + 1 < best_distance[(r + dr, c + dc, dr, dc)]:
                prev[(r + dr, c + dc, dr, dc)] = []
            prev[(r + dr, c + dc, dr, dc)].append((r, c, dr, dc))
            best_distance[(r + dr, c + dc, dr, dc)] = dist + 1
            heappush(pq, (dist + 1, r + dr, c + dc, dr, dc) )

        # check left, add path if distance is at most the current minumum:
        if  (r, c, -dc, dr) not in seen and dist + 1000 <= best_distance[(r, c, -dc, dr)]:
            if dist + 1000 < best_distance[(r, c, -dc, dr)]:
                prev[(r, c, -dc, dr)] = []
            prev[(r, c, -dc, dr)].append((r, c, dr, dc))
            best_distance[(r, c, -dc, dr)] = dist + 1000
            heappush(pq, (dist + 1000, r, c, -dc, dr) )

        # check right, add path if distance is at most the current minumum:
        if (r, c, dc, -dr) not in seen and dist + 1000 <= best_distance[(r, c, dc, -dr)]:
            if dist + 1000 < best_distance[(r, c, dc, -dr)]:
                prev[(r, c, dc, -dr)] = []
            prev[(r, c, dc, -dr)].append((r, c, dr, dc))
            best_distance[(r, c, dc, -dr)] = dist + 1000
            heappush(pq, (dist + 1000, r, c, dc, -dr) )

    return best_distance, prev


# Part 1
best_distances, prev = dijkstra(grid, START, END, 0, 1)
distances_to_end = [(dist, r, c, dr, dc) for (r, c, dr, dc), dist in best_distances.items() if r == END[0] and c == END[1]]
min_dist, r, c, dr, dc = sorted(distances_to_end)[0]

# Part 2
# go from end, visit any points along any of the shortest paths
q = deque()
seen = set()

for (dist, r, c, dr, dc) in distances_to_end:
    if dist == min_dist:
        q.append((r, c, dr, dc))
        seen.add((r, c, dr, dc))

while q:
    r, c, dr, dc = q.popleft()

    # add all previous nodes along any shortest path to the queue and set of visited nodes
    for pr, pc, pdr, pdc in prev[(r, c, dr, dc)]:
        if (pr, pc, pdr, pdc) not in seen:
            seen.add((pr, pc, pdr, pdc))
            q.append((pr, pc, pdr, pdc))

# remove direction from the visited set
seen = {(r, c) for r, c, dr, dc in seen}

# print best seats for fun
# for r in range(R):
#     for c in range(C):
#         print("O", end="") if (r, c) in seen else print(grid[r][c], end="")
#     print()

total_p1 = min_dist
total_p2 = len(seen)

print(f"2024 Day 16, Part 1 = {min_dist}") 
print(f"2024 Day 16, Part 2 = {total_p2}")  