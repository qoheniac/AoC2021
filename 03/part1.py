with open("input", "r") as f:
    ones = [int(bit) for bit in f.readline().rstrip()]
    rows = 1
    cols = len(ones)
    for line in f:
        rows += 1
        for i in range(cols):
            ones[i] += int(line[i])
gamma = 0
epsilon = 0
halfrows = rows / 2
for i, n in enumerate(ones[::-1]):
    if n > halfrows:
        gamma += 2 ** i
    else:
        epsilon += 2 ** i
print(gamma * epsilon)
