import re

with open("day3/input.txt") as f:
    s = f.read().strip()

def parse_nums(s):
    num1 = int(s.split(",")[0].split("(")[1])
    num2 = int(s.split(",")[1].split(")")[0])
    return(num1 * num2)

# Part 1
regex = r'mul\(\d+,\d+\)'
expressions_p1 = re.findall(regex, s)
multiplications_p1 = [parse_nums(x) for x in expressions_p1]
total_p1 = sum(multiplications_p1)

# Part 2
while True:
    start = s.find("don't")
    end = s[start:].find("do()")
    if start == -1 or end == -1:
        break
    s = s[:start] + s[start+end+4:]

expressions_p2 = re.findall(regex, s)
multiplications_p2 = [parse_nums(x) for x in expressions_p2]
total_p2 = sum(multiplications_p2)

print(f"2024 Day 3, Part 1 = {total_p1}") 
print(f"2024 Day 3, Part 2 = {total_p2}")  