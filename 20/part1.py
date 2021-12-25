from numpy import pad

# read image enhancement algorithm (IEA) and input image with some extra space
with open("input") as f:
    iea = f.readline().rstrip()
    f.readline()
    old_img = pad([list(line.rstrip()) for line in f], 3, constant_values=".")

# get image height and width and copy image for simultaneous updates
height = len(old_img)
width = len(old_img[0])
new_img = old_img.copy()

# simultaneously update all pixels
for _ in range(2):
    old_img, new_img = new_img, old_img
    for i in range(1, height - 1):
        for j in range(1, width - 1):

            # construct binary from environment and look up new pixel from IEA
            binary = "".join(
                "1" if old_img[m][n] == "#" else "0"
                for m in range(i - 1, i + 2)
                for n in range(j - 1, j + 2)
            )
            index = int(binary, 2)
            new_img[i][j] = iea[index]

    # handle infinite pixels outside input image represented by edge pixels
    new_img = pad(
        new_img[1:-1, 1:-1],
        1,
        constant_values=iea[511] if old_img[0, 0] == "#" else iea[0],
    )

# count lit pixels
print(sum([1 if pxl == "#" else 0 for line in new_img for pxl in line]))
