with open("input") as f:

    # parse dots
    dots = set()
    while (line := f.readline()) != "\n":
        dots.add(tuple([int(n) for n in line.rstrip().split(",")]))

    # parse instruction
    axes = {"x": 0, "y": 1}
    split = f.readline().rstrip().split("=")
    i = axes[split[0][-1]]
    n = int(split[1])
    dots = set(
        [
            tuple([abs(dot[j] - (2 * n if j == i else 0)) for j in range(2)])
            if dot[i] > n
            else dot
            for dot in dots
        ]
    )

    # output number of visible dots
    print(len(dots))
