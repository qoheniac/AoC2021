# read relative beacon positions
with open("input") as f:
    data = [
        [
            tuple([int(number) for number in beacon.split(",")])
            for beacon in scanner.rstrip().split("\n")[1:]
        ]
        for scanner in f.read().split("\n\n")
    ]

# initialization
scanners = [(0, 0, 0)]
beacons = set(data[0])
unlocated = set(range(1, len(data)))
N = len(unlocated)

# iterate unlocated scanners until all are located
while len(unlocated) > 0:
    print(f"{round(100 * (1 - len(unlocated) / N)):3d}%", end="\r")
    for i in unlocated:

        # iterate rotations
        for permutation in range(3):
            for parity in (1, -1):
                for σ in [
                    (parity, parity, parity),
                    (parity, -parity, -parity),
                    (-parity, parity, -parity),
                    (-parity, -parity, parity),
                ]:

                    # calculate differences between relative beacon locations
                    # and known absolute beacon locations and count occurrences
                    count = dict()
                    for abs_beacon in beacons:
                        for rel_beacon in data[i]:
                            beacon = (
                                σ[0] * rel_beacon[permutation],
                                σ[1] * rel_beacon[(permutation + parity) % 3],
                                σ[2] * rel_beacon[(permutation - parity) % 3],
                            )
                            Δ = tuple(
                                abs_beacon[i] - beacon[i] for i in range(3)
                            )
                            count[Δ] = count[Δ] + 1 if Δ in count else 1

                            # if occurs for twelfth time save scanner position,
                            # calculate absolute beacon positions and continue
                            # with an yet unlocated scanner if one is left
                            if count[Δ] == 12:
                                break
                        else:
                            continue
                        break
                    else:
                        continue
                    scanners.append(Δ)
                    for rel_beacon in data[i]:
                        beacon = (
                            σ[0] * rel_beacon[permutation],
                            σ[1] * rel_beacon[(permutation + parity) % 3],
                            σ[2] * rel_beacon[(permutation - parity) % 3],
                        )
                        beacons.add(tuple(Δ[i] + beacon[i] for i in range(3)))
                    unlocated.remove(i)
                    break
                else:
                    continue
                break
            else:
                continue
            break
        else:
            continue
        break

# find and print largest Manhattan distance between scanners
N = len(scanners)
largest_distance = 0
for i in range(N - 1):
    for j in range(i, N):
        largest_distance = max(
            largest_distance,
            sum([abs(scanners[i][k] - scanners[j][k]) for k in range(3)]),
        )
print(largest_distance)
