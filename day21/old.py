from collections import defaultdict, deque
from itertools import product
from functools import cache
from pprint import pprint
import numpy as np

with open("day21/input.txt") as f:
    codes = [line.strip() for line in f.readlines()]

DIRS = {
    "<": (0, -1),
    ">": (0, 1), 
    "v": (1, 0), 
    "^": (-1, 0)
}

KEY_POSITIONS = {
    "7": (0, 0), "8": (0, 1), "9": (0, 2),
    "4": (1, 0), "5": (1, 1), "6": (1, 2),
    "1": (2, 0), "2": (2, 1), "3": (2, 2),
    "#": (3, 0), "0": (3, 1), "A": (3, 2),
}

REMOTE_POSITIONS = {
    "#": (0, 0), "^": (0, 1), "A": (0, 2),
    "<": (1, 0), "v": (1, 1), ">": (1, 2),
}

KEYPAD = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    ["#", "0", "A"]
]

REMOTE = [
    ["#", "^", "A"],
    ["<", "v", ">"]
]

REMOTE_MAP = {
    ("A", "A"): "A",
    ("A", "<"): "v<<A",
    ("A", ">"): "vA",
    ("A", "^"): "<A",
    ("A", "v"): "v<A",

    ("<", "A"): ">>^A",
    ("<", "<"): "A",
    ("<", ">"): ">>A",
    ("<", "^"): ">^A",
    ("<", "v"): ">A",

    (">", "A"): "^A",
    (">", "<"): "<<A",
    (">", ">"): "A",
    (">", "^"): "<^A",
    (">", "v"): "<A",

    ("^", "A"): ">A",
    ("^", "<"): "v<A",
    ("^", ">"): "v>A",
    ("^", "^"): "A",
    ("^", "v"): "vA",

    ("v", "A"): "^>A",
    ("v", "<"): "<A",
    ("v", ">"): ">A",
    ("v", "^"): "^A",
    ("v", "v"): "A"
}

def dist(sr, sc, er, ec):
    return abs(sr - er) + abs(sc - ec)

@cache
def find_path(start, end, keypad=False):

    if keypad:
        positions = KEY_POSITIONS
        R = 4
    else:
        positions = REMOTE_POSITIONS
        R = 2

    q = deque()
    seen = set()
    q.append((*positions[start], ""))
    seen.add((*positions[start], ""))
    paths = defaultdict(list)

    best_distance = defaultdict(lambda: float("inf"))
    best_distance[positions[start]] = 0
    prev = defaultdict(list)

    while q:
        r, c, path = q.popleft()

        if len(path) > best_distance[positions[end]]:
            break

        if (r, c) == positions[end]:
            if list(path) == sorted(list(path)) or list(path) == sorted(list(path), reverse=True):
                paths[len(path)].append(path + "A")
        
        for dir in DIRS:
            dr, dc = DIRS[dir]
            
            nr = r + dr
            nc = c + dc
            if nr < 0 or nr >= R or nc < 0 or nc >= 3:
                continue
            if (nr, nc) == positions["#"]:
                continue
            if (nr, nc, path + dir) in seen:
                continue
            if len(path) + 1 > best_distance[(nr, nc)]:
                continue
            prev[(nr, nc)].append((r, c))
            best_distance[(nr, nc)] = len(path) + 1
            seen.add((nr, nc, path + dir))
            q.append((nr, nc, path + dir))

    return paths[best_distance[positions[end]]]


# Part 1

keypad_start = "A"
total_p1 = 0
for code in codes:

    # remote 1 - control keypad
    presses1 = []
    for i in range(len(code)):
        presses1.append(find_path(keypad_start, code[i], keypad=True))
        keypad_start = code[i]

    presses1 = list(map("".join, product(*presses1)))

    print(presses1)
    #print(presses1)
    # print()
    # print(code)
    #presses1 = "A".join(["".join(sorted(list(group), reverse=True)) for group in presses1.split("A")])

    # remote 2 - control remote 1
    presses2 = []
    for p in presses1:
        p_new = []
        remote_start = "A"
        for i in range(len(p)):
            p_new.append(find_path(remote_start, p[i], keypad=False))
            remote_start = p[i]

        p_new = list(map("".join, product(*p_new)))
        presses2 += p_new

    # presses2 = ["<A>Av<<AA>^AA>AvAA^A<vAAA>^A",]
    # presses2 = ["<A>A<AAv<AA>>^AvAA^A<vAAA>^A",]

    # presses2 = ["v<<AA>^AA>A",]
    # #presses2 = ["<AAv<AA>>^A",]

    # presses2 = ["v<<AA>^AA>A", "<AAv<AA>>^A"]
    # presses2 = ["v<A^A>", "<AvA>^"]

    # presses2 = ["<AvA>^",]

    # Remote 3 - control remote 2
    presses3 = []
    for p in presses2:
        p3 = []
        remote_start = "A"
        for i in range(len(p)):
            p3.append(find_path(remote_start, p[i], keypad=False))
            remote_start = p[i]

        p3 = list(map("".join, product(*p3)))
        presses3 += p3
    
    lens = [len(presses) for presses in presses3]
    # print(presses3[0])
    # print()
    # print(lens)
    # print()
    # print(presses3[-1])
    total_p1 += int(code.replace("A", "")) * min(lens)
    print(int(code.replace("A", "")), min(lens))
    #print(len(presses3))
