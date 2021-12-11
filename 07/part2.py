with open("input") as f:
    pos = [int(x) for x in f.read().rstrip().split(",")]

best = float("inf")
for m in range(min(pos), max(pos) + 1):
    fuel = sum([(Δ := abs(x - m)) * (Δ + 1) // 2 for x in pos])
    best = min(best, fuel)
print(best)
