from numpy import append, array, inf, logical_and


def parse_line(line):
    return array(list(map(int, list(line.rstrip()))))


def get_risk(heights, neighbors):
    lows = heights[logical_and.reduce([heights < n for n in neighbors])]
    return sum(lows) + len(lows)


def left_of(heights):
    return append(inf, heights[:-1])


def right_of(heights):
    return append(heights[1:], inf)


risk = 0
with open("input") as f:
    top = parse_line(f.readline())
    mid = parse_line(f.readline())
    risk += get_risk(top, [mid, left_of(top), right_of(top)])  # first row
    for line in f:
        bot = parse_line(line)
        risk += get_risk(mid, [top, bot, left_of(mid), right_of(mid)])
        top, mid, bot = mid, bot, top
    risk += get_risk(mid, [top, left_of(mid), right_of(mid)])  # last row
print(risk)
