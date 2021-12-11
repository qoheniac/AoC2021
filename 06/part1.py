with open("input") as f:
    timers = [int(t) for t in f.read().rstrip().split(",")]
for _ in range(80):
    for i in range(len(timers)):
        if timers[i] == 0:
            timers[i] = 6
            timers.append(8)
        else:
            timers[i] -= 1
print(len(timers))
