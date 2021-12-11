from statistics import median

with open("input") as f:
    pos = [int(x) for x in f.read().rstrip().split(",")]

m = round(median(pos))
print(sum([abs(x - m) for x in pos]))
