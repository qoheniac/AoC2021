# read in y limits of target as x dimension can be ignored
with open("input") as f:
    y_min, y_max = [
        int(lim)
        for lim in f.read()
        .rstrip()
        .split(": ")[1]
        .split(", ")[1]
        .split("=")[1]
        .split("..")
    ]

# assuming y_max negative, then if v_y positive, probe will return to y=0 with
# velocity -1-v_y so target will be missed if v_y larger -1-y_min, therefore
# starting with v0=-1-y_min, trajectory parts below y=0 are checked until a hit
# is found, then maximum y, i.e. v0-th triangular number, is returned
v0 = -1 - y_min
while v0 > 0:
    y_old = y = 0
    v = -v0
    while y > y_min:
        y_old, y = y, y + v
        v -= 1
    if y_old < y_max:
        break
    v0 -= 1
print(v0 * (v0 + 1) // 2)
