from collections import deque

with open("day18/input.txt") as f:
    bytes = [tuple(map(int, line.strip().split(","))) for line in f.readlines()]
bytes = [(y, x) for x, y in bytes]

# R = 7
# C = 7
# BYTES_P1 = 12

R = 71
C = 71
BYTES_P1 = 1024

dirs = [ (1, 0), (0, 1), (-1, 0), (0, -1)]
START = (0, 0)
END = (R - 1, C - 1)

def find_path(i):
    blocked = set(bytes[:i])
    min_cost = float("inf")
    seen = set()
    q = deque()

    q.append((*START, 0))
    seen.add(START)

    while q:
        r, c, cost = q.popleft()
        if (r, c) == END:
            min_cost = cost
            break

        for dr, dc in dirs:
            if 0 <= r + dr < R and 0 <= c + dc < C and (r + dr, c + dc) not in seen and (r + dr, c + dc) not in blocked:
                seen.add((r + dr, c + dc))
                q.append((r + dr, c + dc, cost + 1))
                
    return min_cost

# Part 1
total_p1 = find_path(BYTES_P1)

# Part 2
low, high = BYTES_P1, len(bytes)

# binary search to find the first blocking byte
while low <= high:
    mid = (low + high) // 2
    if find_path(mid) == float("inf"):
        high = mid - 1
    else:
        low = mid + 1

total_p2 = str(bytes[mid - 1][1]) + "," + str(bytes[mid - 1][0])


print(f"2024 Day 18, Part 1 = {total_p1}") 
print(f"2024 Day 18, Part 2 = {total_p2}")  