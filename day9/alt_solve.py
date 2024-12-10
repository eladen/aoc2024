
from tqdm import tqdm
with open("day9/input.txt") as f:
    disk = list(map(int, f.read().strip()))

orig_filesystem = []
orig_filesystem_p2 = []
id = 0

for location, reps in enumerate(disk):
    if location % 2 == 0:
        orig_filesystem += [id] * reps
        id += 1
    else:
        orig_filesystem += [-1] * reps

orig_filesystem_p2 = list(orig_filesystem)
reordered_p2 = list(orig_filesystem)

# Part 1
reordered = []
max_vals = len(list(filter(lambda x: x != -1, orig_filesystem)))
for position in range(max_vals):
    if orig_filesystem[position] != -1:
        reordered.append(orig_filesystem[position])
    else:
        last = orig_filesystem.pop()
        while last == -1:
            last = orig_filesystem.pop()
        reordered.append(last)

total_p1 = sum([pos * id for pos, id in enumerate(reordered)])

# Part 2
# loop over all FileIDs, descending
max_id = id
#for id in tqdm(range(id)[::-1]):
for id in tqdm(range(max_id - 1, -1, -1)):
    count = orig_filesystem_p2.count(id)
    file_pos = reordered_p2.index(id)
    
    # loop over all empty spaces on the disk
    for dot_pos in range(file_pos):

        if reordered_p2[dot_pos] != -1:
            continue
        
        # find the length of the empty space
        space = 0
        while dot_pos + space < file_pos and reordered_p2[dot_pos + space] == -1:
            space += 1

        # found empty space enough to fit the file
        if space >= count and dot_pos < file_pos:

            # replace FileID with '.'
            #reordered_p2 = ["." if x == id else x for x in reordered_p2 ]
            for i in range(file_pos, file_pos + count):
                reordered_p2[i] = -1
            
            # replace earlier '.'s with FileID
            for i in range(dot_pos, dot_pos + count):
                reordered_p2[i] = id

            # end the loop as file has been moved already
            break

        # search_start = dot_pos + count + 1
total_p2 = sum([pos * id for pos, id in enumerate(reordered_p2) if id != -1])
print(f"2024 Day 9, Part 1 = {total_p1}") 
print(f"2024 Day 9, Part 2 = {total_p2}")  
