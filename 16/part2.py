def length_versum_result(bits):

    # read packet header and initialize version sum
    version = int(bits[:3], 2)
    type_id = int(bits[3:6], 2)
    versum = version

    # literal value packet
    if type_id == 4:

        # count groups
        groups = 1
        while bits[6 + 5 * (groups - 1)] == "1":
            groups += 1

        # calculate length and value
        length = 6 + 5 * groups
        result = int(
            "".join([bits[7 + i * 5 : 11 + i * 5] for i in range(groups)]), 2
        )

    # operator packet
    else:

        # initialize list of sub-packet results
        sub_results = []

        # parse sub-packets with given total length
        if bits[6] == "0":
            length = 22 + int(bits[7:22], 2)
            sub_length = 22
            while sub_length < length:
                l, v, r = length_versum_result(bits[sub_length:length])
                sub_length += l
                versum += v
                sub_results.append(r)

        # parse given number of sub-packets
        else:
            length = 18
            for i in range(int(bits[7:18], 2)):
                l, v, r = length_versum_result(bits[length:])
                length += l
                versum += v
                sub_results.append(r)

        # apply operation to sub-packet results
        match type_id:
            case 0:
                result = sum(sub_results)
            case 1:
                result = 1
                for r in sub_results:
                    result *= r
            case 2:
                result = min(sub_results)
            case 3:
                result = max(sub_results)
            case 5:
                result = 1 if sub_results[0] > sub_results[1] else 0
            case 6:
                result = 1 if sub_results[0] < sub_results[1] else 0
            case 7:
                result = 1 if sub_results[0] == sub_results[1] else 0

    # return length, version sum and value of first packet in bits
    return length, versum, result


# read transmission, convert to bits and call above function to get version sum
with open("input") as f:
    transmission = f.read().rstrip()
bits = "".join([f"{int(nibble, 16):04b}" for nibble in transmission])
print(length_versum_result(bits)[2])
