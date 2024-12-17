registers = dict()
with open("day17/input.txt") as f:
    regs, program = f.read().split("\n\n")
    registers["A"] = int(regs.splitlines()[0].split(": ")[1])
    registers["B"] = int(regs.splitlines()[1].split(": ")[1])
    registers["C"] = int(regs.splitlines()[2].split(": ")[1])
    program = list(map(int, program.split(": ")[1].split(",")))

regA = registers["A"]

def combo(x):
    assert x != 7
    if x <= 3:
        return x
    if x == 4:
        return registers["A"]
    if x == 5:
        return registers["B"]
    if x == 6:
        return registers["C"]

# functions return True if pointer needs to be moved after execution
def f0(x):
    registers["A"] = registers["A"] // (2**combo(x))
    return True

def f1(x):
    registers["B"] = registers["B"] ^ x
    return True

def f2(x):
    registers["B"] = combo(x) % 8
    return True

def f3(x):
    if registers["A"] == 0:
        return True
    return False

def f4(x):
    registers["B"] = registers["B"] ^ registers["C"]
    return True

def f5(x):
    output.append(combo(x) % 8)
    return True

def f6(x):
    registers["B"] = int(registers["A"] / 2**combo(x))
    return True

def f7(x):
    registers["C"] = registers["A"] // 2**combo(x)
    return True

instructions = {
    0: f0,
    1: f1,
    2: f2,
    3: f3,
    4: f4,
    5: f5,
    6: f6,
    7: f7
}

def run_program(a):
    global output
    output = []
    pointer = 0
    registers["A"] = a
    while pointer < len(program) - 1:
        opcode = program[pointer]
        operand = program[pointer + 1]
        inst = instructions[opcode](operand)
        if inst:
            pointer += 2
        else: 
            pointer = operand
        
    return output

# Part 1
total_p1 = ",".join(map(str, run_program(regA)))

# Part 2

# build A backwards - from 1-7, one of which needs to be the value of A when program last outputs
check_next = set([1, 2, 3, 4, 5, 6, 7])
final = set()
for out in program[::-1]:
    check_now = check_next
    check_next = set()
    for a in check_now:
        o = run_program(a)
        if out == o[0]:
            # output is matching the one we look for; update the range for next iteration, or add the value to the final set of valid values of program is complete
            if o == program:
                final.add(a)
            else:
                # for next iteration, check all values that give the current value of A after floor dividing by 8
                check_next.update(range(a * 8, a * 8 + 8))

total_p2 = min(final)

print(f"2024 Day 17, Part 1 = {total_p1}") 
print(f"2024 Day 17, Part 2 = {total_p2}")