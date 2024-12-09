from collections import defaultdict
from tqdm import tqdm

with open("day9/input.txt") as f:
    disk = list(map(int, f.read().strip()))

total_p1 = 0
total_p2 = 0

orig_filesystem = []
orig_filesystem_p2 = []

id = 0
for location, reps in enumerate(disk):
    if location % 2 == 0:
        orig_filesystem += [id] * reps
        id += 1
    else:
        orig_filesystem += ["."] * reps

orig_filesystem_p2 = list(orig_filesystem)
reordered_p2 = list(orig_filesystem)

# Part 1
reordered = []
max_vals = len(list(filter(lambda x: x != ".", orig_filesystem)))

for position in range(max_vals):
    if orig_filesystem[position] != ".":
        reordered.append(orig_filesystem[position])
    else:
        last = orig_filesystem.pop()
        while last == ".":
            last = orig_filesystem.pop()
        reordered.append(last)

total_p1 = sum([pos * id for pos, id in enumerate(reordered)])

# Part 2

# loop over all FileIDs, descending
for id in tqdm(range(id)[::-1]):
    count = orig_filesystem_p2.count(id)
    search_start = 0

    # loop over all empty spaces on the disk
    while "." in reordered_p2[search_start:]:

        # find first empty space in the iteration
        dot_pos = reordered_p2[search_start:].index(".") + search_start

        # find the length of the empty space
        space = 0
        while dot_pos + space < len(reordered_p2) and reordered_p2[dot_pos + space] == ".":
            space += 1

        # found empty space enough to fit the file
        if space >= count and dot_pos < reordered_p2.index(id):

            # replace FileID with '.'
            reordered_p2 = ["." if x == id else x for x in reordered_p2 ]
            
            # replace earlier '.'s with FileID
            for i in range(dot_pos, dot_pos + count):
                reordered_p2[i] = id

            # end the loop as file has been moved already
            break

        search_start = dot_pos + space + 1

total_p2 = sum([pos * id for pos, id in enumerate(reordered_p2) if id != "."])

print(f"2024 Day 9, Part 1 = {total_p1}") 
print(f"2024 Day 9, Part 2 = {total_p2}")  