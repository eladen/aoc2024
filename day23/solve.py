from collections import defaultdict

with open("day23/input.txt") as f:
    links = [line.strip().split("-") for line in f.readlines()]

graph = defaultdict(set)
for node1, node2 in links:
    graph[node1].add(node2)
    graph[node2].add(node1)
    graph[node1].add(node1)
    graph[node2].add(node2)

# Part 1
connections = set()
for node in graph:
    if not node.startswith("t"):
        continue
    for node2 in graph[node]:
        if node == node2:
            continue
        for node3 in graph[node2]:
            if node == node3 or node2 == node3:
                continue
            if node in graph[node3]:
                connections.add(frozenset((node, node2, node3)))
total_p1 = len(connections)


# Part 2
# where at least 3 PCs are connected (same as P1), add all neighbours they have in common to form a candidate for a lan party
party_candidates = set()
for node in graph:
    for node2 in graph[node]:
        for node3 in graph[node2]:
            if node in graph[node3]:
                party_candidates.add(frozenset(graph[node] & graph[node2] & graph[node3]))

max_party_size = 0

# loop through all candidates for a lan party and keep only PCs that are ALL interconnected, i.e. they form a real lan party
for party_candidate in party_candidates:
    lan_party = set(party_candidate)

    # remove all nodes (PCs) that are note connected to all other candidates
    for node in party_candidate:
        lan_party = lan_party & graph[node]
    
    # if the remaining lan party is the biggest so far, remember it
    if len(lan_party) > max_party_size:
        max_party_size = len(lan_party)
        biggest_lan_party = lan_party

total_p2 = ",".join(sorted(list(biggest_lan_party)))

print(f"2024 Day 23, Part 1 = {total_p1}") 
print(f"2024 Day 23, Part 2 = {total_p2}")  