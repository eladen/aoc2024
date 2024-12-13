import math
from functools import cache
import numpy as np

with open("day13/input.txt") as f:
    machines = f.read().split("\n\n")

class Machine:
    def __init__(self, dxa, dya, dxb, dyb, tx, ty) -> None:
        self.dxa = dxa
        self.dya = dya
        self.dxb = dxb
        self.dyb = dyb
        self.tx = tx
        self.ty = ty

machines_list = []
for machine in machines:
    a, b, t = machine.splitlines()
    dxa = int(a.split(": ")[1].split(", ")[0].split("+")[1])
    dya = int(a.split(": ")[1].split(", ")[1].split("+")[1])
    dxb = int(b.split(": ")[1].split(", ")[0].split("+")[1])
    dyb = int(b.split(": ")[1].split(", ")[1].split("+")[1])
    tx = int(t.split(": ")[1].split(", ")[0].split("=")[1])
    ty = int(t.split(": ")[1].split(", ")[1].split("=")[1])
    machines_list.append(Machine(dxa, dya, dxb, dyb, tx, ty))
    pass

@cache
def press_buttons(machine: Machine, tokens=0, x=0, y=0, a_remaining=100, b_remaining=100):

    # return remaining tokens if at target
    if x == machine.tx and y == machine.ty:
        return tokens

    # no remaining tokens and not on target
    if a_remaining < 0 or b_remaining < 0:
        return math.inf
    
    # X or Y coordinate above target
    if x > machine.tx or y > machine.ty:
        return math.inf
    
    # try both buttons if enough tokens
    return min(
        # press A
        press_buttons(machine, tokens + 3,  x + machine.dxa, y + machine.dya, a_remaining - 1, b_remaining),

        # press B
        press_buttons(machine, tokens + 1, x + machine.dxb, y + machine.dyb, a_remaining, b_remaining - 1)
    )

total_p1 = 0
total_p2 = 0
for machine in machines_list:

    # Part 1
    # res = press_buttons(machine)
    # if res < math.inf:
    #     r1 = True
    #     total_p1 += res

    # Part 1 alt
    left = np.array([[machine.dxa, machine.dxb],[machine.dya, machine.dyb]])
    right = np.array([machine.tx, machine.ty])
    a, b = np.linalg.solve(left, right)

    # check solution
    a = round(a)
    b = round(b)

    if a * machine.dxa + b * machine.dxb == machine.tx and a * machine.dya + b * machine.dyb == machine.ty and a <= 100 and b <= 100:
        total_p1 += 3 * a + b

    # Part 2
    left = np.array([[machine.dxa, machine.dxb],[machine.dya, machine.dyb]])
    right = np.array([machine.tx + 10000000000000, machine.ty + 10000000000000])
    a, b = np.linalg.solve(left, right)

    # check solution
    a = round(a)
    b = round(b)

    if a * machine.dxa + b * machine.dxb == machine.tx + 10000000000000 and a * machine.dya + b * machine.dyb == machine.ty + 10000000000000:
        total_p2 += 3 * a + b

print(f"2024 Day 13, Part 1 = {total_p1}") 
print(f"2024 Day 13, Part 2 = {total_p2}")  