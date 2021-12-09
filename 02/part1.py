lut = {"forward": 1j, "down": 1, "up": -1}
pos = 0
with open("input", "r") as f:
    for line in f:
        cmd, num = line.split()
        pos += lut[cmd] * int(num)
print(int(pos.real * pos.imag))
