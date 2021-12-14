with open("input") as f:

    # parse dots
    dots = set()
    while (line := f.readline()) != "\n":
        dots.add(tuple(int(n) for n in line.rstrip().split(",")))

    # parse instruction
    axes = {"x": 0, "y": 1}
    for line in f:
        split = line.rstrip().split("=")
        i = axes[split[0][-1]]
        n = int(split[1])
        dots = set(
            [
                tuple(abs(dot[j] - (2 * n if j == i else 0)) for j in range(2))
                if dot[i] > n
                else dot
                for dot in dots
            ]
        )

# output resulting image
xmax = max(dot[0] for dot in dots)
ymax = max(dot[1] for dot in dots)
output = [["  "] * (xmax + 1) for _ in range(ymax + 1)]
for dot in dots:
    output[dot[1]][dot[0]] = "██"
print("\n".join(["".join(line) for line in output]))
