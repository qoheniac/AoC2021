from math import sqrt

# read in x and y limits of target
with open("input") as f:
    x_min, x_max, y_min, y_max = [
        int(lim)
        for dim in f.read().rstrip().split(": ")[1].split(", ")
        for lim in dim.split("=")[1].split("..")
    ]

# calculate area in initial velocity space where hits are possible
v_x_min = round(sqrt(2*x_min+0.25))  # smallest triangular number >= x_min
v_x_max = x_max
v_y_min = y_min
v_y_max = -1 - y_min

# in this velocity area check trajectory parts below y=0 for hits and count
# trajectories that didn't skip the target
count = 0
for v_x_0 in range(v_x_min, v_x_max + 1):
    for v_y_0 in range(v_y_min, v_y_max + 1):
        v_x = v_x_0 if v_y_0 < 0 else max(0, v_x_0 - 2 * v_y_0 - 1)
        v_y = v_y_0 if v_y_0 < 0 else -1 - v_y_0
        x = (v_x_0 * (v_x_0 + 1) - v_x * (v_x + 1)) // 2
        y = 0
        if x > x_max or y < y_min:
            continue
        while x <= x_max and y >= y_min:
            x_old, y_old = x, y
            x += v_x
            y += v_y
            v_x = max(0, v_x - 1)
            v_y -= 1
        if x_old >= x_min and y_old <= y_max:
            count += 1
print(count)
