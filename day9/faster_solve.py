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
def represent_disk(disk, ids):
    rep = []
    for i, x in enumerate(disk):
        if ids[i] == -1:
            rep += ["."] * x
        else:
            rep += [ids[i]] * x
    return(rep)

ids = [i // 2  if i % 2 == 0 else -1 for i, x in enumerate(disk)]
orig_disk = list(disk)
orig_ids = list(ids)

for i, file_space in enumerate(orig_disk[::-1]):
    orig_position = len(orig_disk) - 1 - i
    file_id = orig_ids[orig_position]
    if file_id == -1:
        continue
    
    prev_position = ids.index(file_id)
    for new_position, empty_space in enumerate(disk):
        if ids[new_position] == -1 and empty_space >= file_space and new_position < prev_position:
            ids[prev_position] = -1
            ids[new_position] = file_id

            remaining_space = empty_space - file_space
            if remaining_space > 0:
                disk = disk[:new_position + 1] + [remaining_space] + disk[new_position + 1:]
                disk[new_position] = file_space
                ids = ids[:new_position + 1] + [-1] + ids[new_position + 1:]
            break

new_disk = represent_disk(disk, ids)

total_p2 = sum([pos * id for pos, id in enumerate(new_disk) if id != "."])

print(f"2024 Day 9, Part 1 = {total_p1}") 
print(f"2024 Day 9, Part 2 = {total_p2}")  