from functools import cache
from collections import deque, defaultdict
from itertools import product

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

KEYPAD_MAP = {
    ('0', '0'): 'A',
    ('0', '1'): '^<A',
    ('0', '2'): '^A',
    ('0', '3'): '>^A',
    ('0', '4'): '^^<A',
    ('0', '5'): '^^A',
    ('0', '6'): '>^^A',
    ('0', '7'): '^^^<A',
    ('0', '8'): '^^^A',
    ('0', '9'): '>^^^A',
    ('0', 'A'): '>A',

    ('1', '0'): '>vA',
    ('1', '1'): 'A',
    ('1', '2'): '>A',
    ('1', '3'): '>>A',
    ('1', '4'): '^A',
    ('1', '5'): '>^A',
    ('1', '6'): '>>^A',
    ('1', '7'): '^^A',
    ('1', '8'): '>^^A',
    ('1', '9'): '>>^^A',
    ('1', 'A'): '>>vA',

    ('2', '0'): 'vA',
    ('2', '1'): '<A',
    ('2', '2'): 'A',
    ('2', '3'): '>A',
    ('2', '4'): '<^A',
    ('2', '5'): '^A',
    ('2', '6'): '>^A',
    ('2', '7'): '<^^A',
    ('2', '8'): '^^A',
    ('2', '9'): '>^^A',
    ('2', 'A'): 'v>A',

    ('3', '0'): '<vA',
    ('3', '1'): '<<A',
    ('3', '2'): '<A',
    ('3', '3'): 'A',
    ('3', '4'): '<<^A',
    ('3', '5'): '<^A',
    ('3', '6'): '^A',
    ('3', '7'): '<<^^A',
    ('3', '8'): '<^^A',
    ('3', '9'): '^^A',
    ('3', 'A'): 'vA',

    ('4', '0'): '>vvA',
    ('4', '1'): 'vA',
    ('4', '2'): 'v>A',
    ('4', '3'): 'v>>A',
    ('4', '4'): 'A',
    ('4', '5'): '>A',
    ('4', '6'): '>>A',
    ('4', '7'): '^A',
    ('4', '8'): '>^A',
    ('4', '9'): '>>^A',
    ('4', 'A'): '>>vvA',

    ('5', '0'): 'vvA',
    ('5', '1'): '<vA',
    ('5', '2'): 'vA',
    ('5', '3'): 'v>A',
    ('5', '4'): '<A',
    ('5', '5'): 'A',
    ('5', '6'): '>A',
    ('5', '7'): '<^A',
    ('5', '8'): '^A',
    ('5', '9'): '>^A',
    ('5', 'A'): 'vv>A',

    ('6', '0'): '<vvA',
    ('6', '1'): '<<vA',
    ('6', '2'): '<vA',
    ('6', '3'): 'vA',
    ('6', '4'): '<<A',
    ('6', '5'): '<A',
    ('6', '6'): 'A',
    ('6', '7'): '<<^A',
    ('6', '8'): '<^A',
    ('6', '9'): '^A',
    ('6', 'A'): 'vvA',

    ('7', '0'): '>vvvA',
    ('7', '1'): 'vvA',
    ('7', '2'): 'vv>A',
    ('7', '3'): 'vv>>A',
    ('7', '4'): 'vA',
    ('7', '5'): 'v>A',
    ('7', '6'): 'v>>A',
    ('7', '7'): 'A',
    ('7', '8'): '>A',
    ('7', '9'): '>>A',
    ('7', 'A'): '>>vvvA',

    ('8', '0'): 'vvvA',
    ('8', '1'): '<vvA',
    ('8', '2'): 'vvA',
    ('8', '3'): 'vv>A',
    ('8', '4'): '<vA',
    ('8', '5'): 'vA',
    ('8', '6'): 'v>A',
    ('8', '7'): '<A',
    ('8', '8'): 'A',
    ('8', '9'): '>A',
    ('8', 'A'): 'vvv>A',

    ('9', '0'): '<vvvA',
    ('9', '1'): '<<vvA',
    ('9', '2'): '<vvA',
    ('9', '3'): 'vvA',
    ('9', '4'): '<<vA',
    ('9', '5'): '<vA',
    ('9', '6'): 'vA',
    ('9', '7'): '<<A',
    ('9', '8'): '<A',
    ('9', '9'): 'A',
    ('9', 'A'): 'vvvA',

    ('A', '0'): '<A',
    ('A', '1'): '^<<A',
    ('A', '2'): '<^A',
    ('A', '3'): '^A',
    ('A', '4'): '^^<<A',
    ('A', '5'): '<^^A',
    ('A', '6'): '^^A',
    ('A', '7'): '^^^<<A',
    ('A', '8'): '<^^^A',
    ('A', '9'): '^^^A',
    ('A', 'A'): 'A'
 }

REMOTE_MAP = {
    ("A", "A"): "A",
    ("A", "<"): "v<<A",
    ("A", ">"): "vA",
    ("A", "^"): "<A",
    ("A", "v"): "<vA",

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


@cache
def compute(out, remaining):
      
    if remaining == 0:
        return sum(map(len, out))

    total = 0

    for s in out:
        out = []
        for i, j in zip("A" + s, s):
            out.append(REMOTE_MAP[(i, j)])
        out = tuple(out)
        total += compute(out, remaining - 1)

    return total

codes = ["382A", "463A", "935A", "279A", "480A"]
#ri = ["029A", "980A", "179A", "456A", "379A"]

total_p1 = 0
total_p2 = 0
for code in codes:
    
    presses = []
    for i, j in zip("A" + code, code):
        presses.append(find_path(i, j, keypad=True))

    res_p1 = []
    res_p2 = []
    for out in list(product(*presses)):
        res_p1.append(compute(out, 2))
        res_p2.append(compute(out, 25))

    total_p1 += int(code.replace("A", "")) * min(res_p1)
    total_p2 += int(code.replace("A", "")) * min(res_p2)

print(f"2024 Day 21, Part 1 = {total_p1}") 
print(f"2024 Day 21, Part 2 = {total_p2}") 

