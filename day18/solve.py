from collections import deque

with open("day18/input.txt") as f:
    bytes = [tuple(map(int, line.strip().split(","))) for line in f.readlines()]
bytes = [(y, x) for x, y in bytes]

# R = 7
# C = 7
# MAX_BLOCKS = 12

R = 71
C = 71
MAX_BLOCKS = 1024

dirs = [ (1, 0), (0, 1), (-1, 0), (0, -1)]
START = (0, 0)
END = (R-1, C-1)


for i in range(len(bytes)):
    
    blocked = set(bytes[:i])
    found_path = False
    seen = set()
    q = deque()

    # for r in range(R):
    #     for c in range(C):
    #         print("#", end="") if (r, c) in blocked else print(".", end="")
    #     print()

    q.append((*START, 0))
    seen.add(START)

    while q:
        r, c, cost = q.popleft()
        if (r, c) == END:
            if i == MAX_BLOCKS:
                total_p1 = cost
            found_path = True
            break

        for dr, dc in dirs:
            if 0 <= r + dr < R and 0 <= c + dc < C and (r + dr, c + dc) not in seen and (r + dr, c + dc) not in blocked:
                seen.add((r + dr, c + dc))
                q.append((r + dr, c + dc, cost + 1))

    if found_path == False:
        total_p2 = str(bytes[i-1][1]) + "," + str(bytes[i-1][0])
        break


print(f"2024 Day 18, Part 1 = {total_p1}") 
print(f"2024 Day 18, Part 2 = {total_p2}")  