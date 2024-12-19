import time
from runpy import run_path

t0 = time.time()

print()
run_path("day1/solve.py")
t1 = time.time() 
print(f"Duration = {round(t1 - t0, 3)}s")

print()
run_path("day2/solve.py")
t2 = time.time() 
print(f"Duration = {round(t2 - t1, 3)}s")

print()
run_path("day3/solve.py")
t3 = time.time()
print(f"Duration = {round(t3 - t2, 3)}s")

print()
run_path("day4/solve.py")
t4 = time.time()
print(f"Duration = {round(t4 - t3, 3)}s")

print()
run_path("day5/solve.py")
t5 = time.time()
print(f"Duration = {round(t5 - t4, 3)}s")

print()
run_path("day6/solve.py")
t6 = time.time()
print(f"Duration = {round(t6 - t5, 3)}s")

print()
run_path("day7/solve.py")
t7 = time.time()
print(f"Duration = {round(t7 - t6, 3)}s")

print()
run_path("day8/solve.py")
t8 = time.time()
print(f"Duration = {round(t8 - t7, 3)}s")

print()
run_path("day9/faster_solve.py")
t9 = time.time()
print(f"Duration = {round(t9 - t8, 3)}s")

print()
run_path("day10/solve.py")
t10 = time.time()
print(f"Duration = {round(t10 - t9, 3)}s")

print()
run_path("day11/solve.py")
t11 = time.time()
print(f"Duration = {round(t11 - t10, 3)}s")

print()
run_path("day12/solve.py")
t12 = time.time()
print(f"Duration = {round(t12 - t11, 3)}s")

print()
run_path("day13/solve.py")
t13 = time.time()
print(f"Duration = {round(t13 - t12, 3)}s")

print()
run_path("day14/solve.py")
t14 = time.time()
print(f"Duration = {round(t14 - t13, 3)}s")

print()
run_path("day15/solve.py")
t15 = time.time()
print(f"Duration = {round(t15 - t14, 3)}s")

print()
run_path("day16/solve.py")
#gc.collect()
t16 = time.time()
print(f"Duration = {round(t16 - t15, 3)}s")

print()
run_path("day17/solve.py")
t17 = time.time()
print(f"Duration = {round(t17 - t16, 3)}s")

print()
run_path("day18/solve.py")
t18 = time.time()
print(f"Duration = {round(t18 - t17, 3)}s")

print()
run_path("day19/solve.py")
t19 = time.time()
print(f"Duration = {round(t19 - t18, 3)}s")

print()
print()
print(f"TOTAL TIME = {round(t19 - t0, 2)}s")