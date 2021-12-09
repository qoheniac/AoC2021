def parseline(line):
    return int(line.rstrip())


count = 0
with open("input", "r") as f:
    old = parseline(f.readline())
    for line in f:
        new = parseline(line)
        if new > old:
            count += 1
        old, new = new, old
print(count)
