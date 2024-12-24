from collections import defaultdict, deque

initials = dict()
gates = dict()
topograph = defaultdict(list)

with open("day24/input.txt") as f:
    inits, gts = f.read().split("\n\n")
    for line in inits.splitlines():
        k = line.split(": ")[0]
        v = int(line.split(": ")[1])
        initials[k] = v
    
    for line in gts.splitlines():
        left, target = line.split(" -> ")
        source1, gtype, source2 = left.split(" ")
        topograph[source1].append(target)
        topograph[source2].append(target)
        gates[target] = (gtype, source1, source2)

all_nodes = set(initials.keys()) | set(gates.keys())

for node in all_nodes - set(topograph.keys()):
    topograph[node] = []

FUNS = {
    "AND": lambda x, y: x & y,
    "OR": lambda x, y: x | y,
    "XOR": lambda x, y: x ^ y
}

def toposort(graph):
    ordering = []
    seen = set()
    nodes = graph.keys()

    def dfs(node):
        seen.add(node)
        for next in graph[node]:
            if next in seen: 
                continue
            dfs(next)
        ordering.append(node)

    for node in nodes:
        if node in seen: 
            continue
        dfs(node)

    return ordering[::-1]

sorted_wires = toposort(topograph)

wire_values = dict()
for wire in sorted_wires:
    if wire in initials:
        wire_values[wire] = initials[wire]
    else:
        f, s1, s2 = gates[wire]
        wire_values[wire] = FUNS[f](wire_values[s1], wire_values[s2])

def get_decimal(ch, wire_values):
    ch_wires = sorted([(wire, val) for wire, val in wire_values.items() if wire.startswith(ch)])[::-1]
    ch_binary = "".join([str(val) for wire, val in ch_wires])
    return int(ch_binary, 2)

total_p1 = get_decimal("z", wire_values)
total_p2 = 0

print(f"2024 Day 12, Part 1 = {total_p1}") 
print(f"2024 Day 12, Part 2 = {total_p2}")  

print(get_decimal("x", wire_values))
print(get_decimal("y", wire_values))
print(get_decimal("z", wire_values))

# for node in topograph:
#     for next in topograph[node]:
#         print(f"{node} -> {next}")

x = [a for k, (a,b,c) in gates.items() if k.startswith("z")]