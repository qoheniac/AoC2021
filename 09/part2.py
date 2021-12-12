from numpy import pad, product, zeros_like

with open("input") as f:
    heights = pad(
        [list(map(int, list(line.rstrip()))) for line in f.readlines()],
        1,
        constant_values=9,
    )
basins = zeros_like(heights)
for i0 in range(1, len(heights) - 1):
    for j0 in range(1, len(heights[i0]) - 1):
        if heights[i0, j0] == 9:
            continue
        move = True
        i, j = i0, j0
        while move:
            height = heights[i][j]
            if heights[i][j - 1] < height:
                j -= 1
            elif heights[i - 1][j] < height:
                i -= 1
            elif heights[i + 1][j] < height:
                i += 1
            elif heights[i][j + 1] < height:
                j += 1
            else:
                move = False
                basins[i][j] += 1
print(product(sorted(basins[basins != 0])[-3:]))
