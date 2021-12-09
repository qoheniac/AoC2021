aim = 0
pos = 0
with open("input", "r") as f:
    for line in f:
        cmd, num = line.split()
        num = int(num)
        match cmd:
            case "down":
                aim += num
            case "up":
                aim -= num
            case "forward":
                pos += (1j + aim) * num
print(int(pos.real * pos.imag))
