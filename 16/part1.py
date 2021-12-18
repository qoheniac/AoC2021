# return length and version sum of first packet in bits
def length_versum(bits):
    version = int(bits[:3], 2)
    type_id = int(bits[3:6], 2)
    if type_id == 4:
        groups = 1
        while bits[6 + 5 * (groups - 1)] == "1":
            groups += 1
        length = 6 + 5 * groups
        versum = version
    else:
        if bits[6] == "0":
            length = 22 + int(bits[7:22], 2)
            versum = version
            sub_length = 22
            while sub_length < length:
                l, v = length_versum(bits[sub_length:length])
                sub_length += l
                versum += v
        else:
            length = 18
            versum = version
            for i in range(int(bits[7:18], 2)):
                l, v = length_versum(bits[length:])
                length += l
                versum += v
    return length, versum


# read transmission, convert to bits and call length_versum to get version sum
with open("input") as f:
    transmission = f.read().rstrip()
bits = "".join([f"{int(nibble, 16):04b}" for nibble in transmission])
print(length_versum(bits)[1])
