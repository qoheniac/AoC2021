class Corrupted(Exception):
    pass


opening = ["(", "[", "{", "<"]
closing = [")", "]", "}", ">"]
points = {")": 3, "]": 57, "}": 1197, ">": 25137}
score = 0
with open("input") as f:
    for line in f:
        memory = []
        for character in list(line):
            try:
                for i, c in enumerate(opening):
                    if c == character:
                        memory.append(i)
                        break
                else:
                    for i, c in enumerate(closing):
                        if c == character:
                            if c == closing[memory[-1]]:
                                memory.pop()
                            else:
                                raise Corrupted
                            break
            except Corrupted:
                score += points[character]
                break
print(score)
