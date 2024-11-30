from aocd import get_data, submit
from tqdm import tqdm

real = get_data(day = 1, year = 2024)

example = '''\
>
'''

data = example

def solve_p1(data):
    for line in tqdm(data.splitlines()):
        pass

    return 0

p1 = solve_p1(data)
print(p1)      

""" if data == real:
    submit(p1, part = "a", day = 1, year = 2024) """