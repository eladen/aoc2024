left = []
right = []
with open("day1/input.txt") as f:
    for line in f.readlines():
        left.append(int(line.split()[0]))
        right.append(int(line.split()[1]))

left.sort()
right.sort()
dist = [abs(r - l) for (l, r) in zip(left, right)]
similarity = [len(list(filter(lambda r: r == l, right))) * l for l in left]

p1 = sum(dist)
p2 = sum(similarity)

print(f"2024 Day 1, Part 1 = {p1}") 
print(f"2024 Day 1, Part 2 = {p2}")  