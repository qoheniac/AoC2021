# deterministic die generator
def gen_die():
    while True:
        for i in range(1, 101):
            yield i


# read starting positions and set initial scores to zero
with open("input") as f:
    positions = [int(line.rstrip().split(": ")[1]) for line in f]
N = len(positions)
scores = [0] * N

# play game until one player reaches at least 1000 points
roll = enumerate(gen_die())
while True:
    for i in range(N):
        positions[i] = (
            positions[i] + sum([next(roll)[1] for _ in range(3)]) - 1
        ) % 10 + 1
        scores[i] += positions[i]
        if scores[i] >= 1000:
            break
    else:
        continue
    break

# output product of lowest score and number of die rolls
print(min(scores) * next(roll)[0])
