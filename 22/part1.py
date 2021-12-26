from numpy import full


def parse_limits(limits):
    result = [0] * 6
    for i, dimension in enumerate(limits.split(",")):
        interval = dimension.split("=")[1]
        lower, upper = interval.split("..")
        result[2 * i] = min(max(0, int(lower) + 50), 101)
        result[2 * i + 1] = min(max(0, int(upper) + 51), 101)
    return result


reactor = full((101,) * 3, False)
with open("input") as f:
    for line in f:
        columns = line.rstrip().split(" ")
        state = columns[0] == "on"
        c = parse_limits(columns[1])
        cuboid = full((c[1] - c[0], c[3] - c[2], c[5] - c[4]), state)
        reactor[c[0] : c[1], c[2] : c[3], c[4] : c[5]] = cuboid
print(reactor.sum())
