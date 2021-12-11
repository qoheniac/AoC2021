from numpy import array, zeros

# read input
with open("input") as f:
    lines = array(
        [
            [
                [int(num) for num in coord.split(",")]
                for coord in row.split(" -> ")
            ]
            for row in f.read().rstrip().split("\n")
        ]
    )

# init overlaps matrix
x_max, y_max = lines.reshape(2 * len(lines), 2).max(axis=0)
overlaps = zeros((y_max + 1, x_max + 1))

# count overlaps of horizontal and vertical lines
for [x1, y1], [x2, y2] in lines:
    if x1 == x2:
        top, bottom = sorted([y1, y2])
        overlaps[top : bottom + 1, x1] += 1
    elif y1 == y2:
        left, right = sorted([x1, x2])
        overlaps[y1, left : right + 1] += 1
print((overlaps >= 2).sum())
