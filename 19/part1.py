with open("input") as f:
    data = [
        [
            tuple([int(number) for number in beacon.split(",")])
            for beacon in scanner.rstrip().split("\n")[1:]
        ]
        for scanner in f.read().split("\n\n")
    ]

signals = set([(0, 0, 0)])
beacons = set(data[0])
unlocated = set(range(1, len(data)))

while len(unlocated) > 0:
    print(unlocated)
    for i in unlocated:
        for permutation in range(3):
            for parity in (1, -1):
                for σ in [
                    tuple(parity * (1 if m == n else -1) for m in range(3))
                    for n in range(4)
                ]:
                    # Δs = []
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
                            if Δ in count and count[Δ] > 0:
                                count[Δ] += 1
                                if count[Δ] >= 12:
                                    break
                            else:
                                count[Δ] = 0
                                for signal in signals:
                                    if (
                                        max(
                                            abs(signal[i] - Δ[i])
                                            for i in range(3)
                                        )
                                        < 2000
                                    ):
                                        count[Δ] = 1
                                        break
                        else:
                            continue
                        break
                    else:
                        continue
                    signals.add(Δ)
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
print(len(beacons))
