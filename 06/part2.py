# input
with open("input") as f:
    init = [int(i) for i in f.read().rstrip().split(",")]

# initialization
fish = [0] * 9
for i in init:
    fish[i] += 1

# growth
for _ in range(256):
    births = fish[0]
    fish[:8] = fish[1:]
    fish[6] += births
    fish[8] = births
print(sum(fish))