print(total_p1)

exit()
# # Part 2
# keypad_start = "A"
# total_p3 = 0
# vals = dict()
# for code in codes:

#     # remote 1 - control keypad
#     presses = []
#     for i in range(len(code)):
#         presses.append(find_path(keypad_start, code[i], keypad=True))
#         keypad_start = code[i]

#     presses = list(map("".join, product(*presses)))[:1]
#     # print(presses[0])
#     # print(len(presses[0]))

#     #params = []
#     # remotes 2:X - control remote i-1
#     for i in range(3):
#         print(presses)
#         presses_new = []
#         for p in presses:
#             p_new = []
#             remote_start = "A"
#             for i in range(len(p)):
#                 p_new.append(find_path(remote_start, p[i], keypad=False))
#                 remote_start = p[i]
#             print(p_new)
#             print("start")
#             p_new = list(map("".join, product(*p_new)))
#             print("done")
#             presses_new += p_new
#         print("done2")
#         presses = presses_new
#         l = [len(p) for p in presses]
#         print(min(l))
#         len(l)
#         presses = list(filter(lambda x: len(x) == min(l), presses))[:1]
#         print(presses)
#         #params.append(len(presses[0]))

#     #vals[code] = params
#     lens = [len(p) for p in presses]
#     total_p3 += int(code.replace("A", "")) * min(lens)


total_p2 = 0
vals = dict()
test = dict()
for keypad_start in "0123456789A":
    for code in "0123456789A":
# for keypad_start in "A":
#     for code in "5":

        # remote 1 - control keypad
        presses = []
        presses.append(find_path(keypad_start, code, keypad=True))
        #keypad_start = code[i]

        presses = list(map("".join, product(*presses)))
        vals[(keypad_start, code)] = presses[0]
        # print(presses[0])
        # print(len(presses[0]))

        # params = []
        # params.append(len(presses[0]))
        # # remotes 2:X - control remote i-1
        # for i in range(3):
        #     presses_new = []
        #     for p in presses:
        #         p_new = []
        #         remote_start = "A"
        #         for i in range(len(p)):
        #             p_new.append(find_path(remote_start, p[i], keypad=False))
        #             remote_start = p[i]

        #         p_new = list(map("".join, product(*p_new)))
        #         presses_new += p_new
        #     presses = presses_new
        #     l = [len(p) for p in presses]
        #     presses = list(filter(lambda x: len(x) == min(l), presses))
        #     params.append(len(presses[0]))

        # vals[(keypad_start, code)] = params
        # # lens = [len(p) for p in presses]
        # # total_p2 += int(code.replace("A", "")) * min(lens)


pprint(vals)
xxx = defaultdict(int)
for k, v in vals.items():
    xxx[tuple(v)] +=1

pprint(xxx)
exit()


coeffs = dict()
len25 = dict()
#left = np.array([[0, 0, 1], [1, 1, 1], [4, 2, 1], [9, 3, 1]])
left = np.array([[0, 0, 0, 1], [1, 1, 1, 1], [8, 4, 2, 1], [27, 9, 3, 1]])

rep = 2
for ch, params in vals.items():
    # print(ch)
    # print(params)
    right = np.array(params)
    a, b, c, d = np.linalg.solve(left, right)
    #print(a, b, c, d)
    coeffs[ch] = [round(a), round(b), round(c), round(d)]
    # len25[ch] = rep**2 * round(a) + rep * round(b) + round(c)
    len25[ch] = rep**3 * round(a) + rep**2 * round(b) + rep * round(c) + round(d)

total_p2 = 0
for code in codes:
    t = 0
    t += len25[("A", code[0])] + len25[(code[0], code[1])] + len25[(code[1], code[2])] + len25[(code[2], code[3])]
    #print(code, t)
    total_p2 += int(code.replace("A", "")) * t

# pprint(vals)
# pprint(coeffs)
# pprint(len25)

print(f"2024 Day 21, Part 1 = {total_p1}") 
print(f"2024 Day 21, Part 2 = {total_p2}")  
#print(f"2024 Day 21, Part 3 = {total_p3}")