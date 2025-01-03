from collections import defaultdict
from copy import deepcopy

# X_MAX = 11
# Y_MAX = 7
X_MAX = 101
Y_MAX = 103
robots = []

class Robot:
    def __init__(self, px, py, vx, vy) -> None:
        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy
        self.q = self.set_quadrant()

    def move(self, secs=1):
        self.px = (self.px + secs * self.vx) % X_MAX
        self.py = (self.py + secs * self.vy) % Y_MAX
        self.q = self.set_quadrant()

    def set_quadrant(self):
        if self.px < X_MAX // 2:
            if self.py < Y_MAX // 2:
                return "UL"
            elif self.py > Y_MAX // 2:
                return "DL"
        elif self.px > X_MAX // 2:
            if self.py < Y_MAX // 2:
                return "UR"
            elif self.py > Y_MAX // 2:
                return "DR"
        return "MID"

with open("day14/input.txt") as f:
    for line in f.read().splitlines():
        position = line.split(" ")[0].split("=")[1]
        velocity = line.split(" ")[1].split("=")[1]
        px, py = map(int, position.split(","))
        vx, vy = map(int, velocity.split(","))
        robots.append(Robot(px, py, vx, vy))

# Part 1
quadrants = defaultdict(int)
for robot in robots:
    robot.move(100)
    quadrants[robot.q] += 1

bckp = deepcopy(robots)

# Part 2

# look for high concentration of robots in a space (a line in this case)
# if number of robots on any given line reached a new maximum, remember this max and the position in the loop; additionaly, print the robot map to check
# There are cycles in iterations - x positions repeats every 101 steps and y position every 103; no need to go aboe 101 * 103 steps
# Start the loop at 100 because robots already moved 100 times in part 1

max_count = 0
last_i = 0
for i in range(100, X_MAX * Y_MAX):

    all_positions = set()
    count_per_line = defaultdict(set)

    for robot in robots:
        robot.move()
        all_positions.add((robot.px, robot.py))
        count_per_line[robot.py].add(robot.px)

        if len(count_per_line[robot.py]) > max_count:
            max_count = len(count_per_line[robot.py])
            last_i = i

    # print robots if new max count has been reached for visual check
    # if max_count > 20 and last_i == i:   

    #     print("\n\n\n")
    #     print(i, max_count)
    #     print()

    #     for y in range(Y_MAX):
    #         for x in range(X_MAX):
    #             if (x, y) in all_positions:
    #                 print("#", end="")
    #             else:
    #                 print(".", end="")
    #         print()
    


total_p1 = quadrants["UL"] * quadrants["UR"] * quadrants["DL"] * quadrants["DR"]
total_p2 = last_i + 1

print(f"2024 Day 14, Part 1 = {total_p1}") 
print(f"2024 Day 14, Part 2 = {total_p2}")  

# # Part 2 - alternative

# # look for iteration with minimum total (manhattan) distance between positions of robots
# robots = bckp
# min_total_dist = math.inf
# last_i = 0
# vars = []

# for i in range(100, X_MAX * Y_MAX):

#     all_positions = []
#     count_per_line = defaultdict(set)

#     for robot in robots:
#         robot.move()
#         all_positions.append((robot.px, robot.py))
        
#     distances = []
#     for j, pos in enumerate(all_positions):
#         for pos2 in all_positions[:j]:
#             distances.append(abs(pos[0] - pos2[0]) + abs(pos[1] - pos2[1]))
    
#     total_dist = sum(distances)
#     if total_dist < min_total_dist:
#         min_total_dist = total_dist
#         last_i = i

# total_p2_alt = last_i + 1
# print(f"2024 Day 14, Part 2 alternative = {total_p2_alt}")  