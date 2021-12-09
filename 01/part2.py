def parseline(line):
    return int(line.rstrip())


count = 0
with open("input", "r") as f:
    sum1 = parseline(f.readline())
    sum2 = parseline(f.readline())
    sum3 = parseline(f.readline())
    sum1 += sum3 + sum2
    sum2 += sum3
    for line in f:
        new = parseline(line)
        sum2 += new
        sum3 += new
        if sum2 > sum1:
            count += 1
        sum1, sum2 = sum2, sum3
        sum3 = new
print(count)
