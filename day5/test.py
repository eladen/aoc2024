from collections import Counter
update = [75,97,47,61,53]
rls = [[47, 53], [97, 61], [97, 47], [75, 53], [61, 53], [97, 53], [75, 47], [97, 75], [47, 61], [75, 61]]
ll = Counter()
rr = Counter()
for l, r in rls:
    print(r, l)
    ll[l] += 1
    rr[r] += 1

print(ll)
print(rr)
print(ll - rr)

for u in update:
    if ll[u] == rr[u]:
        print(u)