from collections import defaultdict, deque

initials = dict()
gates = dict()
gates_rev = dict()
topograph = defaultdict(list)

with open("day24/input2.txt") as f:
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

        s1, s2 = sorted([source1, source2])
        gates[target] = (gtype, s1, s2)
        gates_rev[(s1, s2, gtype)] = target

all_nodes = set(initials.keys()) | set(gates.keys())

# print([(k, v) for k, v in gates.items() if k.startswith("z") and v[0] != "XOR"])
# [('z31', ('AND', 'x31', 'y31')), ('z45', ('OR', 'dps', 'mfg')), ('z38', ('OR', 'bvk', 'trm'))]

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


# print(get_decimal("x", wire_values))
# print(get_decimal("y", wire_values))
# print(get_decimal("z", wire_values))

expected = get_decimal("x", wire_values) + get_decimal("y", wire_values)
actual = get_decimal("z", wire_values)

print(actual)
print(expected)

exp = bin(expected)[2:][::-1]
act = bin(actual)[2:][::-1]



def full_adder(x, y, c_in):
    x, y = sorted([x, y])
    xor1 = gates_rev[(x, y, "XOR")]
    a, b = sorted([c_in, xor1])
    s = gates_rev[(a, b, "XOR")]

    a, b = sorted([c_in, xor1])
    and1 = gates_rev[a, b, "AND"]
    and2 = gates_rev[x, y, "AND"]
    a, b = sorted([and1, and2])
    c_out = gates_rev[(a, b, "OR")]

    return(s, c_out)

def half_adder(x, y):
    x, y = sorted([x, y])
    s = gates_rev[(x, y, "XOR")]
    c_out = gates_rev[(x, y, "AND")]
    return s, c_out

s, c_out = half_adder("x00", "y00")
# print(s, c_out)
#exit()
#print(full_adder("x00", "y00"))

# manually looking through the bits backwards
# if a problem is found (key missing or Z bits are not result of a XOR gate - based on the adder logic), I manually looked at the adder cell, find the problem and fix it in input2 directly

for i in range(1, len(act) - 1):
    #i = 11
    if i < 10:
        x = "x0" + str(i)
        y = "y0" + str(i)
        z = "z0" + str(i)
    else:
        x = "x" + str(i)
        y = "y" + str(i)
        z = "z" + str(i)

    # print()
    # print(i)
    # print(wire_values[x], wire_values[y], wire_values[z], c_out, wire_values[c_out])
    # print(f"expected = {exp[i]}")
    # print(f"actual = {act[i]}")
    s, c_out = full_adder(x, y, c_out)
    # print(f"using adder = {s}, {c_out}, {wire_values[s]}, {wire_values[c_out]}")
        
    # if exp[i] != act[i]:
    #      print(i)

# for node in topograph:
#     for next in topograph[node]:
#         print(f"{node} -> {next}")

#x = [a for k, (a,b,c) in gates.items() if k.startswith("z")]

# manually swapped pairs
total_p2 = sorted([
    "rpv", "z11",
    "rpb", "ctg",
    "dmh", "z31",
    "dvq", "z38"
])
total_p2 = ",".join(total_p2)

print(f"2024 Day 12, Part 1 = {total_p1}") 
print(f"2024 Day 12, Part 2 = {total_p2}")  