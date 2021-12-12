count = 0
with open("input") as f:
    for line in f:
        output = line.split(" | ")[1].split()
        for digit in output:
            if len(digit) in [2, 3, 4, 7]:
                count += 1
print(count)
