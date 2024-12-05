from collections import Counter
with open("day5/input.txt") as f:
    rules, updates = f.read().split("\n\n")
    rules = [list(map(int, r.split("|"))) for r in rules.splitlines()]
    updates = [list(map(int, p.split(","))) for p in updates.splitlines()]

total_p1 = 0
total_p2 = 0

for update in updates:
    ll = Counter()
    rr = Counter()
    rls = [[l, r] for l, r in rules if l in update and r in update]

    ordered = True
    for left, right in rls:

        ll[left] += 1
        rr[right] += 1
        
        if update.index(left) > update.index(right):
            ordered = False

    if ordered:
        total_p1 += update[len(update)//2]
    else:
        for u in update:
            if ll[u] == rr[u]:
                total_p2 += u

print(f"2024 Day 5, Part 1 = {total_p1}") 
print(f"2024 Day 5, Part 2 = {total_p2}")